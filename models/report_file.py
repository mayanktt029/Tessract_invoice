from odoo import models, api


class ReportSalesDocument(models.AbstractModel):
    _name = 'report.tessract.report_sales_document'  # This should match the 'name' field in the report definition XML
    _description = 'Sales Document Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)  # Ensure you are using the correct model

        return {
            'docs': docs  # Pass 'docs' to the template
        }
