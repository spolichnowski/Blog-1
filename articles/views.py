from django.conf import settings

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
)
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import EmailMessageForm
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'article_list'
    paginate_by = 6


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'


class ArticleAddView(CreateView):
    model = Article
    success_url = reverse_lazy('list')
    template_name = 'articles/article_add.html'
    fields = ['title','title_image', 'slug', 'content', 'tags']


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/article_add.html'
    fields = ['title','title_image', 'slug', 'content', 'tags']
    success_url = reverse_lazy('list')


def email(request):
    if request.method == 'GET':
        form = EmailMessageForm()
    else:
        form = EmailMessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    name,
                    message,
                    settings.EMAIL_HOST_USER,
                    ('stachpolichnowski@gmail.com',),
                    fail_silently=True

                )
            except BadHeaderError:
                return HttpResponse('coś tam') #uzupełnij luju !!!!
#            return redirect('Dziękujemy')
    return render(request, 'articles/email.html', {'form': form})
