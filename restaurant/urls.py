from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
  path('', views.index, name='index'),
  path('booking/', include(router.urls)),
  path('menu/', views.MenuItemsView.as_view()),
  path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
  path('api-token-auth/', obtain_auth_token),

]