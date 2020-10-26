from django.urls import path
from accounts.views import registration_view, login_view, logout_view

app_name = 'accounts'
urlpatterns = [
    path('register/' , registration_view , name = 'accounts-register'),
    path('logout/', logout_view , name = 'accounts-logout'),
    path('login/', login_view , name = 'accounts-login')
]
