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

def emp_mgr_dept(request):
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').all()
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='A')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='N')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(ename='KING')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING',sal__gt='2000')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE',sal__lt='3000')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(sal__gte='3000')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='FORD')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(sal='3000')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='JONES')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING',sal__gte='5000')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='ALLEN')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(hiredate__year='1981')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING',hiredate__year='1981')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(hiredate__day='2')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(hiredate__year='1987')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(sal__gte=800)
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE',deptno__dname='SALES')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='WARD',deptno__dname='ACCOUNTING')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='SCOTT')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='JONES',hiredate__year='1987')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(hiredate__year='1981',sal__gte='3000')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(comm__gt='0')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE',comm__gt='500')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(sal__gt='3000')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH',hiredate__year='1987')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(hiredate__month='4')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(hiredate__month='2',sal__gte='1500')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(hiredate__month='2',comm__gte='500')
    emp_mgr_dept=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='R')
    

    d={'emp_mgr_dept':emp_mgr_dept}
    return render(request,'emp_mgr_dept.html',d)



def emp_salgrade(request):
    #EO=Emp.objects.all()
    #SO=SalGrade.objects.all()
    # Retrieving the data of employess who belongs to grade 4
    #SO=SalGrade.objects.filter(grade=4)#[grade4 SalgradeObjects]

    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    # Retrieving the data of employess who belongs to grade 3,4
    SO=SalGrade.objects.filter(grade__in=(3,4))

    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))

    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)