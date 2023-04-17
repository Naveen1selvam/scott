from django.shortcuts import render
from app.models import * 
def dept(request):
    LOD=Depat.objects.all()
    d={'dt':LOD}
    return render(request,'dept.html',d)
def emp(reqeust):
    LOE=Empt.objects.all()
    d={'et':LOE}
    return render(reqeust,'emp.html',d)