from django.shortcuts import render,redirect
from .forms import *


# Home page view
def home_page_view(request):
    return render(request, "base/home_page.html")


# Create,show and delete operation for specialization_for_organisation
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


# Create,show,update and delete operation for organisation
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
        

# Create,show and delete operation for degree
def degree(request):
    if request.method == "POST":
        fm = Degree_Form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Degree_Form()
    else:
        fm = Degree_Form()

    all_records = Degree.objects.all()

    return render(
        request,
        "base\degree_page.html",
        {"form": fm, "all_records": all_records},
    )

def delete_degree_record(request, id):
    if request.method == "POST":
        pi = Degree.objects.get(pk=id)
        pi.delete()
        return redirect('degree_page')


# Create,show,update and delete operation for doctor
def doctor(request):
    if request.method == "POST":
        fm = Doctor_Form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm = Doctor_Form()
    else:
        fm = Doctor_Form()

    all_records = Doctor.objects.all()

    return render(
        request,
        "base\doctors_page.html",
        {"form": fm, "all_records": all_records},
    )

def update_doctor_record(request,id):
    if request.method=='POST':
        pi=Doctor.objects.get(pk=id)
        fm=Doctor_Form(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Doctor.objects.get(pk=id)
        fm=Doctor_Form(instance=pi)
    
    return render(request,'base/update_doctor_page.html',{'form':fm})

def delete_doctor_record(request, id):
    if request.method == "POST":
        pi = Doctor.objects.get(pk=id)
        pi.delete()
        return redirect('doctor_page')


# Create,show,update and delete operation for organization staff
def organization_staff(request):
    if request.method == "POST":
        fm = Organisation_Staff_Form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm = Organisation_Staff_Form()
    else:
        fm = Organisation_Staff_Form()

    all_records = Organization_Staff.objects.all()

    return render(
        request,
        "base\organization_staff_page.html",
        {"form": fm, "all_records": all_records},
    )

def update_organisation_staff_record(request,id):
    if request.method=='POST':
        pi=Organization_Staff.objects.get(pk=id)
        fm=Organisation_Staff_Form(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Organization_Staff.objects.get(pk=id)
        fm=Organisation_Staff_Form(instance=pi)
    
    return render(request,'base/update_organization_staff_page.html',{'form':fm})

def delete_organisation_staff_record(request,id):
    if request.method == "POST":
        pi = Organization_Staff.objects.get(pk=id)
        pi.delete()
        return redirect('organization_staff_page')
    

# Create,show,update and delete operation for patient
def patient(request):
    if request.method == "POST":
        fm = Patient_Form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm = Patient_Form()
    else:
        fm = Patient_Form()

    all_records = Patient.objects.all()

    return render(
        request,
        "base\patient_page.html",
        {"form": fm, "all_records": all_records},
    )

def update_patient_record(request,id):
    if request.method=='POST':
        pi=Patient.objects.get(pk=id)
        fm=Patient_Form(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Patient.objects.get(pk=id)
        fm=Patient_Form(instance=pi)
    
    return render(request,'base/update_patient_page.html',{'form':fm})

def delete_patient_record(request,id):
    if request.method == "POST":
        pi = Patient.objects.get(pk=id)
        pi.delete()
        return redirect('patient_page')