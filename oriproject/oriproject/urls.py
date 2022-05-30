from django.contrib import admin
from django.urls import path, include
from blog import views as blogviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogviews.home),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]
