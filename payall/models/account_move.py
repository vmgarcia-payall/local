# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import datetime

class AccountMove( models.Model):
    _inherit = 'account.move'
    
    state_id = fields.Char(string='Estado', store=True)
    partner_id = fields.Many2one(required=True)
    
    #------------------- Relacion con los servicios ------------------
    No_Contable = fields.Char( string = 'No Doc Contable',readonly=True, index=True)
    No_Registro = fields.Char( string = 'No Registro',readonly=True, index=True)
    
    #------------------- CUENTA CONTRATO ------------------
   
    tipo_tarifa = fields.Char(string = 'tipo de tarifa')
    fecha_creacion = fields.Date(string = 'Fecha de creación')
    #------------------- CUENTA CONTRATO ------------------
    
    inicio_periodo = fields.Date(string='Inicio período', default=fields.Date.today, store=True)
    fin_periodo = fields.Date(string='Fin período', default=fields.Date.today, store=True)

    precio_consumo = fields.Integer( string = "precio")
    saldo_vencido = fields.Float( string="Saldo Vencido", default = 0.0)
    
    
    @api.onchange('inicio_periodo')
    def expiration_date(self):
        for record in self:
            record.dias_lectura = record.inicio_periodo.day
    
    @api.onchange('partner_id')
    def _compute_short_code(self):
        for record in self:
            record.state_id = record.partner_id.state_id.short_code
    
    @api.depends('move_type')
    def _get_move_type(self):
        for record in self:
            return record.move_type
        
    @api.model
    def create(self, vals):
        vals['No_Contable'] = self.env['ir.sequence'].next_by_code('Seq_No_Contable')
        vals['No_Registro'] = self.env['ir.sequence'].next_by_code('Seq_No_Registro')
        vals['name'] = 'SERIECC' + vals['state_id'] + self.env['ir.sequence'].next_by_code('seq_fact')
        result = super(AccountMove, self).create(vals)
        return result