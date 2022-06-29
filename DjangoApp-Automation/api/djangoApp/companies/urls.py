from rest_framework import routers

from companies.views import CompanyViewSet

companies_router = routers.DefaultRouter()
companies_router.register("companies", viewset=CompanyViewSet, basename="companies")