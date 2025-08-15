# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, AccessError
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

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')
    marca_id = fields.Many2one('prada.marca','Marca')

class PradaTemp(models.Model):
    _name = 'prada.temp'
    
    name = fields.Char('Nombre')
    clave = fields.Char('Clave')

class PradaMarca(models.Model):
    _name = 'prada.marca'
    _rec_name = 'name'
    
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

class PradaDepartamento(models.Model):
    _name = 'prada.departamento'
    _rec_name = 'clave'
    
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

class PradaSeccion(models.Model):
    _name = 'prada.seccion'
    _rec_name = 'clave'
    
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

class PradaSilueta(models.Model):
    _name = 'prada.silueta'
    _rec_name = 'clave'

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

class PradaHorma(models.Model):
    _name = 'prada.horma'

    name = fields.Char('Nombre')

class PradaMaterial(models.Model):
    _name = 'prada.material'
    _rec_name = 'clave'

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

class PradaColor(models.Model):
    _name = 'prada.color'
    _rec_name = 'clave'

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

class PradaAtributo1(models.Model):
    _name = 'prada.atributo1'
    _rec_name = 'clave'

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

class PradaAtributo2(models.Model):
    _name = 'prada.atributo2'
    _rec_name = 'clave'

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

class PradaOcasion(models.Model):
    _name = 'prada.ocasion'
    _rec_name = 'clave'

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

class PradaCategoria(models.Model):
    _name = 'prada.categoria'
    _rec_name = 'clave'

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


class PradaTendencia(models.Model):
    _name = 'prada.tendencia'
    _rec_name = 'clave'

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

class PradaColeccion(models.Model):
    _name = 'prada.coleccion'
    _rec_name = 'clave'

    name = fields.Char('Nombre')
    clave = fields.Char('Clave')

class PradaTienda(models.Model):
    _name = 'prada.tienda'
    _rec_name = 'clave'

    clave = fields.Char('CLAVE')
    name = fields.Char('NOMBRE')

class PradaTroquel(models.Model):
    _name = 'prada.troquel'

    name = fields.Char('Nombre')

class PradaEstadoWeb(models.Model):
    _name = 'prada.estado_web'

    name = fields.Char('Nombre')

class PradaEstadoMarketing(models.Model):
    _name = 'prada.estado_marketing'

    name = fields.Char('Nombre')

