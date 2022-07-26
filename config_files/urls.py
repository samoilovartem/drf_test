from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from famous_women.views import *
from rest_framework import routers
from famous_women.routers import MyCustomRouter

# router = MyCustomRouter()
# router.register(r'famous-women', FamousWomenViewSet)
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/', include(router.urls))  # http://127.0.0.1:8000/api/v1/famous-women/
    path('api/v1/famous-women/', FamousWomenApiList.as_view()),
    path('api/v1/famous-women/<int:pk>/', FamousWomenApiUpdate.as_view()),
    path('api/v1/famous-women/delete/<int:pk>/', FamousWomenApiDestroyView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
