from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet )
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed',views.UserProfileFeedViewSet)
"""for a model viewset you dont need to specify the base name beacuse rest_framework will auto figure this out"""
urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
