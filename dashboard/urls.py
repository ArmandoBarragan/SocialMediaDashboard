from django.urls import path
from dashboard.views import index_view, creation_view, login_view
urlpatterns = [
    path('', index_view, name="index"),
    path('create', creation_view, name='sign_up'),
    path('login', login_view, name='login')
]