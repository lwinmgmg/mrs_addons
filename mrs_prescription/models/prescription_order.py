from odoo import models, fields


class PrescriptionOrder(models.Model):
    _name = "mrs.prescription.order"

    _description = "Prescription Order"

    visit_id = fields.Many2one(comodel_name="mrs.visit")
    patient_id = fields.Many2one(
        comodel_name="res.partner",
        related="visit_id.patient_id",
        readonly=False,
        store=True,
        index=True,
    )
    # Related to Dose
    is_dose_free_text = fields.Boolean("Free Text Dose?", default=False)
    dose_free_text = fields.Text()
    product_id = fields.Many2one(comodel_name="product.product", string="Drug")
    quantity = fields.Float(string="Dose")
    uom_id = fields.Many2one(comodel_name="uom.uom", string="Dose Unit")

    # Dose Frequency
    frequency_qty = fields.Float(string="Frequency (Times)")
    frequency_uom_id = fields.Many2one(comodel_name="uom.uom", string="Frequency Unit")

    # Dose Duration
    start_date = fields.Datetime()
    duration = fields.Float()
    duration_uom_id = fields.Many2one(comodel_name="uom.uom")

    # Notes
    note = fields.Text()
    is_prn = fields.Boolean("Take as needed")
    prn_reason = fields.Text("P.R.N. Reason")

    # Dispensing
    dispensing_instruction = fields.Text()
    dispense_qty = fields.Float(string="Quantity to dispense")
    dispense_uom_id = fields.Many2one(comodel_name="uom.uom", string="Quantity unit")
    prescription_refills = fields.Float()