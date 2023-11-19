from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # View for landing page
    path('',landing_page_view,name='landing_page_view'),

    # View for patient personal home page
    path('patient_home_page',patient_home_page,name='patient_home_page'),

    # View for doctor personal home page
    path('doctor_home_page',doctor_home_page,name='doctor_home_page'),

    # View for home page
    path('home_page/',home_page_view,name='home_page'),
    
    # Views for specialization_for_organisation
    path('specialization_for_organisation_page/',specialization_for_organisation,name='specialization_for_organisation_page'),
    path('specialization_for_organisation_page/delete_specialization_for_organisation_record/<int:id>', delete_specialization_for_organisation_record, name='delete_specialization_for_organisation_record'),

    # Views for organisation
    path('organization_page/',organization,name='organization_page'),
    path('organization_page/delete_organization_record/<int:id>',delete_organization_record,name='delete_organization_record'),
    path('organization_page/update_organization_record/<int:id>',update_organization_record,name='update_organization_record'),

    # Views for degree
    path('degree_page/',degree,name='degree_page'),
    path('degree_page/delete_degree_record/<int:id>',delete_degree_record,name='delete_degree_record'),

    # Views for doctor
    path('doctor_page/',doctor,name='doctor_page'),
    path('doctor_page/delete_doctor_record/<str:id>',delete_doctor_record,name='delete_doctor_record'),
    path('doctor_page/update_doctor_record/<str:id>',update_doctor_record,name='update_doctor_record'),

    # Views for organisation staff
    path('organization_staff_page/',organization_staff,name='organization_staff_page'),
    path('organization_staff_page/delete_organization_staff_record/<str:id>',delete_organisation_staff_record,name='delete_organization_staff_record'),
    path('organization_staff_page/update_organization_staff_record/<str:id>',update_organisation_staff_record,name='update_organization_staff_record'),

    # Views for patient
    path('patient_page/',patient,name='patient_page'),
    path('patient_page/delete_patient_record/<str:id>',delete_patient_record,name='delete_patient_record'),
    path('patient_page/update_patient_record/<str:id>',update_patient_record,name='update_patient_record'),

    # View for patient_history
    path('patient_history_page',patient_history,name='patient_history_page'),
    path('patient_history_page/delete_patient_history_record/<int:id>',delete_patient_history_record,name='delete_patient_history_record'),
    path('patient_history_page/update_patient_history_record/<int:id>',update_patient_history_record,name='update_patient_history_record'),
    path('logout/',Logout,name='logout'),
    # View for organization admin
    path('organization_admin_page',organization_admin,name='organization_admin_page'),
    path('organization_admin_page/delete_organization_admin_records/<str:id>',delete_organization_admin_record,name='delete_organization_admin_record')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
