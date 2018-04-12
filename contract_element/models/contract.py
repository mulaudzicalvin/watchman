# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    contract_element_ids = fields.One2many(
        comodel_name='account.analytic.account.element',
        inverse_name='contract_id',
        string='Contract Elements')

    @api.multi
    def getElementByMonth(self, month):
        # for invoice_line in self.recurring_invoice_line_ids:
        # for element in self.contract_element_ids:
        pass

    @api.model
    def set_element(self, cif, qr, vi, date):
        partner = self.env['res.partner'].search([
            ('vat', '=', cif)
        ])
        if partner:
            contract = self.search([
                ('partner_id', '=', partner.id)
            ])
            element = self.env['account.analytic.account.element'].create({
                'qr': qr,
                'vi': vi,
                'start_date': date,
                'contract_id': contract.id
            })
            return element
        else:
            raise ValidationError(
                _('No partner found with this cif'))

    @api.model
    def unset_element(self, qr, date):
        element = self.env['account.analytic.account.element'].search([
            ('qr', '=', qr),
            ('end_date', '=', False)
        ])
        if element:
            element.end_date = date
            return element
        else:
            raise ValidationError(
                _('No element found with this qr'))
