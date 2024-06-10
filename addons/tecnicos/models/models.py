# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tecnicos(models.Model):
    _name = 'tecnicos.tecnicos'
    _description = 'tecnicos.tecnicos'

    nombre = fields.Char('Nombre')
    apellido = fields.Char(string='Apellido')
    celular = fields.Char(string='Celular')
    email = fields.Char(string='Correo Electrónico',required=True)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

