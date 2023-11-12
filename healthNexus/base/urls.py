from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',home_page_view,name='home_page'),
    
    path('specialization_for_organisation_page/',specialization_for_organisation,name='specialization_for_organisation_page'),
    path('specialization_for_organisation_page/delete_specialization_for_organisation_record/<int:id>', delete_specialization_for_organisation_record, name='delete_specialization_for_organisation_record'),

    path('organization_page/',organization,name='organization_page'),
    path('organization_page/delete_organization_record/<int:id>',delete_organization_record,name='delete_organization_record'),
    path('organization_page/update_organization_record/<int:id>',update_organization_record,name='update_organization_record')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
