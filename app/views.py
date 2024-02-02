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


def selfjoins(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lte=2000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lt=2000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING',sal__gt=2000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(ename='JONES')
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='ALLEN')
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING',sal__gte=1500)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE',sal__lte=1500)
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='SCOTT')
   

    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoins.html',d)

