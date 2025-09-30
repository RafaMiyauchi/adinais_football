from django.urls import path
from main.views import (
    show_main, create_product, delete_product, show_product, 
    edit_product, register, login_user, logout_user,
    show_xml, show_json, show_xml_by_id, show_json_by_id
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product, name='create_product'),
    path('products/<uuid:id>/', show_product, name='show_detail'),
    path('edit/<uuid:id>/', edit_product, name='edit_product'),
    path('delete/<uuid:id>/', delete_product, name='delete_product'),

    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
]
