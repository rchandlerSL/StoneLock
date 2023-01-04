# -*- coding: utf-8 -*-
from odoo.addons.base.maintenance.migrations import util


def migrate(cr, version):
    util.force_noupdate(cr, "sale_enterprise.sale_report_action_dashboard", noupdate=False)
    cr.execute(
        """
        UPDATE ir_filters
           SET action_id = %s
         WHERE model_id = 'sale.report'
          AND action_id = %s
        """,
        [util.ref(cr, "sale.action_order_report_all"), util.ref(cr, "sale_enterprise.sale_report_action_dashboard")],
    )