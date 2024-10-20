from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView
from .models import *
cats_db = {}


class MainHome(ListView):
    
    template_name = 'main/main_page.html'
    context_object_name = 'cr'

        
        
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cr'] = CardAbout.objects.all
        context['trainer'] = Trainer.act.all().select_related('classes_type')
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return CardAbout.objects.all().select_related('trainer_classes')




class ShowPost(DetailView):
    model = CardAbout
    template_name = 'main/cards__about.html'
    slug_url_kwarg = 'card__about__slug'
    context_object_name = 'cr'


class ShowTrainer(DetailView):
    model = Trainer
    template_name = 'main/trainercard.html'
    slug_url_kwarg = 'trainer__slug'
    context_object_name = 'trainer'

class Member(ListView):
    template_name = 'main/card.html'
    context_object_name = 'Member'

        
        
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Member'] = Membership.objects.all
        return context

    def get_queryset(self):
        return Membership.objects.all()
  
    



def about(request):
        return render(request,'main/about.html')

def schedule(request):
        return render(request,'main/schedule.html')

def services(request):
        return HttpResponse('3')

def galery(request):
        return HttpResponse('4')

def contact(request):
        return HttpResponse('5')


def cards(request):
        return render(request,'main/card.html')


# def card__about(request,card__about__slug):
#         card = CardAbout.objects.all().select_related('trainer_classes').filter(slug=card__about__slug)
#         trainer = Trainer.act.all().select_related('classes_type')
#         context={
#                 'cr':card,
#                 'trainer':trainer
#         }
        
        
#         return render(request,'main/cards__about.html',context)


