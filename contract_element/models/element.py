# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import calendar


class AccountAnalyticAccountElement(models.Model):
    _name = 'account.analytic.account.element'
    _name_rec = 'qr'

    contract_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Contract')

    qr = fields.Char(
        string='QR')

    vi = fields.Char(
        string='VI')

    start_date = fields.Date(
        string='Start Date')

    end_date = fields.Date(
        string='End Date')

    start_date_percent = fields.Float(
        string='Start Date Percent',
        compute='_compute_start_date_percent')

    end_date_percent = fields.Float(
        string='End Date Percent',
        compute='_compute_end_date_percent')

    def _compute_start_date_percent(self):
        for record in self.filtered(lambda r: r.start_date):
            month_day_number = calendar.monthrange(
                fields.Date.from_string(record.start_date).year,
                fields.Date.from_string(record.start_date).month)[1]
            month_day = fields.Date.from_string(record.start_date).day
            record.start_date_percent = (
                month_day_number - month_day) / month_day_number

    def _compute_end_date_percent(self):
        for record in self.filtered(lambda r: r.end_date):
            month_day_number = calendar.monthrange(
                fields.Date.from_string(record.end_date).year,
                fields.Date.from_string(record.end_date).month)[1]
            month_day = fields.Date.from_string(record.end_date).day
            record.end_date_percent = 1 - \
                ((month_day_number - month_day) / month_day_number)

    @api.constrains('qr', 'end_date')
    def _check_field(self):
        last_qr = ''
        for record in self.search([]):
            if record.qr == last_qr and not record.end_date:
                raise ValidationError(
                    _("You can't add more than one line with the same QR "
                      "and without end date"))
            last_qr = record.qr
