# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'complete_name_clave'

    complete_name_clave = fields.Char(
        'Complete Name', compute='_compute_complete_name_clave', recursive=True,
        store=True)

    @api.depends('name', 'ref')
    def _compute_complete_name_clave(self):
        for objeto in self:
            if objeto.ref:
                objeto.complete_name_clave = '%s' % (objeto.ref)
            else:
                objeto.complete_name_clave = objeto.name

class PradaCategoria(models.Model):
    _name = 'prada.proveedor'
    _rec_name = 'clave'
    _description = 'Proveedor'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    marca_id = fields.Many2one('prada.marca','Marca')

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.proveedor'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaTemp(models.Model):
    _name = 'prada.temp'
    _description = 'Temp'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.temp'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaMarca(models.Model):
    _name = 'prada.marca'
    _rec_name = 'name'
    _description = 'Marca'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.marca'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaDepartamento(models.Model):
    _name = 'prada.departamento'
    _rec_name = 'clave'
    _description = 'Departamento'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.departamento'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaSeccion(models.Model):
    _name = 'prada.seccion'
    _rec_name = 'clave'
    _description = 'Seccion'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.seccion'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))


class PradaSilueta(models.Model):
    _name = 'prada.silueta'
    _rec_name = 'clave'
    _description = 'Silueta'

    name = fields.Char('name')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.silueta'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaHorma(models.Model):
    _name = 'prada.horma'
    _description = 'Horma'

    name = fields.Char('Nombre')

class PradaMaterial(models.Model):
    _name = 'prada.material'
    _rec_name = 'clave'
    _description = 'Material'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.material'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaColor(models.Model):
    _name = 'prada.color'
    _rec_name = 'clave'
    _description = 'Color'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.color'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaAtributo1(models.Model):
    _name = 'prada.atributo1'
    _rec_name = 'clave'
    _description = 'Atributo1'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.atributo1'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaAtributo2(models.Model):
    _name = 'prada.atributo2'
    _rec_name = 'clave'
    _description = 'Atributo2'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.atributo2'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))


class PradaOcasion(models.Model):
    _name = 'prada.ocasion'
    _rec_name = 'clave'
    _description = 'Ocasion'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.ocasion'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaCategoria(models.Model):
    _name = 'prada.categoria'
    _rec_name = 'clave'
    _description = 'Categoria'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.categoria'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))


class PradaTendencia(models.Model):
    _name = 'prada.tendencia'
    _rec_name = 'clave'
    _description = 'Tendencia'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name', recursive=True,
        store=True)

    @api.depends('name', 'clave')
    def _compute_complete_name(self):
        for objeto in self:
            if objeto.clave:
                objeto.complete_name = '%s - %s' % (objeto.clave, objeto.name)
            else:
                objeto.complete_name = objeto.name

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.tendencia'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaColeccion(models.Model):
    _name = 'prada.coleccion'
    _rec_name = 'clave'
    _description = 'Coleccion'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.coleccion'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaTienda(models.Model):
    _name = 'prada.tienda'
    _rec_name = 'clave'
    _description = 'Tienda'

    clave = fields.Char('CLAVE')
    name = fields.Char('NOMBRE')

    @api.onchange('clave')
    def _onchange_clave(self):
        if not self.clave:
            return

        id_local = self._origin.id
        dominio = [('id', '!=', id_local),('clave','=',self.clave)]
        if self.env['prada.tienda'].search_count(dominio):
            raise ValidationError(_('Clave repetida'))

class PradaTroquel(models.Model):
    _name = 'prada.troquel'
    _description = 'Troquel'

    name = fields.Char('Nombre')

class PradaEstadoWeb(models.Model):
    _name = 'prada.estado_web'
    _description = 'estado_web'

    name = fields.Char('Nombre')

class PradaEstadoMarketing(models.Model):
    _name = 'prada.estado_marketing'
    _description = 'Marketing'

    name = fields.Char('Nombre')


class PradaCambiosPreconfirmacion(models.Model):
    _name = 'prada.cambios_preconfirmacion'
    _description = 'Cambios preconfirmacion'

    name = fields.Char('Nombre')

