from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_page.urls')),
    path('', include('films.urls')),
    path('', include('tags.urls')),
    path('', include('parser_app.urls')),
    path('', include('users.urls')),
    path('recipes_list/', include('recipes.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                    document_root=settings.STATIC_ROOT)
