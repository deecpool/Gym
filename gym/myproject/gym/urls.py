from django.urls import path,include
from .views import *

urlpatterns = [
    path('',MainHome.as_view(),name='home'),
    path('about/',about,name='about'),
    path('schedule/',schedule,name='schedule'),
    path('services/',services,name='services'),
    path('galery/',galery,name='galery'),
    path('contact/',contact,name='contact'),
    path('cards/',Member.as_view(),name='cards'),
    path('card__about/<slug:card__about__slug>',ShowPost.as_view(),name='card__about'),
    path('trainer_card/<slug:trainer__slug>',ShowTrainer.as_view(),name='trainer')
    
    # path('trainer/<slug:trainer_slug>',trainer_slug,name='trainer_slug')
    
    
    
    
    
    
    
    
    
]
