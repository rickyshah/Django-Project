from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = 'index.html'

class LoggedPage(TemplateView):
    template_name = 'logged.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'
