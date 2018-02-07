# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    service_partner_id = fields.Many2one(
        'res.partner',
        string="Service Address")

    contact_partner_id = fields.Many2one(
        'res.partner',
        string="Contact Address")

    def _prepare_invoice(self):
        invoice = super(AccountAnalyticAccount,
                        self)._prepare_invoice()
        invoice.update({
            'partner_shipping_id': self.service_partner_id
                and self.service_partner_id.id})
        return invoice