class PradaCorrida(models.Model):
    _name = 'prada.corrida'
    _description = 'Corrida'

    name = fields.Char('CORRIDA', required=True)

    temp = fields.Many2one('prada.temp', 'TEMPORADA DEL ARTÍCULO')
    seccion_id = fields.Many2one('prada.seccion', string='SECCIÓN', required=True)
    coleccion_id = fields.Many2one('prada.coleccion', string='COLECCIÓN', required=True)
    departamento_id = fields.Many2one('prada.departamento', string='DEPARTAMENTO', required=True)
    talla = fields.Float('35')
    columna1 = fields.Float('36')
    columna2 = fields.Float('37')
    columna3 = fields.Float('38')
    columna4 = fields.Float('39')
    columna5 = fields.Float('40')
    columna6 = fields.Float('41')
    columna7 = fields.Float('42')
    columna8 = fields.Float('43')
    columna9 = fields.Float('44')
    columna10 = fields.Float('45')
    columna12 = fields.Float('46')
    columna13 = fields.Float('47')
    columna14 = fields.Float('48')
    columna15 = fields.Float('49')
    columna16 = fields.Float('50')
    columna17 = fields.Float('90')
    columna18 = fields.Float('100')
    columna19 = fields.Float('105')
    columna20 = fields.Float('110')
    columna21 = fields.Float('120')
    columna22 = fields.Float('GD')
    columna23 = fields.Float('MD')

    columna11 = fields.Float('UNI')
    totalu = fields.Float('TotalU', compute='_compute_totalu')
    total = fields.Float('Total',store = True ,compute='_compute_total')

    @api.depends(
        'talla','columna1','columna2','columna3','columna4',
        'columna5','columna6','columna7','columna8','columna9',
        'columna10','columna11','columna12','columna13','columna14','columna15','columna16',
        'columna17','columna18','columna19','columna20','columna21','columna22','columna23'
    )
    def _compute_total(self):
        for corrida in self:
            corrida.total = (
                (corrida.talla or 0) +
                (corrida.columna1 or 0) +
                (corrida.columna2 or 0) +
                (corrida.columna3 or 0) +
                (corrida.columna4 or 0) +
                (corrida.columna5 or 0) +
                (corrida.columna6 or 0) +
                (corrida.columna7 or 0) +
                (corrida.columna8 or 0) +
                (corrida.columna9 or 0) +
                (corrida.columna10 or 0) +
                (corrida.columna11 or 0) +
                (corrida.columna12 or 0) +
                (corrida.columna13 or 0) +
                (corrida.columna14 or 0) +
                (corrida.columna15 or 0) +
                (corrida.columna16 or 0) +
                (corrida.columna17 or 0) +
                (corrida.columna18 or 0) +
                (corrida.columna19 or 0) +
                (corrida.columna20 or 0) +
                (corrida.columna21 or 0) +
                (corrida.columna22 or 0) +
                (corrida.columna23 or 0)
            )

    @api.depends(
        'talla','columna1','columna2','columna3','columna4',
        'columna5','columna6','columna7','columna8','columna9',
        'columna10','columna11','total'
    )
    def _compute_totalu(self):
        for corrida in self:
            corrida.totalu = corrida.total



    @api.onchange('seccion_id','departamento_id','name', 'coleccion_id', 'temp')
    def _onchange_apartados(self):
        if self.seccion_id and self.departamento_id and self.name:
            corrida_id = self._origin
            dominio = [('id', '!=', corrida_id.id),('seccion_id','=',self.seccion_id.id),('departamento_id','=', self.departamento_id.id), ('name','=', self.name),('coleccion_id','=', self.coleccion_id.id),('temp','=', self.temp.id)]
            if self.env['prada.corrida'].search_count(dominio):
                raise ValidationError(_('Corrida repetida'))


