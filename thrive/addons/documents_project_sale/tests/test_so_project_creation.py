# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import Command
from thrive.tests.common import tagged

from thrive.addons.sale_project.tests.common import TestSaleProjectCommon


@tagged("-at_install", "post_install")
class testSoProjectCreation(TestSaleProjectCommon):

    def test_template_parent_folder(self):
        """
        When a single workspace template is used for a project generated by a SO,
        the copied workspace should be placed in the same folder as the template.
        When multiple workspace templates are used for a single project, the
        created workspace should be in the 'Projects' workspace.
        If there are multiple products, but with the same template, then the
        created workspace should be a simple copy of that template, and in the same folder.
        """
        parent_folder = self.env['documents.folder'].create({
            'name': 'Parent Folder',
        })
        template_folder_1, template_folder_2 = self.env['documents.folder'].create([{
            'name': 'Template Folder 1',
            'parent_folder_id': parent_folder.id,
        }, {
            'name': 'Template Folder 2',
            'parent_folder_id': parent_folder.id,
        }])

        product_template_1, product_template_2 = self.env['product.template'].create([{
            'name': 'Product 1',
            'type': 'service',
            'service_tracking': 'project_only',
            'template_folder_id': template_folder_1.id,
        }, {
            'name': 'Product 2',
            'type': 'service',
            'service_tracking': 'project_only',
            'template_folder_id': template_folder_2.id,
        }])
        product_1 = self.env['product.product'].search([('product_tmpl_id', '=', product_template_1.id)])
        product_2 = self.env['product.product'].search([('product_tmpl_id', '=', product_template_2.id)])

        # SO with a single product with a workspace template
        sales_order_1 = self.env['sale.order'].create({
            'partner_id': self.partner_a.id,
            'order_line': [Command.create({'product_id': product_1.id})],
        })
        sales_order_1.action_confirm()

        self.assertEqual(sales_order_1.project_count, 1)
        so1_project = sales_order_1.project_ids[0]
        so1_project_workspace = so1_project.documents_folder_id
        self.assertEqual(so1_project_workspace.parent_folder_id.id, template_folder_1.parent_folder_id.id)

        # SO with two different products with different workspace templates
        sales_order_2 = self.env['sale.order'].create({
            'partner_id': self.partner_a.id,
            'order_line': [
                Command.create({'product_id': product_1.id}),
                Command.create({'product_id': product_2.id}),
            ],
        })
        sales_order_2.action_confirm()

        self.assertEqual(sales_order_2.project_count, 1)
        so2_project = sales_order_2.project_ids[0]
        so2_project_workspace = so2_project.documents_folder_id
        documents_project_folder = self.env.ref('documents_project.documents_project_folder')
        self.assertEqual(so2_project_workspace.parent_folder_id.id, documents_project_folder.id)

        # SO with two different products with the same workspace template
        product_template_2.template_folder_id = template_folder_1.id
        sales_order_3 = self.env['sale.order'].create({
            'partner_id': self.partner_a.id,
            'order_line': [
                Command.create({'product_id': product_1.id}),
                Command.create({'product_id': product_2.id}),
            ],
        })
        sales_order_3.action_confirm()

        self.assertEqual(sales_order_3.project_count, 1)
        so3_project = sales_order_3.project_ids[0]
        so3_project_workspace = so3_project.documents_folder_id
        self.assertEqual(so3_project_workspace.parent_folder_id.id, template_folder_1.parent_folder_id.id)

    def test_multiple_templates_same_so(self):
        project_template_1, project_template_2 = self.env['project.project'].create([{
            'name': f'Project Template {i + 1}',
        } for i in range(2)])

        parent_template_folder = self.env['documents.folder'].create({
            'name': 'Parent',
        })

        template_folder_1, template_folder_2, template_folder_3 = self.env['documents.folder'].create([{
            'name': f'Template Folder {i + 1}',
            'parent_folder_id': parent_template_folder.id,
            'description': f'{i + 1}',
        } for i in range(3)])

        product_templates = self.env['product.template'].create([{
            'name': f'Product Template {i + 1}',
            'type': 'service',
            'service_tracking': 'project_only'
        } for i in range(7)])

        for i, (project_id, folder_id) in enumerate((
            (project_template_1.id, template_folder_1.id),
            (project_template_1.id, template_folder_1.id),
            (project_template_1.id, template_folder_2.id),
            (project_template_2.id, template_folder_2.id),
            (project_template_2.id, False),
            (False, template_folder_3.id),
            (False, template_folder_2.id),
        )):
            product_templates[i].write({
                'project_template_id': project_id,
                'template_folder_id': folder_id,
            })
        products = self.env['product.product'].search([('product_tmpl_id', 'in', product_templates.ids)], order="id asc")

        sales_order = self.env['sale.order'].create({
            'partner_id': self.partner_a.id,
            'order_line': [Command.create({'product_id': products[i].id}) for i in range(7)],
        })
        sales_order.action_confirm()

        self.assertEqual(sales_order.project_count, 3, "There should be 3 projects created: one per project template, plus one for products without template.")
        project_1, project_2, project_3 = sales_order.project_ids

        project_1_workspace = project_1.documents_folder_id
        self.assertTrue("1" in project_1_workspace.description and "2" in project_1_workspace.description, "The workspace should be a combination of templates 1 and 2.")

        project_2_workspace = project_2.documents_folder_id
        self.assertEqual(project_2_workspace.parent_folder_id.id, parent_template_folder.id, "The workspace should be a copy of template 2.")

        project_3_workspace = project_3.documents_folder_id
        self.assertTrue("2" in project_3_workspace.description and "3" in project_3_workspace.description, "The workspace should be a copy of templates 2 and 3.")

    def test_project_template_with_documents_disabled(self):
        template_folder = self.env['documents.folder'].create({
            'name': 'Template Folder',
        })
        template_project = self.env['project.project'].create({
            'name': 'Template Project',
            'use_documents': False,
        })
        product_template = self.env['product.template'].create({
            'name': 'Product 1',
            'type': 'service',
            'service_tracking': 'project_only',
        })

        product_template.template_folder_id = template_folder
        product_template.project_template_id = template_project
        product_template._compute_template_folder_id()
        self.assertFalse(template_project.use_documents)
        self.assertFalse(product_template.template_folder_id, "Setting a project template with the documents feature disabled should unset the workspace template.")

        product = self.env['product.product'].search([('product_tmpl_id', '=', product_template.id)])
        sales_order = self.env['sale.order'].create({
            'partner_id': self.partner_a.id,
            'order_line': [Command.create({'product_id': product.id})],
        })
        sales_order.action_confirm()
        self.assertFalse(sales_order.project_ids.use_documents, "The generated project should have the documents feature disabled.")

    def test_workspace_from_project(self):
        """
            This tests the flow of creating a project and then using
            that project and its workplace to create the product
        """
        project_template = self.env['project.project'].create({
            'name': 'Test Project',
        })
        self.env['product.template'].create({
            'name': 'Test product',
            'type': 'service',
            'service_tracking': 'task_in_project',
            'project_template_id': project_template.id,
            'template_folder_id': project_template.documents_folder_id.id,
        })
