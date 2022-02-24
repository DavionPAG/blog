from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
  template_name = "pages_templates/home.html"

class AboutView(TemplateView):
  template_name = "pages_templates/about.html"