from django.shortcuts import render
from django.http import *
from . import models
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import datetime, date
import PyPDF2
import os
import hashlib
import random

def student_registration(request):
    return render(request, "student_registration.html")

def category_selection(request):
    return render(request, "category_selection.html")

def thanku(request):
    if request.method == 'POST':
        clss = int(request.POST.get('class'))
        sect = request.POST.get('sec')
        file = request.FILES.get('excel')
        names = request.POST.get('names')
        adm = request.POST.get('adm')
        DOBs = request.POST.get('DOB')
        names = names.split("\r\n")
        DOBS = DOBs.split("\r\n")
        adm = adm.split("\r\n")
        DOB = []
        boo=False
        try:
            for dt in DOBS:
                print(dt)
                d = int(dt[:2])
                my = dt[3:]
                m = int(my[:2])
                y = int(my[3:])
                DOB.append(date(y, m, d))
        except:
            pass
        data = models.teacher_data(
            Class=str(clss) + ' ' + sect, excel_pdf=file)
        data.save()
        pdfReader = PyPDF2.PdfFileReader(file)
        faulty = []
        for i in range(len(adm)):
            pdfWriter = PyPDF2.PdfFileWriter()
            st_data = models.student_data.objects.filter(Q(admission__icontains=adm[i]) & Q(roll__icontains=i + 1) & Q(date__icontains=DOB[i]) & Q(sec__icontains=sect) & Q(Class__icontains=clss))
            try:
                if not st_data:
                    pdfWriter.addPage(pdfReader.getPage(i))
                    rd='admd_' + str(random.randint(999,9999999)) +adm[i]
                    re = hashlib.sha256(rd.encode())
                    result = str(re.hexdigest()) + '.pdf'

                    with open('/home/kv6registration/kv6_registratipn/media/report_pdf/'+result, "wb") as f:
                        pdfWriter.write(f)
                    f.close()
                    stu_data = models.student_data(
                         roll=i + 1, Class=clss, sec=sect, admission=adm[i], name=names[i], date=DOB[i], pdf='report_pdf/'+result)
                    stu_data.save()

            except:
                if len(adm[i]) != 0:
                    faulty.append(names[i])
                    boo=True
    return render(request, "thank_u.html", {'fault': faulty,'boo':boo})

#login id and passwords for teachers
logging={'shuvam':'shuvam_123','sahil':'sahil_123','anil':'anil_123'}

def upload(request):
    name = pswd = ''
    name = request.GET.get('name')
    pswd = request.GET.get('pswd')
    for nm in logging:
        if name==nm and pswd==logging[nm]:
            return render(request, "teacher_uploading.html")
            break
    else:
        return HttpResponseRedirect('/login/')

def login(request):
    return render(request, "login.html")

def thanx(request):
    return render(request, "thank_u.html")

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Class = int(request.POST.get('class'))
        roll = request.POST.get('roll')
        adm = request.POST.get('admission')
        sect = request.POST.get('sec')
        dob = datetime.strptime(request.POST.get('dob'), '%Y-%m-%d').date()
        if adm is not None and dob is not None and Class is not None:
            st_data = models.student_data.objects.filter(Q(admission__icontains=adm) & Q(
                roll__icontains=int(roll)) & Q(date__icontains=dob) & Q(sec__icontains=sect) & Q(Class__icontains=Class))
        elif name is not None and roll is not None and dob is not None and Class is not None:
            st_data = models.student_data.objects.filter(Q(admission__icontains=adm) & Q(name__icontains=name) & Q(
                roll__icontains=int(roll)) & Q(date__icontains=dob) & Q(sec__icontains=sect) & Q(Class__icontains=Class))
        else:
            return HttpResponseRedirect('/student_registration/')
        if st_data:
            return render(request, "reportcard.html", {'data': st_data[0]})
        else:
            return render(request, "sorry.html")