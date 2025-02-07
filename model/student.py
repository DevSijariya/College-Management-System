from odoo import models ,fields,api
from odoo.exceptions import UserError

class StudentDetail(models.Model):
    """
    Description: Student Class which is used to store student information
    """
    _name = "students.details" # Set the name of the new model
    _description = "This Model is used to store the information of the student "

    name = fields.Char("Name",required=True)
    age = fields.Integer("Age")
    date_of_birth = fields.Date("Date of Birth")
    profile_pic = fields.Image("Image")
    roll_number = fields.Integer("Roll Number")
    branch = fields.Char("Branch")
    admission_date=fields.Date('Admission Date')
    leaving_date=fields.Date('leaving Date')
    section = fields.Selection([('A', 'A'), ('B', 'B'),('C','C'),('D','D')])
    active=fields.Boolean("Student Present", default=True)
    Description=fields.Text("Description")
    teacher_id=fields.Many2one(comodel_name='teachers.details',relation="student_course_rel",column1="name",column2="name")
    course_ids=fields.Many2many(comodel_name='courses.details')

    def create(self,vals):
        return super(StudentDetail,self).create(vals)

    @api.ondelete(at_uninstall=False)
    def _unlink_record(self):
        if any(record.active==True for record in self):
            raise UserError("You Can not delete this record")
    
    @api.constrains('roll_number')
    def _check_unique_roll_number(self):
        for record in self:
            duplicate = self.search([('roll_number', '=', record.roll_number), ('id', '!=', record.id)])
            if duplicate:
                raise UserError(f"The roll number {record.roll_number} is already assigned to another student.")

    