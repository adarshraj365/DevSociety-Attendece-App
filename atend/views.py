from django.shortcuts import render
import requests
from .models import  present
# Create your views here.
def makeAttendence(request,email):
    url = "http://devsociety.pythonanywhere.com/api/v1/member/mail/adarshraj_api/12527@123/"+email+"/devsociety@data2k19/"
    q = requests.get(url)
    q = q.json()
    x = present()
    x.name = q['name']
    x.mail = q['email']
    x.branch= q['branch']
    x.roll = q['Rollno']
    x.save()
    return render(request,"index.html")