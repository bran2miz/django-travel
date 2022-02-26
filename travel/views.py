from django.views.generic import TemplateView

class HomePageView(TemplateView):
  template_name = 'home.html'

class AboutView(TemplateView):
  template_name = 'about.html'

class TravelView(TemplateView):
  template_name = 'travels.html'