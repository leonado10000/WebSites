from django.urls import path
from . import views
urlpatterns = [
    path('/scoto', views.scoto , name="scoto"),
    path('/star/<int:page_id>', views.idea, name="idea")
    # path('/addIdea'),
]