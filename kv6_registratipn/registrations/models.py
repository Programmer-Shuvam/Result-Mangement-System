from django.db import models

# Create your models here.


class student_data(models.Model):
    name = models.CharField(max_length=50, default='Mr. NoBody')
    roll = models.IntegerField()
    Class = models.IntegerField()
    sec=models.CharField(max_length=3,default='A')
    admission = models.CharField(max_length=20)
    date = models.DateField()
    pdf = models.FileField(upload_to="report_pdf")

    def __str__(self):
        return str(self.Class)+' '+self.sec + ' '+str(self.roll)


class teacher_data(models.Model):
    Class = models.CharField(max_length=50)
    excel_pdf = models.FileField(upload_to="excel_pdf")

    def __str__(self):
        return self.Class


''' I have set the mysql field type to a mediumblob and the django field type to textfield.
    I have used a queryset and httpresponse to view the PDF objects in a browser (but not directly in django).<- "from stakoverflow" '''
