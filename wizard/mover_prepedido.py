# -*- coding: utf-8 -*-
from odoo import fields, models, _
import logging
from odoo.exceptions import UserError, ValidationError

class MoverPrepedidoWizard(models.TransientModel):
        _name = "mover_prepedido.wizard"
        _description = 'Comentario wizard'
        
        prepedido_id = fields.Many2one('mrp.eco','Prepedido')
       
        def confirmar(self):
            for movimiento in self:
                ids = self.env.context.get('active_ids', [])
                logging.warning(ids)
                prepedido_ids = self.env['prada.pim.line'].search([('id','in',ids)])
                logging.warning(prepedido_ids)
                for prepedido in prepedido_ids:
                    prepedido.sudo().write({'eco_id': movimiento.prepedido_id.id})
            return {'type': 'ir.actions.act_window_close'}