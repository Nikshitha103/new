from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router=DefaultRouter()
router.register(r'items',ItemViewSet)

urlpatterns=[
    #path('',views.add_db,name='add_db'),
    path('success/',views.success, name='success'),
    path("update/<str:pername>/<str:perage>/",views.update,name="update"),
    path("delete/<str:pername>/<str:perage>/",views.delete, name="delete"),
    path('',include(router.urls)),
    
]