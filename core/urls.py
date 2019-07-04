from django.urls import path
from . import views


urlpatterns = [
    # Post views
    path('', views.home, name='home'),
    path('mydegrees/', views.SpecialtyList.as_view(), name='specialty_list'),
    path('create-degree/', views.SpecialtyCreate.as_view(), name='specialty_create'),
    path('update-degree/<int:pk>', views.SpecialtyUpdate.as_view(), name='specialty_update'),
    path('delete-degree/<int:id>', views.specialty_delete, name="specialty_delete"),
    path('myareas/', views.AreaList.as_view(), name="area_list"),
    path('create-area/', views.AreaCreate.as_view(), name='area_create'),
    path('update-area/<int:pk>', views.AreaUpdate.as_view(), name='area_update'),
    path('delete-area/<int:id>', views.area_delete, name="area_delete"),
    path('inscriptions/', views.InscriptionList.as_view(), name="inscription_list"),

    # path('list/<int:id>/', views.InvoiceList.as_view(), name='invoice_list'),
    # path('detail/<int:invoice_id>/', views.InvoiceDetail.as_view(), name='invoice_detail'),
]