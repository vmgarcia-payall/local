# -*- coding: utf-8 -*-
from odoo import models, fields, api


class RatesTypes( models.Model):
    _name = 'rates.type'
    _description = 'Modulo para tipos de tarifas'

    name = fields.Char(string='Tarifa')
    description = fields.Text(string='Descripcion')
    rates_ids = fields.One2many(string='Tarifas', comodel_name='rates.move', inverse_name='rate_type_id')