class PradaCorrida(models.Model):
    _name = 'prada.corrida'

    name = fields.Char('CORRIDA', required=True)

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
    columna11 = fields.Float('UNI')
    totalu = fields.Float('TotalU', compute='_compute_total')
    total = fields.Float('Total',store = True ,compute='_compute_total')

    @api.depends('talla','columna1','columna2','columna3','columna4','columna5','columna6','columna7','columna8','columna9','columna10','columna11')
    def _compute_total(self):
        total = 0
        for corrida in self:
            total += corrida.talla + corrida.columna1+corrida.columna2+corrida.columna3+corrida.columna4+corrida.columna5+corrida.columna6+corrida.columna7+corrida.columna8+corrida.columna9+corrida.columna10+corrida.columna11
            corrida.total = total
            corrida.totalu = total


    @api.onchange('seccion_id','coleccion_id','departamento_id','name')
    def _onchange_apartados(self):
        logging.warning("_onchange_apartados")
        logging.warning("antes de if ")
        logging.warning(self.seccion_id)
        logging.warning(self.coleccion_id)
        logging.warning(self.departamento_id)
        logging.warning(self._origin)
        logging.warning(self._origin.id)
        if self.seccion_id and self.coleccion_id and self.departamento_id and self.name:
            corrida_id = self._origin
            dominio = [('id', '!=', corrida_id.id),('seccion_id','=',self.seccion_id.id), ('coleccion_id','=',self.coleccion_id.id),('departamento_id','=', self.departamento_id.id), ('name','=', self.name)]
            logging.warning('dominio')
            logging.warning(dominio)
            logging.warning(self.env['prada.corrida'].search_count(dominio))
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
    codigo_prada = fields.Char('CÓDIGO PRADA', readonly = False, store = True, related = 'producto_id.default_code')
    modelo = fields.Char('MODELO', readonly = False, store = False, related = 'producto_id.modelo')
    departamento_id = fields.Many2one('prada.departamento', 'DEPARTAMENTO', readonly = False, store = True, related = 'producto_id.departamento_id')
    seccion_id = fields.Many2one('prada.seccion', 'SECCIÓN', readonly = False, store = True, related = 'producto_id.seccion_id')
    silueta_id = fields.Many2one('prada.silueta', 'SILUETA', readonly = False, store = True, related = 'producto_id.silueta_id')
    #horma_id = fields.Many2one('prada.horma', 'Horma', readonly = False, store = True, related = 'producto_id.horma_id')
    horma = fields.Char('HORMA',related = 'producto_id.horma', readonly = False, store = True)
    material_id = fields.Many2one('prada.material', 'MATERIAL', readonly = False, store = True, related = 'producto_id.material_id')
    color_id = fields.Many2one('prada.color', 'COLOR', readonly = False, store = True, related = 'producto_id.color_id')
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
    corrida = fields.Float('CORRIDA')
    talla = fields.Float('35', readonly = True, store = True, compute='_compute_columnas')
    columna1 = fields.Float('36', readonly = True, store = True, compute='_compute_columnas')
    columna2 = fields.Float('37', readonly = True, store = True, compute='_compute_columnas')
    columna3 = fields.Float('38', readonly = True, store = True, compute='_compute_columnas')
    columna4 = fields.Float('39', readonly = True, store = True, compute='_compute_columnas')
    columna5 = fields.Float('40', readonly = True, store = True, compute='_compute_columnas')
    columna6 = fields.Float('41', readonly = True, store = True, compute='_compute_columnas')
    columna7 = fields.Float('42', readonly = True, store = True, compute='_compute_columnas')
    columna8 = fields.Float('43', readonly = True, store = True, compute='_compute_columnas')
    columna9 = fields.Float('44', readonly = True, store = True, compute='_compute_columnas')
    columna10 = fields.Float('45', readonly = True, store = True, compute='_compute_columnas')
    columna11 = fields.Float('UNI', readonly = True, store = True, compute='_compute_columnas')
    totalu = fields.Float('TOTAL U', readonly = True, store = True, compute='_compute_columnas')
    total_eur = fields.Float('TOTAL EUR', readonly = True, store = True, compute = '_compute_valores', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    gastos = fields.Float('GASTOS', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    iva = fields.Float('IVA', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    
    total_usd = fields.Float('TOTAL $', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    pvp_calculado = fields.Float('PVP CALCULADO', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    pvp_redondeado = fields.Float('PVP REDONDEADO', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    pvp_comercial = fields.Float('PVP COMERCIAL', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    pvp_outlet = fields.Float('PVP OUTLET', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion')
    comentarios_compras = fields.Html('COMENTARIOS COMPRAS')
    mes_entrega = fields.Char('MES DE ENTREGA')
    mes_recibo_tienda = fields.Char('MES RECIBIDO EN TIENDAS')
    apuntes_getoria_compra_es = fields.Html('APUNTES GESTORIA COMPRA EN ESPAÑA', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion,prada_compras_producto')
    revision_es_antes_vuelo = fields.Html('REVISIÓN FISICA EN ESPAÑA ANTES DEL VUELO', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion,prada_compras_producto')
    troquel_id = fields.Many2one('prada.troquel','TROQUEL')
    medidas = fields.Char('MEDIDAS')
    tipo_punta = fields.Char('TIPO DE PUNTA')
    tipo_fijacion = fields.Char('TIPO DE FIJACIÓN')
    comentarios_producto_compra_es = fields.Html('COMENTARIOS DE PRODUCTO EN COMPRA ESPAÑA', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion,prada_compras_producto')
    comentarios_p1_revision_mx = fields.Html('COMENTARIOS PRODUCTO 1RA REVISIÓN MEXICO',groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion,prada_compras_producto')
    comentarios_p2_revision_mx = fields.Html('COMENTARIOS PRODUCTO 2DA REVISIÓN MEXICO',groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_planeacion,prada_compras_producto')
    comentarios_producto_llegada_mx = fields.Html('COMENTARIOS PRODUCTO LLEGADA A MÉXICO PARA WEB', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_producto,prada.prada_ecommerce,prada.prada_marketing')
    cuidados_producto = fields.Html('CUIDADOS DEL PRODUCTO', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_producto,prada.prada_ecommerce,prada.prada_marketing')
    atributo_especial = fields.Html('ATRIBUTO ESPECIAL', groups='prada.prada_dg,prada.prada_gestoria,prada.prada_compras,prada.prada_compras_importaciones,prada.prada_compras_producto,prada.prada_ecommerce,prada.prada_marketing')
    estatus_muestra_web_id = fields.Many2one('prada.estado_web','ESTATUS DE LA MUESTRA WEB')
    estatus_muestra_marketing_id = fields.Many2one('prada.estado_marketing','ESTATUS MUESTRA MARKETING', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_producto,prada.prada_ecommerce,prada.prada_marketing')
    fecha_vuelo_muestras = fields.Date('FECHA VUELO MUESTRAS')
    estatus_muestra_importaciones = fields.Char('ESTATUS MUESTRA IMPORTACIONES')
    fecha_vuelo_produccion = fields.Date('FECHA VUELO PRODUCCIÓN')
    estatus_produccion_importacion = fields.Char('ESTATUS PRODUCCIÓN IMPORTACIONES')
    bullets = fields.Html('BULLETS', compute= '_compute_bullet', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_producto,prada.prada_ecommerce,prada.prada_marketing')
    titulo = fields.Html('TITULO', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_producto,prada.prada_ecommerce,prada.prada_marketing')
    descripcion = fields.Html('DESCRIPCIÓN', groups='prada.prada_dg,prada.prada_compras,prada.prada_compras_producto,prada.prada_ecommerce,prada.prada_marketing')
    metatitulo = fields.Html('METATITULO', groups='prada.prada_dg,prada.prada_ecommerce,prada.prada_marketing')
    metadescripcion = fields.Html('METADESCRIPCIÓN', groups='prada.prada_dg,prada.prada_ecommerce,prada.prada_marketing')
    titulo_amazon = fields.Html('TITULO AMAZON', groups='prada.prada_dg,prada.prada_ecommerce,prada.prada_marketing')
    desripcion_amazon = fields.Html('DESCRIPCIÓN AMAZON', groups='prada.prada_dg,prada.prada_ecommerce,prada.prada_marketing')
    bullets_amazon = fields.Html('BULLETS AMAZON', groups='prada.prada_dg,prada.prada_ecommerce,prada.prada_marketing')


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
    
    @api.onchange('producto_id')
    def _onchange_producto_id(self):
        if not self.producto_id:
            return

        logging.warning(self.eco_id._origin.id)
        eco_id = self.eco_id._origin.id
        dominio = [('eco_id', '=', eco_id),('producto_id','=',self.producto_id.id)]
        logging.warning('onchange producto')
        logging.warning(self.env['prada.pim.line'].search_count(dominio))
        if self.env['prada.pim.line'].search_count(dominio):
            raise ValidationError(_('Producto repetido'))

    
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
            
    
    @api.depends('seccion_id','corrida','coleccion_id')
    def _compute_columnas(self):
        for linea in self:
            total_eur = 0
            if linea.seccion_id and linea.corrida > 0:
                corrida_id = self.env['prada.corrida'].search([('seccion_id','=',linea.seccion_id.id),('departamento_id','=',linea.departamento_id.id),('coleccion_id','=',linea.coleccion_id.id),('name','=',str(int(linea.corrida)))])
                if corrida_id:
                    totalu = corrida_id.talla + corrida_id.columna1 + corrida_id.columna2 + corrida_id.columna3 + corrida_id.columna4 + corrida_id.columna5 + corrida_id.columna6 + corrida_id.columna7 + corrida_id.columna8 + corrida_id.columna9 + corrida_id.columna10 + corrida_id.columna11
                    linea.talla = corrida_id.talla
                    linea.columna1 = corrida_id.columna1
                    linea.columna2 = corrida_id.columna2
                    linea.columna3 = corrida_id.columna3
                    linea.columna4 = corrida_id.columna4
                    linea.columna5 = corrida_id.columna5
                    linea.columna6 = corrida_id.columna6
                    linea.columna7 = corrida_id.columna7
                    linea.columna8 = corrida_id.columna8
                    linea.columna9 = corrida_id.columna9
                    linea.columna10 = corrida_id.columna10
                    linea.columna11 = corrida_id.columna11
                    linea.totalu = totalu
            #         total_eur = corrida.total * linea.costo
            # linea.total_eur = total_eur

    @api.depends('corrida')
    def _compute_valores(self):
        for linea in self:
            total_eur = linea.corrida * linea.costo
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
            linea.pvp_comercial = pvp_comercial
            
    @api.onchange('producto_id')
    def onchannge_producto_id(self):
        for linea in self:
            linea.costo = linea.producto_id.standard_price

    def create(self, vals):
        _logger.warning("Create called with vals: %s", vals)
        productos_repetidos = {}
        if len(vals) > 1:
            for v in vals:
                producto = v['producto_id']
                if producto not in productos_repetidos:
                    productos_repetidos[producto] = 0
                productos_repetidos[producto] += 1

            if len(productos_repetidos) > 0:
                for p in productos_repetidos:
                    if productos_repetidos[p] > 1:
                        raise ValidationError(_('Producto repetido'))
                        
    
        def check_group(fields, groups, error="You do not have permission to edit this field."):
            if any(field in vals for field in fields):
                if not all(self.env.user.has_group(group) for group in groups):
                    raise AccessError(error)
    
        check_group(
            ['comentarios_compras', 'mes_entrega', 'mes_recibo_tienda'],
            ['prada.prada_compras']
        )
    
        check_group(
            ['corridas_prepedido', 'corrida'],
            ['prada.prada_compras', 'prada.prada_compras_planeacion']
        )
    
        check_group(
            [
                'temp', 'proveedor_id', 'marca_id', 'modelo', 'departamento_id', 'seccion_id', 'silueta_id', 'horma_id',
                'material_id', 'color_id', 'atributo1_id', 'atributo2_id', 'ocasion_id', 'no_juego', 'juego1',
                'juego2', 'juego3', 'categoria_id', 'tendencia_id', 'coleccion_id', 'tienda_id', 'troquel_id',
                'medidas', 'tipo_punta', 'tipo_fijacion', 'comentarios_producto_compra_es',
                'comentarios_p1_revision_mx', 'comentarios_p2_revision_mx', 'comentarios_producto_llegada_mx',
                'cuidados_producto', 'atributo_especial', 'estatus_muestra_marketing_id'
            ],
            ['prada.prada_compras', 'prada.prada_compras_producto']
        )
    
        check_group(
            ['apuntes_getoria_compra_es', 'revision_es_antes_vuelo'],
            ['prada.prada_gestoria']
        )
    
        check_group(
            ['costo'],
            ['prada.prada_gestoria', 'prada.prada_compras']
        )
    
        check_group(
            ['fecha_vuelo_muestras', 'estatus_muestra_importaciones', 'fecha_vuelo_produccion', 'estatus_produccion_importacion'],
            ['prada.prada_compras_importaciones', 'prada.prada_compras']
        )
    
        check_group(
            ['titulo', 'descripcion', 'metatitulo', 'metadescripcion', 'titulo_amazon', 'desripcion_amazon', 'bullets_amazon'],
            ['prada.prada_marketing']
        )
    
        check_group(
            ['codigo_prada'],
            ['prada.prada_compras_planeacion']
        )
    
        check_group(
            ['pvp_comercial', 'pvp_outlet'],
            ['prada.prada_compras_planeacion', 'prada.prada_compras']
        )
    
        check_group(
            ['estatus_muestra_web_id'],
            ['prada.prada_compras_producto', 'prada.prada_compras', 'prada.prada_ecommerce']
        )
    
        if 'prada_image' in vals:
            if not all(self.env.user.has_group(g) for g in ['prada.prada_compras_producto', 'prada.prada_marketing', 'prada.prada_ecommerce']):
                raise UserError("You do not have permission to edit this field.")
    
        return super().create(vals)
    
    def write(self, vals):
        logging.warning("vals")
        logging.warning(vals)
        if ('comentarios_compras' or 'mes_entrega' or 'mes_recibo_tienda') in vals:
            if not self.env.user.has_group('prada.prada_compras'):
                raise AccessError("You do not have permission to edit this field.")

        if ('corridas_prepedido' or 'corrida') in vals:
            if not self.env.user.has_group('prada.prada_compras') or not self.env.user.has_group('prada.prada_compras_planeacion'):
                raise AccessError("You do not have permission to edit this field.")
                
        if ('comentarios_compras' or 'mes_entrega' or 'mes_recibo_tienda') in vals:
            if not self.env.user.has_group('prada.prada_compras'):
                raise AccessError("You do not have permission to edit this field.")
        
        condicion_compras_producto = ('temp' or 'proveedor_id' or 'marca_id' or 'modelo' or 'departamento_id' or 'seccion_id' or'silueta_id' or 'horma_id' or 'material_id' or 'color_id' or 'atributo1_id' or 'atributo2_id' or 'ocasion_id' or 'no_juego' or 'juego1' or 'juego2' or 'juego3' or 'categoria_id' or 'tendencia_id' or 'coleccion_id' or 'tienda_id' or 'troquel_id' or 'medidas' or 'tipo_punta' or 'tipo_fijacion' or 'comentarios_producto_compra_es' or 'comentarios_p1_revision_mx' or 'comentarios_p2_revision_mx' or 'comentarios_producto_llegada_mx' or 'cuidados_producto' or 'atributo_especial' or 'estatus_muestra_marketing_id')

        if condicion_compras_producto in vals:
            if not self.env.user.has_group('prada.prada_compras') or not self.env.user.has_group('prada.prada_compras_producto'):
                raise AccessError("You do not have permission to edit this field.")

        if ('apuntes_getoria_compra_es' or 'revision_es_antes_vuelo') in vals:
            if not self.env.user.has_group('prada.prada_gestoria'):
                raise AccessError("You do not have permission to edit this field.")

        if 'costo' in vals:
            if not self.env.user.has_group('prada.prada_gestoria') or not self.env.user.has_group('prada.prada_compras'):
                raise AccessError("You do not have permission to edit this field.")
                
        if ('fecha_vuelo_muestras' or 'estatus_muestra_importaciones' or 'fecha_vuelo_produccion' or 'estatus_produccion_importacion') in vals:
            if not self.env.user.has_group('prada.prada_compras_importaciones') or not self.env.user.has_group('prada.prada_compras'):
                raise AccessError("You do not have permission to edit this field.")

        if ('titulo' or 'descripcion' or 'metatitulo' or 'metadescripcion' or 'titulo_amazon' or 'desripcion_amazon' or 'bullets_amazon') in vals:
            if not self.env.user.has_group('prada.prada_marketing'):
                raise AccessError("You do not have permission to edit this field.")

        if ('codigo_prada') in vals:
            if not self.env.user.has_group('prada.prada_compras_planeacion'):
                raise AccessError("You do not have permission to edit this field.")

        if ('pvp_comercial' or 'pvp_outlet') in vals:
            if not self.env.user.has_group('prada.prada_compras_planeacion') or not self.env.user.has_group('prada.prada_compras'):
                raise AccessError("You do not have permission to edit this field.")
                
        if ('estatus_muestra_web_id') in vals:
            if not self.env.user.has_group('prada.prada_compras_producto') or not self.env.user.has_group('prada.prada_compras') or not self.env.user.has_group('prada.prada_ecommerce'):
                raise AccessError("You do not have permission to edit this field.")
                
        if ('prada_image') in vals:
            if not self.env.user.has_group('prada.prada_compras_producto') or not self.env.user.has_group('prada.prada_marketing') or not self.env.user.has_group('prada.prada_ecommerce'):
                raise UserError("You do not have permission to edit this field.")
        return super().write(vals)
