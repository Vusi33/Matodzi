from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name = 'vusi/index.html'

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message Sent Successful!")
            return redirect('index')
        return render(request, self.template_name, {'form': form})


def index_view(request):
    return render(request, 'vusi/index.html')


def inner_page_view(request):
    return render(request, 'vusi/inner-page.html')

def portfolio_details_view(request):
    return render(request, 'vusi/portfolio-details.html')
