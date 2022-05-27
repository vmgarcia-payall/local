# -*- coding: utf-8 -*-

from numpy import require
from odoo import models, fields, api

class PartnerCodeInherit( models.Model):
    _inherit = 'res.partner'

    country_id = fields.Many2one(comodel_name='res.country', string='País', default=lambda self: self._get_default_country())
    state_id = fields.Many2one(comodel_name='res.country.state', string="Estado", required=True ,default=lambda self: self._get_estado())
    municipio_id = fields.Many2one(comodel_name='res.state.municipio', string="Municipio", default=lambda self: self._get_municipio())
    parroquia_id = fields.Many2one(comodel_name='res.municipio.parroquia', string="Parroquia", default=lambda self: self._get_parroquia())
    urbanizacion_id = fields.Many2one(comodel_name='res.parroquia.urbanizacion', string="Urbanización", default=lambda self: self._get_urbanizacion())
    partner_code = fields.Char(string = 'Código de Interlocutor', default=lambda self: self._get_next_sequence_number() )
    titular = fields.Char(string = 'Titular de Pago')
    interlocutor_id = fields.Char(string ="ID de SAP")
    dir_fisc = fields.Text(string = 'Direccion fiscal')
    
    @api.model
    def create(self, vals):
        vals['partner_code'] = self.env['ir.sequence'].next_by_code('partner_code_seq')
        result = super( PartnerCodeInherit, self).create(vals)
        return result 

    @api.model
    def _get_next_sequence_number(self):
        for record in self:
            sequence = self.env['ir.sequence'].search([('code','=','partner_code_seq')])
            next= sequence.get_next_char(sequence.number_next_actual)
            return next
        
    @api.model
    def _get_default_country(self):
        country = self.env['res.country'].search([('code','=','VE')])
        return country

    @api.onchange('country_id')
    def _get_estado(self):
        for record in self:
            return {'domain': {'state_id': [('country_id.id', '=', record.country_id.id)]}}

    @api.onchange('state_id')
    def _get_municipio(self):
        for record in self:
            return { 'domain': { 'municipio_id': [('state_id.id','=',record.state_id.id)]}}

    @api.onchange('municipio_id')
    def _get_parroquia(self):
        for record in self:
            return { 'domain': { 'parroquia_id': [('municipio_id.id','=',record.municipio_id.id)]}}

    @api.onchange('parroquia_id')
    def _get_urbanizacion(self):
        for record in self:
            return {'domain': {'urbanizacion_id': [('parroquia_id.id', '=', record.parroquia_id.id)]}}

