from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _describe = "Hospital Patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', required=True, default='male')
    note = fields.Text(string='Description')
