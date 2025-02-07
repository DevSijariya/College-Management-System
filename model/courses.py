from odoo import fields,models

class CoursesDetails(models.Model):
    _name="courses.details"
    _description="Courses Descriptions"

    name=fields.Char('Course Name')
    description=fields.Text("Couerse Descriptions")
    price=fields.Integer("Course Price")
    