from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

app_name = 'app'

router = SimpleRouter()

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), basename='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), basename = 'token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), basename='token_verify'),
    path('', include(router.urls)),
]
