from odoo import models, fields

class Products(models.Model):
    _name = 'store.product'
    _description = 'Product'

    name = fields.Char(size=100)
    sku = fields.Char(size=50)
    price = fields.Float()
    quantity = fields.Integer()
    supplier_id = fields.Many2one('store.supplier')
