"""FMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (
    UserAuthView , UserApiView)

urlpatterns = [
    path('login', UserAuthView.as_view({
        "post": "login"}),
         ),

    path('signup', UserAuthView.as_view({
        "post": "signup"}),
         ),
    path('customer-user', UserApiView.as_view({
        "post":"create_user",
        "get":"get_listing",
        "patch":"edit_user",
        "delete":"delete_user"}),
         ),
    path('dashboard', UserApiView.as_view({
        "get":"get_dashboard"}),
         ),
]
