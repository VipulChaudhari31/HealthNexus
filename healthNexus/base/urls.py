from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # View for home page
    path('',home_page_view,name='home_page'),
    
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

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
