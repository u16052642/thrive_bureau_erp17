# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import api, models


class HrPayrollStructure(models.Model):
    _inherit = "hr.payroll.structure"

    @api.model_create_multi
    def create(self, vals):
        structures = super().create(vals)
        to_unlink = self.env["hr.salary.rule"]
        for struct in structures:
            if struct.country_id.code != "AU":
                continue
            to_unlink += struct.rule_ids.filtered(lambda r: r.code == 'CHILD_SUPPORT')
        to_unlink.unlink()
        return structures
