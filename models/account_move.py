from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        # Only apply to customer invoices
        if vals.get('move_type') == 'out_invoice' and not vals.get('name'):
            sequence = self.env['ir.sequence'].next_by_code('custom.invoice.sequence')
            vals['name'] = sequence
        return super(AccountMove, self).create(vals)
