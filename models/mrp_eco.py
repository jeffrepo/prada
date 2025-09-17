# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class MrpEco(models.Model):
    _inherit = 'mrp.eco'

    tipo_cambio = fields.Float('Tipo de cambio',digits=(16, 4), compute = '_calcular_tipo_cambio', store = True, readonly = False)
    gastos = fields.Float('Gastos (%)')
    iva = fields.Float('IVA (%)')
    marcaje = fields.Float('Marcaje')
    line_ids = fields.One2many('prada.pim.line','eco_id',string='PIM')
    fecha = fields.Date('Fecha', default = fields.Date.today(), readonly = False)
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
                corrida += int(linea.corrida_id.name)
                suma_unidades += int(linea.corrida_id.name)
    
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