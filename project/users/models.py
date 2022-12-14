from distutils.command.upload import upload
from turtle import mode
from unittest.util import _MAX_LENGTH

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django_userforeignkey.models.fields import UserForeignKey
from django.conf import settings


class Personal_info(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete= models.CASCADE)
    employee_id = models.IntegerField(unique=True)
    e_unit = models.TextField(max_length=47)
    e_division = models.TextField(max_length=47)
    employee_name = models.TextField(max_length=47)
    email= models.EmailField(max_length=50)
    father_name = models.TextField(max_length=255)
    mother_name = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField()
    home_district = models.TextField(max_length=255)
    gender = models.TextField(max_length=50)
    religion = models.TextField(max_length=255)
    national_ID  = models.IntegerField()
    passport = models.TextField(max_length=255)
    driving_licence = models.TextField(max_length=50)
    gpf_cpf  = models.IntegerField()
    phone = models.IntegerField()
    blood_group= models.TextField(max_length=3)
    marital_status = models.TextField(max_length=20)
    specialization = models.TextField(max_length=500)
    about_summary= models.TextField()
    pro_pic= models.ImageField(upload_to='images/')
    signature_pic = models.ImageField(upload_to='signatures/')

class Contract_info(models.Model):
    # personal_info= models.OneToOneField(Personal_info, blank=True, null=True, on_delete= models.CASCADE)
    user = models.OneToOneField(User,null=True, blank=True, on_delete= models.CASCADE)
    present_address = models.TextField(max_length= 300)
    parmanent_address = models.TextField(max_length= 300)
    emergency_name = models.TextField(max_length= 300)
    present_post_office= models.TextField(max_length= 300)
    parmanent_post_office = models.TextField(max_length= 300)
    emergency_relation= models.TextField(max_length= 300)
    present_police_station =  models.TextField(max_length= 300)
    parmanent_police_station = models.TextField(max_length= 300)
    emergency_address=  models.TextField(max_length= 300)
    present_district =  models.TextField(max_length= 300)
    parmanent_district = models.TextField(max_length= 300)
    emergency_phone = models.IntegerField()
    present_upazila =  models.TextField(max_length= 300)
    parmanent_upazila = models.TextField(max_length= 300)
    emergency_cell_no = models.IntegerField()
    present_tel_number = models.IntegerField()
    parmanent_tel_number = models.IntegerField()
    emergency_email =  models.TextField(max_length= 50)

class Joining_info(models.Model):
    # personal_info= models.OneToOneField(Personal_info,blank=True, null=True, on_delete= models.CASCADE)
    user = models.OneToOneField(User,null=True, blank=True, on_delete= models.CASCADE)
    rank= models.TextField(max_length= 300)
    grade = models.TextField(max_length= 300)
    designation= models.TextField(max_length= 300)
    batch= models.TextField(max_length= 300)
    workStation= models.TextField(max_length= 300)
    joining_date= models.DateField()
    office_name=  models.TextField(max_length= 300)
    prl_date = models.DateField()
    department= models.TextField(max_length= 300)
    order_no_date= models.TextField(max_length= 300)
    district= models.TextField(max_length= 300)
    conf_date= models.DateField()
    upazila=  models.TextField(max_length= 300)
    gazatted_date= models.DateField()
    job_nature= models.TextField(max_length= 300)
    edndorsement_date=  models.TextField()

class EducationInformation(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete= models.CASCADE)
    # user = UserForeignKey(auto_user_add=True, related_name="user_models", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    degree= models.TextField(max_length= 300)
    r_department= models.TextField(max_length= 300)
    board_university= models.TextField(max_length= 300)
    passing_year= models.IntegerField()
    result= models.IntegerField()
    distinction= models.TextField(max_length= 300)

class SpouseInformation(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    spouse_name= models.TextField(max_length= 300, blank=True)
    spouse_home_district = models.TextField(max_length= 300 , blank=True)
    spouse_occupation =  models.TextField(max_length= 300 , blank=True)
    spouse_designation =  models.TextField(max_length= 300 , blank=True)
    spouse_org_name =  models.TextField(max_length= 300 , blank=True)
    spouse_org_address =  models.TextField(max_length= 400 , blank=True)
    spouse_cell_no = models.IntegerField( blank=True)

class ChildrenInformation(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    clild_name=  models.TextField(max_length= 150)
    clild_gerder=  models.TextField(max_length= 50)
    clild_birthDate= models.DateField()
    clild_BirthPlace= models.TextField(max_length= 200)
    clild_Remarks= models.TextField(max_length= 500)

class TraningInformation(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    traning_type= models.TextField(max_length= 150)
    traning_title= models.TextField(max_length= 300)
    traning_institution= models.TextField(max_length= 200)
    traning_country= models.TextField(max_length= 150)
    traning_start_date= models.DateField()
    traning_end_date= models.DateField()
    traning_grade= models.IntegerField()
    traning_position= models.TextField(max_length= 150)

class PostingInformation(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    p_designation= models.TextField(max_length= 100)
    p_office= models.TextField(max_length= 150)
    p_district= models.TextField(max_length= 50)
    p_upazila= models.TextField(max_length= 80)
    p_form_date= models.DateField()
    p_to_date= models.DateField()
    p_till_today= models.TextField(max_length= 150)

class PromotionInformatrion(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    pro_designation=  models.TextField(max_length= 150)
    pro_nature=  models.TextField(max_length= 150)
    pro_promotion_date=  models.DateField()
    pro_order_no=  models.TextField(max_length= 100)
    pro_order_date=  models.DateField()
    pro_remarks=  models.TextField(max_length= 300)

class AchievementInformation(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    achievement_type= models.TextField(max_length= 100)
    achievement_year=  models.DateField()
    achievement_description=  models.TextField(max_length= 400)

class LeaveInformation(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    leave_type = models.TextField(max_length= 150)
    leave_form= models.DateField()
    leave_to= models.DateField()
    leave_description= models.TextField(max_length= 400)

class OtherServiceInformation(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    otherService_type = models.TextField(max_length= 150)
    otherService_address =  models.TextField(max_length= 300)
    otherService_designation =  models.TextField(max_length= 150)
    otherService_form= models.DateField()
    otherService_to= models.DateField()

class OtherActivitiesInformation(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    otherActivities_type = models.TextField(max_length= 150)
    otherActivities_role =  models.TextField(max_length= 200)
    otherActivities_form= models.DateField()
    otherActivities_to= models.DateField()

class R_and_D_ProjectsInformation(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    r_and_d_Project_type = models.TextField(max_length= 100)
    r_and_d_ProjectName = models.TextField(max_length= 250)
    r_and_d_Project_role = models.TextField(max_length= 150)
    r_and_d_Project_status= models.TextField(max_length= 50)
    r_and_d_Project_tenure= models.TextField(max_length= 50)

class ThesisSupervisionInformation(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    thesisSupervision_type = models.TextField(max_length= 50)
    thesisSupervision_supervisors = models.TextField(max_length= 300)
    thesisSupervision_studentName = models.TextField(max_length= 100)
    thesisSupervision_studentSession= models.TextField(max_length= 50)
    thesisSupervision_thesisTitle = models.TextField(max_length= 300)

class ResearchInterestInformation(models.Model):
    user= models.ForeignKey(User, null=True, blank=True, on_delete= models.CASCADE)
    researchInterest_fields = models.TextField(max_length= 200)

# class Comment(models.Model):
#     name = models.CharField(max_length=42)
#     email = models.EmailField(max_length=75)
#     website = models.URLField(max_length=200, null=True, blank=True)
#     content = models.TextField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
