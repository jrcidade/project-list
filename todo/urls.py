from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.tasks.urls')),
    path('accounts/', include('todo.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
