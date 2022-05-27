# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResParroquiaInherit(models.Model):

    _name = "res.municipio.parroquia"
    _description = "Descripción del modelo Parroquia"

    name = fields.Char(string='Nombre')
    code = fields.Char(string='Código')
    municipio_id = fields.Many2one("res.state.municipio", "Municipio", required=True)
    Desc_Corta_Parr = fields.Char(string='Descripcion Corta')
    Desc_Larga_Parr = fields.Char(string='Descripcion Larga')
    Nivel_Parr = fields.Char(string='Nivel')


    urbanizaciones_ids = fields.One2many("res.parroquia.urbanizacion", "parroquia_id", "Urbanizaciones")