"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from companies.urls import companies_router
from companies.views import send_company_email, FibonacciView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(companies_router.urls)),
    path("send-email", send_company_email),
    path('fibonacci', FibonacciView.as_view(), name='fib-seq')
]