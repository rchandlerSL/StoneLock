# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
import datetime

class crmLead(models.Model):
    _inherit = 'crm.lead'

    days_spent = fields.Integer(compute='_compute_difference',string="Opportunity Age")

    def _compute_difference(self):
        for rec in self:
            date_spent = (datetime.datetime.today()- rec.date_last_stage_update)
            rec.days_spent = date_spent.days
            if rec.days_spent > 0 and (date_spent.seconds/3600) % 24 >= 1:
                rec.days_spent += 1