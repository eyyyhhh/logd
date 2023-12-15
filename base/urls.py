from django.urls import path
from  . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, register_converter
from .converters import LongStringConverter

register_converter(LongStringConverter, 'longstring')

urlpatterns = [
    path('accounts', views.home, name ='home'),
    path('add', views.add_item, name='add_item'),

    #urls for user
    path('', views.login, name='login'),
    path('home/<str:id>/<str:uid>/<str:user>/<str:password>/<str:phone>/<str:usertype>/<str:gender>/<str:address>/<str:age>/<str:birthdate>', views.updateUserInfo, name='updateUserInfo'),
    path('updateFAQ/<str:id>/<longstring:question>/<longstring:answer>', views.updateFAQ, name='updateFAQ'),
    
    path('login/<str:user>/<str:password>', views.log, name='log'),
    path('dash', views.profile, name='dashboard'),
    
    path('SGdash', views.SG, name='SG'),
    path('updateProfile/<str:schoolName>/<str:address>', views.updateProfile, name='updateProfile'),
    path('updateMission/<str:mission>', views.updateMission, name='updateMission'),
    path('updateVission/<str:vission>', views.updateVission, name='updateVission'),
    path('addUser', views.addUser, name='add_user'), 
    path('addFAQ', views.addFAQ, name='add_FAQ'), 
    path('deletefaq/<int:id>', views.delete_faq, name='delete_faq'),
    path('updateUser/<str:pk>', views.updateUser, name='updateUser'),
    path('delete/<int:id>', views.delete_item, name='delete_item'),
    path('generate_qrcode', views.generate_qrcode, name='qr'),


    path('userLogs', views.userLogs, name ='logs'),
    path('userLogs/<int:id>', views.modal, name='modals'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('view/<int:userid>/<int:schoolid>/<int:logsid>/<int:hostid>', views.viewPage, name='viewPage'),

    path('crud/', views.CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', views.UpdateCrudUser.as_view(), name='crud_ajax_update'),

    path('filter_stored_proc/', views.filter_stored_proc, name='filter_stored_proc'),

] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)