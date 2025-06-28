from django.shortcuts import render
from .models import Empmodel
# Create your views here.

def index(request):
    res=render (request,"index.html",context={})
    return res

def addemp(request):
    res=render(request,"addemp.html",context={})
    return res

def updateemp(request):
    res=render(request,"updateemp.html",context={})
    return res

def delemp(request):
    res=render(request,"listemp.html",context={})
    return res


def insertemp(request):
    empno=request.GET.get('empno')
    ename=request.GET.get('ename')
    job=request.GET.get('job')
    sal=request.GET.get('sal')
    EmpModel=objects.create(empno=empno,ename=ename,job=job,sal=sal)
    res=render(request,"addemp.html",context={})
    return res
def modifyemp(request):
    empno=request.GET.get('empno')
    ename=request.GET.get('ename')
    emp=EmpModel.objects.get(empno=empno)
    res=render(request,"addemp.html",context={})
    return res


def remove(request):
      empno=request.GET.get('empno')
      qs=EmpModel.objects.filter(empno=empno)
      qs.delete()
      res=render.objects.filter(empno=empno)
      return res

def displayemp(request):
    qs=EmpModel.objects.all()
    res=render(request,"listemp.html",context={'emp':qs})
    return res






