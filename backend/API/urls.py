from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('title/<str:id>/', views.title),
    path('search/<str:query>', views.search),
    path('other/<str:goal>/', views.others),
    path('profile/', views.profile),
    path('register/', views.register),

    # tokens url
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]