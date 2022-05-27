# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResCountryInherit( models.Model):
    _inherit = 'res.country.state'
    

    short_code = fields.Char(string = 'Codigo corto')
    name = fields.Char(string='Nombre')
    code = fields.Char(string='Codigo')
    Desc_Corta_EF = fields.Char(string='Descripcion Corta')
    Desc_Larga_EF = fields.Char(string='Descripcion Larga')
    Nivel_EF = fields.Char(string='Nivel')

    municipios_ids = fields.One2many("res.state.municipio", "state_id", "Municipios")

