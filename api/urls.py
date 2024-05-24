from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

# Router yaratish va UserViewSet ro'yxatga olish
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    # Router'dan keladigan URL'larni qo'shish
    path('api/', include(router.urls)),
]

# Ushbu kod localhost:8000/api/users/ manziliga kirganda UserViewSet'dagi list va create
# metodlarini, va localhost:8000/api/users/<int:pk>/ manziliga kirganda esa retrieve,
# update, partial_update va destroy metodlarini chaqirish uchun URL'larni yaratadi.
