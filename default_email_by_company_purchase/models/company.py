from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    mail_template_purchase_id = fields.Many2one(
        comodel_name='mail.template',
        string='Purchase Email Template')
    mail_template_purchase_done_id = fields.Many2one(
        comodel_name='mail.template',
        string='Purchase Done Email Template')
