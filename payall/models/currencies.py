# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomCurrencies( models.Model):
    _name = 'custom.currencies'
    _description = 'Custom VE currencies module'

    petro = fields.Float(string="Petros")
    usd = fields.Float(string="Dolares")
    bolo = fields.Float(string="Bolivares")
    fecha = fields.Datetime(string="Fecha")

    @api.onchange('petro')
    def _update_bolos(self):
        query = self.env['res.partner'].search([('name','=','SOCOPO')])
        print(query)