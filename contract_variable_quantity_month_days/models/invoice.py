# -*- coding: utf-8 -*-
from odoo import models, fields
from calendar import monthrange


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    contract_month_factor = fields.Float(
        string='Contract Month Factor',
        compute='_compute_contract_month')
    contract_month = fields.Integer(
        string='Contract Month',
        compute='_compute_contract_month')
    contract_year = fields.Integer(
        string='Contract Year',
        compute='_compute_contract_month')

    def _compute_contract_month(self):
        for invoice in self:
            if invoice.contract_id:

                date_invoice = fields.Date.from_string(invoice.date_invoice)

                invoice.contract_month = date_invoice.month
                invoice.contract_year = date_invoice.year

                if invoice.recurring_invoice_type == 'post-paid':
                    if invoice.contract_month == 1:
                        invoice.contract_month == 12
                        invoice.contract_year -= 1
                    else:
                        invoice.contract_month -= 1

                date_start_contract = invoice.contract_id.date_start and \
                    fields.Date.from_string(
                        invoice.contract_id.date_start)

                date_end_contract = invoice.contract_id.date_end and \
                    fields.Date.from_string(
                        invoice.contract_id.date_end)
                month_days = monthrange(
                    date_invoice.year, date_invoice.month)[1]
                if invoice.contract_month == date_start_contract.month:
                    contract_days = month_days - date_start_contract.day
                    invoice.contract_month_factor = contract_days / month_days
                elif date_end_contract and \
                        invoice.contract_month == date_end_contract.mont:
                    contract_days = date_end_contract.day
                    invoice.contract_month_factor = contract_days / month_days
                elif (invoice.contract_month < date_start_contract.month) or (
                        date_end_contract and
                        invoice.contract_month > date_end_contract.mont
                ):
                    invoice.contract_month_factor = 0.0
                else:
                    invoice.contract_month_factor = 1.0
