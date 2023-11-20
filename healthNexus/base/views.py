from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import *
from .decorators import user_has_designation

# Landing page view
def landing_page_view(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data["username"]
            password = fm.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                custom_profile = CustomUserProfile.objects.get(user=user)
                designation = custom_profile.designation
                print(designation)
                if designation == "doctor":
                    return redirect("doctor_home_page")
                elif designation == "patient":
                    return redirect("patient_home_page")
                elif designation== "organization_admin":
                    return redirect("organization_admin_home_page")
                elif designation=="organization_staff":
                    return redirect("organization_staff_home_page")
                elif designation=="super_admin":
                    return redirect("super_admin_home_page")
    else:
        fm = AuthenticationForm()
    return render(request, "base/website_landing_page.html", {"form": fm})
    return render(request, "base/website_landing_page.html", {"form": fm})

# @user_has_designation('doctor')
def doctor_home_page(request):
    personal_info = Doctor.objects.get(doctor_id=request.user.username)
    all_his_patients_records = Patient_History.objects.filter(
        doctor_id=request.user.username
    )
    return render(
        request,
        "base/1_doctor_home_page.html",
        {
            "personal_info": personal_info,
            "his_patient_records": all_his_patients_records,
        },
    )


# @user_has_designation('patient')
def patient_home_page(request):
    personal_info = Patient.objects.get(patient_id=request.user.username)
    all_his_patients_records = Patient_History.objects.filter(
        patient_id=request.user.username
    )[::-1][::-1]
    return render(
        request,
        "base/2_patient_home_page.html",
        {
            "personal_info": personal_info,
            "his_patient_records": all_his_patients_records,
        },
    )

# @user_has_designation('super_admin')
def super_admin_home_page(request):
    return render(request,"base/4_super_admin_home_page.html")


# @user_has_designation('organization_staff')
def organization_staff_home_page(request):
    return render(request,"base/5_organization_staff_home_page.html")


# @user_has_designation('organization_admin')
def organization_admin_home_page(request):
    return render(request,"base/3_organization_admin_home_page.html")

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
        "base/specialization_for_organisation_page.html",
       
        {"form": fm, "all_records": all_records},
    )


def delete_specialization_for_organisation_record(request, id):
    if request.method == "POST":
        pi = Specialization.objects.get(pk=id)
        pi.delete()
        return redirect("specialization_for_organisation_page")


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
        "base/organization_page.html",
        
        {"form": fm, "all_records": all_records},
    )


def update_organization_record(request, id):
    if request.method == "POST":
        pi = Organization.objects.get(pk=id)
        fm = Organization_Form(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Organization.objects.get(pk=id)
        fm = Organization_Form(instance=pi)

    return render(request, "base/update_organization_page.html", {"form": fm})


def delete_organization_record(request, id):
    if request.method == "POST":
        pi = Organization.objects.get(pk=id)
        pi.delete()
        return redirect("organization_page")


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
        "base/degree_page.html",
       
        {"form": fm, "all_records": all_records},
    )


def delete_degree_record(request, id):
    if request.method == "POST":
        pi = Degree.objects.get(pk=id)
        pi.delete()
        return redirect("degree_page")


# Create,show,update and delete operation for doctor
def doctor(request):
    if request.method == "POST":
        fm = Doctor_Form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()

            # First create the entry in the inbuilt user
            username = fm.cleaned_data["doctor_id"]
            dob = fm.cleaned_data["dob"]
            phone_number = fm.cleaned_data["phone_number"]
            password = f"{phone_number}@{dob.day}{dob.month}{dob.year}"
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Now create the entry in the custom user
            custom_user = CustomUserProfile.objects.create(
                user=user,
                designation="doctor",
            )
            custom_user.save()

            fm = Doctor_Form()
    else:
        fm = Doctor_Form()

    all_records = Doctor.objects.all()

    return render(
        request,
        "base/doctors_page.html",
       
        {"form": fm, "all_records": all_records},
    )










