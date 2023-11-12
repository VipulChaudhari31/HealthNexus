from django.shortcuts import render,redirect
from .forms import *


# Create your views here.
def home_page_view(request):
    return render(request, "base/home_page.html")


def specialization_for_organisation(request):
    if request.method == "POST":
        fm = Specialization_Form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Specialization_Form()
    else:
        fm = Specialization_Form()

    all_records = Specialization.objects.all()

    return render(
        request,
        "base\specialization_for_organisation_page.html",
        {"form": fm, "all_records": all_records},
    )


def delete_specialization_for_organisation_record(request, id):
    if request.method == "POST":
        pi = Specialization.objects.get(pk=id)
        pi.delete()
        return redirect('specialization_for_organisation_page')
    
def organization(request):
    if request.method == "POST":
        fm = Organization_Form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Organization_Form()
    else:
        fm = Organization_Form()

    all_records = Organization.objects.all()

    return render(
        request,
        "base\organization_page.html",
        {"form": fm, "all_records": all_records},
    )

def update_organization_record(request,id):
    if request.method=='POST':
        pi=Organization.objects.get(pk=id)
        fm=Organization_Form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Organization.objects.get(pk=id)
        fm=Organization_Form(instance=pi)
    
    return render(request,'base/update_organization_page.html',{'form':fm})
        

def delete_organization_record(request, id):
    if request.method == "POST":
        pi = Organization.objects.get(pk=id)
        pi.delete()
        return redirect('organization_page')