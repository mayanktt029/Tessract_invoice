from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    gst_number = fields.Char(string="GST Number")
    contact_number = fields.Char(string="Contact Number")
    client_name = fields.Char(string="Client Name")

    @api.constrains('contact_number')
    def _check_contact_number(self):
        for record in self:
            if record.contact_number:
                if len(record.contact_number) < 10:
                    raise ValidationError("Please enter a correct Contact Number. It must be 10 digits.")
                elif len(record.contact_number) > 10:
                    raise ValidationError("Please enter a correct Contact Number. It should not exceed 10 digits.")
                elif not record.contact_number.isdigit():
                    raise ValidationError("Contact Number must contain only numeric digits.")
