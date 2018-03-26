from odoo import models, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def action_rfq_send(self):
        self.ensure_one()
        template_id = False
        if self.env.context.get('send_rfq', False):
            template_id = self.company_id.mail_template_purchase_id
        else:
            template_id = self.company_id.mail_template_purchase_done_id

        if not template_id:
            return super(PurchaseOrder, self).action_rfq_send()

        compose_form = self.env.ref(
            'mail.email_compose_message_wizard_form', False)
        ctx = dict(self.env.context or {})
        ctx.update({
            'default_model': 'purchase.order',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'custom_layout':
                "purchase."
                "mail_template_data_notification_email_purchase_order",
            'force_email': True
        })
        return {
            'name': _('Compose Email'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }
