from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('/scoto', views.scoto , name="scoto"),
    path('/add', views.Add, name="add")
    # path('/addIdea'),
]
#   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)