def update_doctor_record(request, id):
    if request.method == "POST":
        pi = Doctor.objects.get(pk=id)
        fm = Update_Doctor_Form(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Doctor.objects.get(pk=id)
        fm = Update_Doctor_Form(instance=pi)

    return render(request, "base/update_doctor_page.html", {"form": fm})


def delete_doctor_record(request, id):
    if request.method == "POST":
        pi_1 = Doctor.objects.get(pk=id)
        pi_2 = User.objects.get(username=id)

        # Also deleting the user from inbuilt and custom user
        pi_2.delete()
        pi_1.delete()
        return redirect("doctor_page")


# Create,show,update and delete operation for organization staff
def organization_staff(request):
    if request.method == "POST":
        fm = Organisation_Staff_Form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()

            username = fm.cleaned_data["staff_id"]
            # dob = fm.cleaned_data["dob"]
            # phone_number = fm.cleaned_data["phone_number"]
            first=fm.cleaned_data["first_name"]
            last=fm.cleaned_data["last_name"]
            password = f"{first}@{last}"
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Now create the entry in the custom user
            custom_user = CustomUserProfile.objects.create(
                user=user,
                designation="organization_staff",
            )
            custom_user.save()


            fm = Organisation_Staff_Form()
    else:
        fm = Organisation_Staff_Form()

    all_records = Organization_Staff.objects.all()

    return render(
        request,
        "base/organization_staff_page.html",
        
        {"form": fm, "all_records": all_records},
    )


def update_organisation_staff_record(request, id):
    if request.method == "POST":
        pi = Organization_Staff.objects.get(pk=id)
        fm = Update_Organization_Staff_Form(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Organization_Staff.objects.get(pk=id)
        fm = Update_Organization_Staff_Form(instance=pi)

    return render(request, "base/update_organization_staff_page.html", {"form": fm})


def delete_organisation_staff_record(request, id):
    if request.method == "POST":
        pi = Organization_Staff.objects.get(pk=id)
        pi.delete()
        return redirect("organization_staff_page")


# Create,show,update and delete operation for patient
def patient(request):
    if request.method == "POST":
        fm = Patient_Form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()

            # First create the entry in the inbuilt user
            username = fm.cleaned_data["patient_id"]
            dob = fm.cleaned_data["dob"]
            phone_number = fm.cleaned_data["phone_number"]
            password = f"{phone_number}@{dob.day}{dob.month}{dob.year}"
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Now create the entry in the custom user
            custom_user = CustomUserProfile.objects.create(
                user=user,
                designation="patient",
            )
            custom_user.save()

            fm = Patient_Form()
    else:
        fm = Patient_Form()

    all_records = Patient.objects.all()

    return render(
        request,
       
        "base/patient_page.html",
        {"form": fm, "all_records": all_records},
    )


def update_patient_record(request, id):
    if request.method == "POST":
        pi = Patient.objects.get(pk=id)
        fm = Update_Patient_Form(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Patient.objects.get(pk=id)
        fm = Update_Patient_Form(instance=pi)

    return render(request, "base/update_patient_page.html", {"form": fm})


def delete_patient_record(request, id):
    if request.method == "POST":
        pi_1 = Patient.objects.get(pk=id)
        pi_2 = User.objects.get(username=id)

        # Also deleting the user from inbuilt and custom user
        pi_2.delete()
        pi_1.delete()

        return redirect("patient_page")


# Create,show,update and delete for patient history
def patient_history(request):
    if request.method == "POST":
        fm = Patient_History_Form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            fm = Patient_History_Form()
    else:
        fm = Patient_History_Form()

    all_records = Patient_History.objects.all()

    return render(
        request,
        
        "base/patient_history_page.html",
        {"form": fm, "all_records": all_records},
    )


def update_patient_history_record(request, id):
    if request.method == "POST":
        pi = Patient_History.objects.get(pk=id)
        fm = Patient_History_Form(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Patient_History.objects.get(pk=id)
        fm = Patient_History_Form(instance=pi)

    return render(request, "base/update_patient_history_page.html", {"form": fm})


def delete_patient_history_record(request, id):
    if request.method == "POST":
        pi = Patient_History.objects.get(pk=id)
        pi.delete()
        return redirect("patient_history_page")


# Create,show and delete for organization admin
def organization_admin(request):
    if request.method == "POST":
        fm = Organization_Admin_Form(request.POST)
        if fm.is_valid():
            fm.save()
            fm.save()
            print(fm.cleaned_data["organization_id"])
            # First create the entry in the inbuilt user
            username=fm.cleaned_data["unique_id"]
            first = fm.cleaned_data["first_name"]
            last = fm.cleaned_data["last_name"]
            password = f"{first}@{last}"
            print(password)
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Now create the entry in the custom user
            custom_user = CustomUserProfile.objects.create(
                user=user,
                designation="organization_admin",
            )
            custom_user.save()
            fm = Organization_Admin_Form()
    else:
        fm = Organization_Admin_Form()

    all_records = Organization_Admin.objects.all()

    return render(
        request,
        "base/organization_admin_page.html",
        
        {"form": fm, "all_records": all_records},
    )


def delete_organization_admin_record(request, id):
    if request.method == "POST":
        pi = Organization_Admin.objects.get(pk=id)
        pi.delete()
        return redirect("organization_admin_page")


