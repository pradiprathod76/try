from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from tutorials import views

urlpatterns = [
    path('tutorials/upload/', views.uploadTutorial, name='upload_tutorial'),
    path('tutorials/', views.tutorialList, name='tutorial_list'),
    path('tutorials/<int:pk>', views.deleteTutorial, name='tutorial'),
    path('update/<int:pk>',views.updateTutorial,name='update_tutorial'),
    path('edit/<int:pk>',views.editTutorial,name='edit')
]

if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
