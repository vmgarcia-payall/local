# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUrbanizacionInherit(models.Model):

    _name = "res.parroquia.urbanizacion"
    _description = "Descripción del modelo Urbanización"

    name = fields.Char(string='Nombre')
    code = fields.Char(string='Código')
    parroquia_id = fields.Many2one("res.municipio.parroquia", "Parroquias")
    Desc_Corta_Urb = fields.Char(string='Descripcion Corta')
    Desc_Larga_Urb = fields.Char(string='Descripcion Larga')
    Cod_Postal = fields.Char(string='Codigo Postal')
    Nivel_Urb = fields.Char(string='Nivel')