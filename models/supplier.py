from odoo import fields, models

class Supplier(models.Model):
    _name = 'store.supplier'

    name = fields.Char(size=100)
    phone = fields.Char(size=12)
    address = fields.Char(size=250)
