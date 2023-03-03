from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        user.save()
        return redirect('/')


class HomeView(LoginRequiredMixin, generic.View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
