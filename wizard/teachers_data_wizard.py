from odoo import fields,models

class TeachersDataDelete(models.TransientModel):
    _name="teachers.data.delete"
    _description=" Delete Teachers Data"

    teachers_id=fields.Many2one(
        string="Teachers Data Delete",
        comodel_name="teachers.details",
        relation='teachers_data_rel'
    )

    def action_delete_data(self):
        self.teachers_id.unlink()