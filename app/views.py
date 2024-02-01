from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=1981)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='SALES')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=1981,sal__gt=2000)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[:5:]
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[5:11:]
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[::3]
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(job='SALESMAN')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename='SMITH',deptno__dname='RESEARCH')
    
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)