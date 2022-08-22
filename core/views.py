from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView, CreateView
from django.db.models import Q
from core.models import Page, User, Contact
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


class HomeView(TemplateView):
    pass


class SearchResultsView(ListView):
    model = Page
    template_name = "search_results.html"
    paginate_by = 2

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if query:
            object_list = self.model.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        else:
            object_list = self.model.objects.none()
        return object_list


class UserProfileView(DetailView):
    model = User

    def get_object(self):
        return User.objects.get(username=self.kwargs.get("slug"))


class EditProfileView(SuccessMessageMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name']
    success_message = "Your profile has been updated"

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_success_url(self):
        return reverse('edit-profile')

class ContactView(CreateView):
    model = Contact
    fields = ['name', 'email', 'message']

    def form_valid(self, form):
        messages.success(self.request, "Your message has been sent, thank you!")
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject="Feedback form",
            message=message,
            from_email=settings.SERVER_EMAIL,
            recipient_list=settings.ADMINS,
        )
        return super().form_valid(form)
