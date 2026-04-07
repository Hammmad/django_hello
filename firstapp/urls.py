from django.urls import path, include
from rest_framework.routers import  DefaultRouter
from . import views
from .views import ReservationViewSet
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

router = DefaultRouter()
router.register('reservations', ReservationViewSet)

urlpatterns = [
    # path('function', views.hello_world),
    # path('class', views.HelloLahore.as_view()),
    # path('reservations-home', views.home),
    # path('reservations/', views.get_reservations),
    # path('reservations/<int:id>/', views.get_reservations),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]