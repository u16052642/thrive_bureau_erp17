# -*- coding: utf-8 -*-

import thrive

def migrate(cr, version):
    registry = thrive.registry(cr.dbname)
    from thrive.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_in')
