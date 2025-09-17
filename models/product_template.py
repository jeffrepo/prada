# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    marca_id = fields.Many2one('prada.marca', 'Marca')
    codigo_prada = fields.Char('Código prada')
    modelo = fields.Char('Modelo')
    departamento_id = fields.Many2one('prada.departamento', 'Departamento')
    seccion_id = fields.Many2one('prada.seccion', 'Sección')
    silueta_id = fields.Many2one('prada.silueta', 'Silueta')
    #horma_id = fields.Many2one('prada.horma', 'Horma')
    horma = fields.Char('HORMA')
    material_id = fields.Many2one('prada.material', 'Material')
    color_id = fields.Many2one('prada.color', 'Color')
    atributo1_id = fields.Many2one('prada.atributo1', 'Atributo 1')
    atributo2_id = fields.Many2one('prada.atributo2', 'Atributo 2')
    ocasion_id = fields.Many2one('prada.ocasion', 'Ocasión')
    no_juego = fields.Char('No juego')
    juego1 = fields.Char('Juego 1')
    juego2 = fields.Char('Juego 2')
    juego3 = fields.Char('Juego 3')
    categoria_id = fields.Many2one('prada.categoria', 'Categoría')
    tendencia_id = fields.Many2one('prada.tendencia', 'Tendencia')
    coleccion_id = fields.Many2one('prada.coleccion', 'Colección')
    tienda_id = fields.Many2one('prada.tienda', 'Tienda')


    @api.onchange('default_code')
    def _onchange_default_code(self):
        if not self.default_code:
            return

        domain = [('default_code', '=', self.default_code)]
        if self.id.origin:
            domain.append(('id', '!=', self.id.origin))

        if self.env['product.template'].search_count(domain, limit=1):
            self.default_code = False
            return {'warning': {
                'title': _("Note:"),
                'message': _("Referencia interna ya existe."),
            }}