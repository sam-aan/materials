from django.conf.urls import path, include  # В Django версии 2 и выше используется path, вместо url
# Также не забудьте подключить include ↑
from django.contrib import admin

urlpatterns = [
    # В новой версии Django вместо url используется функция path
    # url(r'^admin/', admin.site.urls),
    # url(r'^webexample/', include('webexample.urls')),

    path('admin/', admin.site.urls),
    path('webexample/', include('webexample.urls'))
]