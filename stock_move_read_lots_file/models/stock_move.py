# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3).

from openerp import models, api, fields, _
from odoo.exceptions import ValidationError
import base64


class StockMove(models.Model):
    _inherit = 'stock.move'

    # file_name = fields.Char(
    #     string='File Name')
    #
    # lot_file = fields.Binary(
    #     string='Load File')
    #
    # @api.multi
    # def load_lots_numbers(self):
    #     move_line_obj = self.env['stock.move.line']
    #     lot_value = []
    #     lot_obj = []
    #     if self.lot_file:
    #         f = base64.b64decode(self.lot_file)
    #         lot_string = f.decode('utf-8').split('\n')
    #         lot_string.pop(-1)
    #         for row in lot_string:
    #             data = {
    #                 'picking_id': self.picking_id.id,
    #                 'move_id': self.id,
    #                 'lot_name': row,
    #                 'qty_done': 1,
    #                 'product_uom_qty': 1,
    #                 'product_uom_id': self.product_uom.id,
    #                 'location_id': self.location_id.id,
    #                 'location_dest_id': self.location_dest_id.id
    #             }
    #             lot_obj.append(move_line_obj.create((data)))
    #             lot_value.append((0, 0, data))
    #         import wdb
    #         wdb.set_trace()
    #         self.write({
    #             'move_line_ids': [lot_value]
    #         })
    #     else:
    #         raise ValidationError(
    #             _("You must to upload a file first"))
