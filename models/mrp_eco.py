# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
from random import randint

import ast

from odoo import api, fields, models, tools, Command, _
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError
import logging

class MrpEco(models.Model):
    _inherit = 'mrp.eco'

    #importaciones tambien puede editarlo

    tipo_cambio = fields.Float('Tipo de cambio',digits=(16, 4), compute = '_calcular_tipo_cambio', store = True, readonly = False, groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    gastos = fields.Float('Gastos (%)', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    iva = fields.Float('IVA (%)', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    marcaje = fields.Float('Marcaje', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    line_ids = fields.One2many('prada.pim.line','eco_id',string='PIM')
    fecha = fields.Date('Fecha', default = fields.Date.today(), readonly = False, groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    total_modelos = fields.Integer('Total modelos', compute='_calcular_totales')
    total_costo_promedio = fields.Float('Total costo promedio', compute='_calcular_totales')
    total_corrida_promedio = fields.Float('Total corrida promedio', compute='_calcular_totales')
    suma_unidades = fields.Integer('Suma unidades', compute='_calcular_totales')

    @api.depends('line_ids')
    def _calcular_totales(self):
        for plm in self:
            total_modelos = 0
            promedio = 0.0
            corrida = 0
            suma_unidades = 0
    
            for linea in plm.line_ids:
                total_modelos += 1
                promedio += linea.costo
                corrida += linea.corrida
                suma_unidades += linea.corrida
    
            plm.total_modelos = total_modelos
            plm.total_costo_promedio = promedio / total_modelos if total_modelos else 0.0
            plm.total_corrida_promedio = corrida / total_modelos if total_modelos else 0.0
            plm.suma_unidades = suma_unidades

    @api.depends('fecha')
    def _calcular_tipo_cambio(self):
        eur_moneda = self.env['res.currency'].search([('name','=','EUR')])
        tipo_cambio = self.env['res.currency']._get_conversion_rate(
            from_currency= eur_moneda,
            to_currency=self.company_id.currency_id,
            company=self.company_id,
            date=self.fecha,
        )
        logging.warning('tipo_cambio')
        logging.warning(tipo_cambio)
        self.tipo_cambio = tipo_cambio
        if self.line_ids:
            for linea in self.line_ids:
                linea._compute_valores()

    @api.onchange('tipo_cambio')
    def _onchange_tipo_cambio(self):
        for pl in self:
            if pl.line_ids:
                for linea in self.line_ids:
                    linea._compute_valores()
                

    