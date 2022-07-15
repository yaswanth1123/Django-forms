from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.
def insert_school(request):
    sf=schoolform()
    d={'sf':sf}
    if request.method=='POST':
        FD=schoolform(request.POST)
        if FD.is_valid():
            id=FD.cleaned_data.get('id')
            name=FD.cleaned_data.get('name')
            S=school.objects.get_or_create(sid=id,sname=name)[0]
            S.save()
            return HttpResponse('school is inserted successful')
    return render(request,'insert_school.html',d)