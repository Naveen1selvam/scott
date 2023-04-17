from django.db import models

# Create your models here.
class Depat(models.Model):
    DeptNo=models.IntegerField(primary_key=True)
    DName=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
    def __str__(self):
        return self.DName
class Empt(models.Model):
    DeptNo=models.ForeignKey(Depat,on_delete=models.CASCADE)
    EmpNo=models.IntegerField(primary_key=True)
    EName=models.CharField(max_length=100,unique=True)
    Job=models.CharField(max_length=100)
    Mgr=models.IntegerField()
    HireDate=models.DateField()
    Salary=models.IntegerField()
    Commission=models.IntegerField(null=True,blank=True)
    
    def __str__(self): 
        return self.EName

