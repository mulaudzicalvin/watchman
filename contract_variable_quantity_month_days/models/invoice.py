# -*- coding: utf-8 -*-
from odoo import models, fields
from calendar import monthrange


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    contract_days = fields.Integer(
        string='Contract Days',
        compute='_compute_contract_days')

    @api.multi
    def _compute_contract_days(self):
        for invoice in self:
            if invoice.contract_id:
                date_invoice = fields.Date.from_string(invoice.date_invoice)
                date_start_contract = invoice.contract_id.date_start and
                    fields.Date.from_string(
                        invoice.contract_id.date_start)
                date_end_contract = invoice.contract_id.date_end and
                    fields.Date.from_string(
                        invoice.contract_id.date_end)
                if date_invoice.month = date_start_contract.mont:
                    invoice.contract_days = monthrange(
                        date_invoice.year, date_invoice.month)[1] - \
                        date_start_contract.day
                elif date_end_contract and
                        date_invoice.month >= date_end_contract.mont:
                    invoice.contract_days = date_end_contract.day
                else:
                    invoice.contract_days = monthrange(
                        date_invoice.year, date_invoice.month)[1]
