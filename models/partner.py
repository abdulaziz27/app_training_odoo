from odoo import models, fields, api
 
class Partner(models.Model):
    _inherit = 'res.partner'
     
    instructor = fields.Boolean("Instruktur")
    session_ids = fields.Many2many('training.sesi', string="Menghadiri Sesi", readonly=True)
    npwp = fields.Char(string="NPWP")
    norek = fields.Integer(string="Nomor Rekening", default=100)
    pelajar = fields.Boolean(String="Pelajar", default=True)
    