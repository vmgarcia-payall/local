# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResMunicipioInherit(models.Model):

    _name = "res.state.municipio"
    _description = "Descripción del modelo Municipio"

    name = fields.Char(string='Nombre Municipio')
    code = fields.Char(string='Código Municipio')
    state_id = fields.Many2one("res.country.state", "Estado", required=True)
    Desc_Corta_Mun = fields.Char(string='Descripcion Corta Municipio')
    Desc_Larga_Mun = fields.Char(string='Descripcion Larga Municipio')
    Nivel_Mun = fields.Char(string='Nivel Municipio')
    #partner_ids = fields.One2many("res.partner", "municipio_id", "Partner")

    parroquias_ids = fields.One2many("res.municipio.parroquia", "municipio_id", "Parroquias")