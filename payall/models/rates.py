# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Rates( models.Model):
    _name = 'rates.move'
    _description = 'Modulo para tarifas'

    rate_type_id = fields.Many2one(string='Tipo de tarifa', comodel_name='rates.type')

    name = fields.Char(string='Tarifa')
    description = fields.Text(string='Descripcion')
    vigente = fields.Boolean(string='Vigente')
    fecha = fields.Date(string='Fecha')
    est_pol = fields.Char(string='Estructura Politica')