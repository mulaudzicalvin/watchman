from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    mail_template_invoice_id = fields.Many2one(
        comodel_name='mail.template',
        string='Invoice Email Template')
