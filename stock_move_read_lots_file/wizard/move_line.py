# -*- coding: utf-8 -*-
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, api, fields, _
from odoo.exceptions import ValidationError
import base64
import xlrd


class WizardMoveLine(models.TransientModel):
    _name = 'wizard.move.line'

    file_name = fields.Char(
        string='File Name')

    lot_file = fields.Binary(
        string='Load File')

    @api.multi
    def load_lots_numbers(self):
        move_obj = self.env['stock.move'].browse(
            self._context.get('default_move_id'))
        move_line_obj = self.env['stock.move.line']
        lot_string = []
        if self.file_name and self.lot_file:
            name = self.file_name.split('.')
            if name[1] == 'xls':
                wb = xlrd.open_workbook(
                    file_contents=base64.decodestring(self.lot_file))
                ws = wb.sheet_by_index(0)
                for rownum in xrange(ws.nrows):
                    a = ws.row_values(rownum)[0]
                    lot_string.append(int(a))
            elif name[1] == 'csv':
                f = base64.b64decode(self.lot_file)
                lot_string = f.decode('utf-8').split('\n')
                lot_string.pop(-1)
            else:
                raise ValidationError(
                    _("You can olny upload csv or xls files"))
            for row in lot_string:
                data = {
                    'lot_name': row,
                    'qty_done': 1.0,
                    'product_uom_qty': 1.0,
                    'product_uom_id': move_obj.product_uom.id,
                    'location_id': move_obj.location_id.id,
                    'location_dest_id': move_obj.location_dest_id.id
                }
                line = move_line_obj.create(data)
                move_obj.move_line_ids += line
        else:
            raise ValidationError(
                _("You must to upload a file first"))
