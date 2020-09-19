from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from blog.views import UserViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('users',UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include("blog.urls")),
    path('users/',include(router.urls)),
    path('api-auth/',include("rest_framework.urls")),
    path('docs/',include_docs_urls(title="我的博客",description="记录我的技术历程")),
]
