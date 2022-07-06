from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

def stanishka(request, *args, **kwargs):
    spisok = ["Kalivan", "Dvacheva", "Shurik", "Shrek"]
    return render(request, "advert/stanishka.html",{"lstn": spisok})

class About(TemplateView):
    template_name = "advert/about.html"
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        context['name'] = 'А ну чики брики и в дамки'
        context['title'] = 'Воровская община №6'
        return context
    # def get(self, request):
    #     return render(request, "advert/about.html"< {})    