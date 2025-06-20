# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging


class PradaTemp(models.Model):
    _name = 'prada.temp'

    name = fields.Char('name')

class PradaMarca(models.Model):
    _name = 'prada.Marca'

    name = fields.Char('name')

class PradaDepartamento(models.Model):
    _name = 'prada.departamento'

    name = fields.Char('name')


class PradaSeccion(models.Model):
    _name = 'prada.seccion'

    name = fields.Char('name')

class PradaSilueta(models.Model):
    _name = 'prada.silueta'

    name = fields.Char('name')

class PradaHorma(models.Model):
    _name = 'prada.horma'

    name = fields.Char('name')

class PradaMaterial(models.Model):
    _name = 'prada.material'

    name = fields.Char('name')

class PradaColor(models.Model):
    _name = 'prada.color'

    name = fields.Char('name')

class PradaAtributo1(models.Model):
    _name = 'prada.atributo1'

    name = fields.Char('name')

class PradaAtributo2(models.Model):
    _name = 'prada.atributo2'

    name = fields.Char('name')

class PradaOcasion(models.Model):
    _name = 'prada.ocasion'

    name = fields.Char('name')

class PradaCategoria(models.Model):
    _name = 'prada.categoria'

    name = fields.Char('name')


class PradaTendencia(models.Model):
    _name = 'prada.tendencia'

    name = fields.Char('name')

class PradaColeccion(models.Model):
    _name = 'prada.coleccion'

    name = fields.Char('name')

class PradaTienda(models.Model):
    _name = 'prada.Tienda'

    name = fields.Char('name')

class PradaPimLine(models.Model):
    _name = 'prada.pim.line'
    _description = 'Pim line for plm'

    eco_id = fields.Many2one('mrp.eco', 'Mrp eco')
    temp = fields.Many2one('prada.temp', 'Temporada del artículo')
    proveedor_id = fields.Many2one('res.partner')
    marca = fields.Many2one('prada.marca', 'Marca')
    codigo_prada = fields.Char('Código prada')
    modelo = fields.Char('Modelo')
    departamento_id = fields.Many2one('prada.departamento', 'Departamento')
    seccion_id = fields.Many2one('prada.seccion', 'Sección')
    silueta_id = fields.Many2one('prada.silueta', 'Silueta')
    horma_id = fields.Many2one('prada.horma', 'Horma')
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
    columna1 = fields.Integer('Columna 1')
    columna2 = fields.Integer('Columna 2')
    columna3 = fields.Integer('Columna 3')
    columna4 = fields.Integer('Columna 4')
    columna5 = fields.Integer('Columna 5')
    columna6 = fields.Integer('Columna 6')
    columna7 = fields.Integer('Columna 7')
    columna8 = fields.Integer('Columna 8')
    columna9 = fields.Integer('Columna 9')
    columna10 = fields.Integer('Columna 10')
    columna11 = fields.Integer('Columna 11')
    totalu = fields.Float('Total U')
    total_eur = fields.Float('Total EUR')
    gastos = fields.Float('Gastos')
    iva = fields.Float('IVA')