class PradaPimLine(models.Model):
    _name = 'prada.pim.line'
    _description = 'Pim line for plm'

    eco_id = fields.Many2one('mrp.eco', 'PRE PEDIDO')
    producto_id = fields.Many2one('product.template', 'PRODUCTO')
    prada_image = fields.Binary(string="FOTO",related='producto_id.image_1920', store = True, readonly=False)
    temp = fields.Many2one('prada.temp', 'TEMPORADA DEL ARTÍCULO')
    proveedor_id = fields.Many2one('prada.proveedor', 'PROVEEDOR')
    marca_id = fields.Many2one('prada.marca', 'MARCA', readonly = False, store = True, related='proveedor_id.marca_id')
    codigo_prada = fields.Char('CÓDIGO PRADA', readonly = False, store = True)
    modelo = fields.Char('MODELO', readonly = False, store = False, related = 'producto_id.modelo')
    departamento_id = fields.Many2one('prada.departamento', 'DEPARTAMENTO', readonly = False, store = True, related = 'producto_id.departamento_id')
    seccion_id = fields.Many2one('prada.seccion', 'SECCIÓN', readonly = False, store = True, related = 'producto_id.seccion_id')
    silueta_id = fields.Many2one('prada.silueta', 'SILUETA', readonly = False, store = True, related = 'producto_id.silueta_id')
    #horma_id = fields.Many2one('prada.horma', 'Horma', readonly = False, store = True, related = 'producto_id.horma_id')
    horma = fields.Char('HORMA',related = 'producto_id.horma', readonly = False, store = True)
    material_id = fields.Many2one('prada.material', 'MATERIAL', readonly = False, store = True, related = 'producto_id.material_id')
    color_id = fields.Many2one('prada.color', 'COLOR', readonly = False, store = True)
    atributo1_id = fields.Many2one('prada.atributo1', 'ATRIBUTO 1', readonly = False, store = True, related = 'producto_id.atributo1_id')
    atributo2_id = fields.Many2one('prada.atributo2', 'ATRIBUTO 2', readonly = False, store = True, related = 'producto_id.atributo2_id')
    ocasion_id = fields.Many2one('prada.ocasion', 'OCASIÓN', readonly = False, store = True, related='producto_id.ocasion_id')
    no_juego = fields.Char('NO JUEGO', readonly = False, store = True, related = 'producto_id.no_juego')
    juego1 = fields.Char('JUEGO 1', readonly = False, store = True, related = 'producto_id.juego1')
    juego2 = fields.Char('JUEGO 2', readonly = False, store = True, related = 'producto_id.juego2')
    juego3 = fields.Char('JUEGO 3', readonly = False, store = True, related = 'producto_id.juego3')
    categoria_id = fields.Many2one('prada.categoria', 'CATEGORÍA', readonly = False, store = True, related = 'producto_id.categoria_id')
    tendencia_id = fields.Many2one('prada.tendencia', 'TENDENCIA', readonly = False, store = True, related = 'producto_id.tendencia_id')
    coleccion_id = fields.Many2one('prada.coleccion', 'COLECCIÓN', readonly = False, store = True, related = 'producto_id.coleccion_id')
    tienda_id = fields.Many2one('prada.tienda', 'TIENDA', readonly = False, store = True, related = 'producto_id.tienda_id')
    costo = fields.Float('COSTO', readonly = False, store = True)
    #costo = fields.Float('COSTO', readonly = False, store = True, groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    corridas_prepedido = fields.Float('CORRIDAS PREPEDIDO ANTICIPO CARRY')
    corrida = fields.Float('CORR')
    corrida_id = fields.Many2one('prada.corrida','CORRIDA', domain='[("temp","=", temp),("seccion_id","=",seccion_id),("departamento_id","=", departamento_id),("coleccion_id","=", coleccion_id)]')
    talla = fields.Float('35', readonly = True, store = True, related='corrida_id.talla')
    columna1 = fields.Float('36', readonly = True, store = True, related='corrida_id.columna1')
    columna2 = fields.Float('37', readonly = True, store = True, related='corrida_id.columna2')
    columna3 = fields.Float('38', readonly = True, store = True, related='corrida_id.columna3')
    columna4 = fields.Float('39', readonly = True, store = True, related='corrida_id.columna4')
    columna5 = fields.Float('40', readonly = True, store = True, related='corrida_id.columna5')
    columna6 = fields.Float('41', readonly = True, store = True, related='corrida_id.columna6')
    columna7 = fields.Float('42', readonly = True, store = True, related='corrida_id.columna7')
    columna8 = fields.Float('43', readonly = True, store = True, related='corrida_id.columna8')
    columna9 = fields.Float('44', readonly = True, store = True, related='corrida_id.columna9')
    columna10 = fields.Float('45', readonly = True, store = True, related='corrida_id.columna10')

    columna12 = fields.Float('46', readonly = True, store = True, related='corrida_id.columna12')
    columna13 = fields.Float('47', readonly = True, store = True, related='corrida_id.columna13')
    columna14 = fields.Float('48', readonly = True, store = True, related='corrida_id.columna14')
    columna15 = fields.Float('49', readonly = True, store = True, related='corrida_id.columna15')
    columna16 = fields.Float('50', readonly = True, store = True, related='corrida_id.columna16')
    columna17 = fields.Float('90', readonly = True, store = True, related='corrida_id.columna17')
    columna18 = fields.Float('100', readonly = True, store = True, related='corrida_id.columna18')
    columna19 = fields.Float('105', readonly = True, store = True, related='corrida_id.columna19')
    columna20 = fields.Float('110', readonly = True, store = True, related='corrida_id.columna20')
    columna21 = fields.Float('120', readonly = True, store = True, related='corrida_id.columna21')
    columna11 = fields.Float('UNI', readonly = True, store = True, related='corrida_id.columna11')
    columna22 = fields.Float('GD', readonly = True, store = True, related='corrida_id.columna22')
    columna23 = fields.Float('MD', readonly = True, store = True, related='corrida_id.columna23')

    totalu = fields.Float('TOTAL U', readonly = True, store = True, compute='_compute_columnas')
    total_eur = fields.Float('TOTAL EUR', readonly = True, store = True, compute = '_compute_valores')
    gastos = fields.Float('GASTOS')
    iva = fields.Float('IVA')

    total_usd = fields.Float('TOTAL $')
    pvp_calculado = fields.Float('PVP CALCULADO')
    pvp_redondeado = fields.Float('PVP REDONDEADO')
    pvp_comercial = fields.Float('PVP COMERCIAL')
    pvp_outlet = fields.Float('PVP OUTLET', readonly=False)
    comentarios_compras = fields.Html('COMENTARIOS COMPRAS')
    mes_entrega = fields.Char('MES DE ENTREGA')
    mes_recibo_tienda = fields.Char('MES RECIBIDO EN TIENDAS')
    apuntes_getoria_compra_es = fields.Html('APUNTES GESTORIA COMPRA EN ESPAÑA')
    revision_es_antes_vuelo = fields.Html('REVISIÓN FISICA EN ESPAÑA ANTES DEL VUELO')
    troquel_id = fields.Many2one('prada.troquel','TROQUEL')
    medidas = fields.Char('MEDIDAS')
    tipo_punta = fields.Char('TIPO DE PUNTA')
    tipo_fijacion = fields.Char('TIPO DE FIJACIÓN')
    comentarios_producto_compra_es = fields.Html('COMENTARIOS DE PRODUCTO EN COMPRA ESPAÑA')
    comentarios_p1_revision_mx = fields.Html('COMENTARIOS PRODUCTO 1RA REVISIÓN MEXICO')
    comentarios_p2_revision_mx = fields.Html('COMENTARIOS PRODUCTO 2DA REVISIÓN MEXICO')
    comentarios_producto_llegada_mx = fields.Html('COMENTARIOS PRODUCTO LLEGADA A MÉXICO PARA WEB')
    cuidados_producto = fields.Html('CUIDADOS DEL PRODUCTO')
    atributo_especial = fields.Html('ATRIBUTO ESPECIAL')
    estatus_muestra_web_id = fields.Many2one('prada.estado_web','ESTATUS DE LA MUESTRA WEB')
    estatus_muestra_marketing_id = fields.Many2one('prada.estado_marketing','ESTATUS MUESTRA MARKETING', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_producto,prada.prada_ecommerce,prada.prada_marketing')
    fecha_vuelo_muestras = fields.Date('FECHA VUELO MUESTRAS')
    estatus_muestra_importaciones = fields.Char('ESTATUS MUESTRA IMPORTACIONES')
    fecha_vuelo_produccion = fields.Date('FECHA VUELO PRODUCCIÓN')
    estatus_produccion_importacion = fields.Char('ESTATUS PRODUCCIÓN IMPORTACIONES')
    bullets = fields.Html('BULLETS', compute= '_compute_bullet')
    titulo = fields.Html('TITULO')
    descripcion = fields.Html('DESCRIPCIÓN')
    metatitulo = fields.Html('METATITULO')
    metadescripcion = fields.Html('METADESCRIPCIÓN')
    titulo_amazon = fields.Html('TITULO AMAZON')
    desripcion_amazon = fields.Html('DESCRIPCIÓN AMAZON')
    bullets_amazon = fields.Html('BULLETS AMAZON')
    #este campo solo es para prueba al pasar a produccion revisar si se hace o no
    #total_modelos = fields.Integer('TOTAL MODELOS',store=True, related='eco_id.total_modelos', group_operator='avg')
    total_modelos = fields.Integer('TOTAL MODELOS',store=True, default="1")
    #total_costo_promedio = fields.Float('TOTAL COSTO PROMEDIO',store=True, related='eco_id.total_costo_promedio', group_operator='avg')
    total_costo_promedio = fields.Float('TOTAL COSTO PROMEDIO',store=True, related='costo', group_operator='avg')
    total_corrida_promedio = fields.Float('TOTAL CORRIDA PROMEDIO',store=True, related='totalu', group_operator='avg')
    suma_unidades = fields.Integer('SUMA UNIDADES',store=True)
    #suma_unidades = fields.Many2one('prada.corrida',string='SUMA UNIDADES', related='corrida_id', store=True)
    url_imagen = fields.Char("URL imagen", compute='_compute_url_imagen')
    cambios_preconfirmacion_id = fields.Many2one('prada.cambios_preconfirmacion', 'CAMBIOS PRECONFIRMACIÓN')

    @api.onchange('codigo_prada', 'producto_id')
    def _onchange_codigo_prada(self):
        if self.codigo_prada and self.producto_id:
            self.producto_id.write({'default_code': self.codigo_prada})
            domain = [('default_code', '=', self.codigo_prada)]
            if self.env['product.template'].search_count(domain, limit=2) >= 2:
                self.codigo_prada = False
                return {'warning': {
                    'title': _("Note:"),
                    'message': _("Referencia interna ya existe."),
                }}


    @api.onchange('producto_id', 'modelo', 'color_id')
    def _onchange_producto_id(self):
        if not (self.producto_id and self.modelo and self.color_id):
            return

        eco_id = self.eco_id.id or self.eco_id._origin.id if self.eco_id else False

        _logger.warning("Onchange validando duplicado con:")
        _logger.warning(f"producto_id={self.producto_id.id}, codigo_prada={self.codigo_prada}, modelo={self.modelo}, color_id={self.color_id.id}, eco_id={eco_id}")

        domain = [
            ('producto_id', '=', self.producto_id.id),
            ('modelo', '=', self.modelo),
            ('color_id', '=', self.color_id.id),
            ('eco_id', '=', eco_id)
        ]

        if self.id:
            domain.append(('id', '!=', self.id))

        duplicates = self.env['prada.pim.line'].search_count(domain)

        if duplicates:
            raise ValidationError(_('Ya existe un producto con la misma combinación de producto, código, modelo, color y ECO.'))



    # @api.onchange('producto_id','codigo_prada','modelo','color_id')
    # def _onchange_producto_id(self):
    #     if not self.producto_id:
    #         return

    #     eco_id = self.eco_id._origin.id

    #     if self.producto_id.color_id:
    #         self.color_id = self.producto_id.color_id.id
    #     if self.producto_id and self.codigo_prada:
    #         self.producto_id.default_code = self.codigo_prada

    #     if self.color_id and self.producto_id and self.modelo:
    #         dominio = [('eco_id', '=', eco_id),('producto_id','=',self.producto_id.id),('modelo','=', self.modelo),('color_id','=', self.color_id.id)]
    #         logging.warning("lines")
    #         logging.warning(self.env['prada.pim.line'].search(dominio))
    #         if self.env['prada.pim.line'].search_count(dominio):
    #             raise ValidationError(_('Producto repetido test'))

    @api.depends('producto_id','silueta_id', 'color_id', 'atributo_especial', 'ocasion_id', 'atributo1_id', 'medidas')
    def _compute_bullet(self):
        for linea in self:
            silueta = linea.silueta_id.name if linea.silueta_id else ''
            color = linea.color_id.name if linea.color_id else ''
            atributo_especial = linea.atributo_especial if linea.atributo_especial else ''
            ocasion = linea.ocasion_id.name if linea.ocasion_id else ''
            atributo1 = linea.atributo1_id.name if linea.atributo1_id else ''
            medidas = linea.medidas if linea.medidas else ''
            bullet = 'SILUETA: '+silueta + ' COLOR: '+color+ ' ATRIBUTO ESPECIAL: ' +atributo_especial+ ' OCASION: ' +ocasion+ ' ATRIBUTO1: ' +atributo1+ ' MEDIDAS: ' + medidas
            linea.bullets = bullet


    @api.depends('seccion_id','corrida_id','coleccion_id')
    def _compute_columnas(self):
        for linea in self:
            total_eur = 0
            corrida_id = linea.corrida_id
            if corrida_id:
                totalu = corrida_id.talla + corrida_id.columna1 + corrida_id.columna2 + corrida_id.columna3 + corrida_id.columna4 + corrida_id.columna5 + corrida_id.columna6 + corrida_id.columna7 + corrida_id.columna8 + corrida_id.columna9 + corrida_id.columna10 + corrida_id.columna11
                linea.totalu = totalu
                linea.suma_unidades = corrida_id.total


    @api.depends('corrida_id')
    def _compute_valores(self):
        for linea in self:
            total_eur = linea.corrida_id.total * linea.costo
            gastos = total_eur * (linea.eco_id.gastos / 100)
            iva = (total_eur + gastos) * (linea.eco_id.iva / 100)
            total_usd = (total_eur + gastos + iva) * linea.eco_id.tipo_cambio
            pvp_calculado = ((total_usd * linea.eco_id.marcaje) / linea.totalu)  if linea.totalu > 0 else 0
            pvp_comercial = int(pvp_calculado/100) * 100 - 10 + 100
            linea.total_eur = total_eur
            linea.gastos = gastos
            linea.iva = iva
            linea.total_usd =  total_usd
            linea.pvp_calculado = pvp_calculado
            #linea.pvp_comercial = pvp_comercial
            linea.pvp_redondeado = pvp_comercial

    @api.onchange('producto_id','seccion_id', 'departamento_id', 'coleccion_id')
    def onchannge_producto_id(self):
        for linea in self:
            linea.costo = linea.producto_id.standard_price
            linea.codigo_prada = linea.producto_id.default_code
            linea.color_id = linea.producto_id.color_id.id if linea.producto_id.color_id else False
            linea.marca_id = linea.producto_id.marca_id.id if linea.producto_id.marca_id else False

    @api.onchange('temp')
    def onchannge_campos_corrida(self):
        for linea in self:
            linea.corrida_id = False

    def action_duplicar_pim_line(self):
        self.ensure_one()  # solo uno a la vez
        nuevo_producto = self.producto_id.copy(default={
            'name': self.producto_id.name + ' duplicado',
            'default_code': '',
            'color_id': False,
        })
        nuevo_pim_linea = self.copy(default={
            'producto_id': nuevo_producto.id,
            'color_id': False,
            'codigo_prada': '',
        })

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'prada.pim.line',
            'view_mode': 'form',
            'res_id': nuevo_pim_linea.id,
            'target': 'current',
        }

    def _compute_url_imagen(self):
        for linea in self:
            if linea.prada_image:
                linea.url_imagen = f'{request.httprequest.host_url}/web/image/{linea._name}/{linea.id}/prada_image'
            else:
                linea.url_imagen = False
