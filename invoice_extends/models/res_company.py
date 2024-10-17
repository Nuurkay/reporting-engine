# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from base64 import b64decode
import io
from io import BytesIO
from PyPDF2 import PdfFileReader, PdfFileWriter

from odoo.exceptions import UserError, ValidationError


class res_company(models.Model):
    _inherit = "res.company"

    account_template = fields.Selection([
            ('fency', 'Fency'),
            ('classic', 'Classic'),
            ('modern', 'Modern'),
            ('odoo_standard', 'Odoo Standard'),
        ], 'Account',default='fency')

    color_account= fields.Char("Account Report Color",
                              help="Background color for Account")
    text_color_account = fields.Char("Text Report Color",
                                  help="Text color for Sale Account")

    watermark_pdf = fields.Binary('Report Watermark')
    file_name = fields.Char('File')

    @api.onchange('watermark_pdf')
    def _onchange_watermark_page(self):
        if self.watermark_pdf:
            pdf_watermark = b64decode(self.watermark_pdf)
            check_pdf = self.file_name.split('.')
            if 'pdf' in check_pdf:
                pdfReader = PdfFileReader(BytesIO(pdf_watermark))
                totalPages = pdfReader.numPages
                if totalPages > 1:
                    raise UserError(_('Watermark Pdf Contain More Than One Page Please Upload One Page Watermark Pdf File.'))
            else:
                raise UserError('Allowed Only Pdf Files.')



class account_invoice(models.Model):
    _inherit = "account.move"

    paypal_chk = fields.Boolean("Paypal")
    paypal_id = fields.Char("Paypal Id")


    def invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        self.ensure_one()
        self.sent = True
        return self.env.ref('invoice_extends.custom_account_invoices').report_action(self)


class res_company(models.Model):
    _inherit = "res.company"

    bank_account_id = fields.Many2one('res.partner.bank', 'Bank Account')

class res_partner_bank(models.Model):
    _inherit = "res.partner.bank"

    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', size=24, change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", 'State')
    country_id = fields.Many2one('res.country', 'Country')
    swift_code = fields.Char('Swift Code')
    ifsc = fields.Char('IFSC')
    branch_name = fields.Char('Branch Name')
