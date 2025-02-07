from odoo import models ,fields,api
from odoo.exceptions import ValidationError
import datetime
import re


class TeacherDetail(models.Model):
    """
    Description: Student Class which is used to store Teacher information
    """
    _name = "teachers.details" # Set the name of the new model
    _description = "This model is used to store the information of the teacher"
    
    name = fields.Char("Name", required=True)
    age = fields.Integer("Age",compute="_compute_age")
    date_of_birth = fields.Date("Date of Birth", required=True)
    subject = fields.Char("Subject", required=True)
    salary=fields.Integer("Salary", required=True)
    Description=fields.Text("Description", required=True)
    image= fields.Image()
    email=fields.Char("Email Address", required=True)
    number=fields.Char("Mobile Number" , required=True)
    monthly_income=fields.Char("Monthly Income",compute='_compute_monthly_income',stored=True)
    today=fields.Date('Creating Date', compute='_compute_todays_date')
    student_id=fields.One2many('students.details',inverse_name='teacher_id')

    @api.model
    def create(self,vals):
        if not vals['email'] or not vals['number']:
            raise ValidationError("Email and Mobile Number cannot be empty.")
        #Checking the Email Address
        existing_email = self.env['teachers.details'].search([('email', '=', vals['email'])])
        if existing_email:
            raise ValidationError("Email is Already Registered Please Use Another Email")
        else:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', vals['email'])
            if match==None: 
                raise ValidationError("Invalid Email Please Use A Valid Email")
        
        #Checking the Mobile Number 
        valid_number = re.match(r'^[6-9][0-9]{9}$', str(vals['number']))
        if valid_number == None:
            raise ValidationError("Invalid Mobile Number Please Enter A Valid Number")
        else:
            return super(TeacherDetail,self).create(vals)

    @api.depends('salary')
    def _compute_monthly_income(self):
        for records in self:
            records.monthly_income=records.salary/12

    def _compute_todays_date(self):
        self.today=datetime.datetime.now()

    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = datetime.date.today()
                if today.strftime("%m%d") >= record.date_of_birth.strftime("%m%d"):
                    record['age'] = today.year - record.date_of_birth.year
                else:
                    record['age'] = today.year - record.date_of_birth.year - 1
            else:
                record['age'] = 0 
        if record['age']<=-1:
            raise ValidationError("Invalid Date Of Birth")


    def _data_delete(self):
        self.unlink()
    
    def button(self):
        return {
                "name":"Delete data",
                "type": "ir.actions.act_window",
                "res_model": "teachers.data.delete",
                "views": [[False, "form"]],
                "target": "new",
        }