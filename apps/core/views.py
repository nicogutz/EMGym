from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core import models


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
        try:
            device = models.Device.objects.get(user=request.user)
        except ObjectDoesNotExist:
            device = None

        return render(request, self.template_name, {"device": device})

    def post(self, request, *args, **kwargs):

        device = models.Device(user=request.user, uid=request.POST['uid'])
        try:
            device.save()
        except IntegrityError:
            return render(request, self.template_name, {"device": device, "is_successful": False})

        return render(request, self.template_name, {"device": device, "is_successful": True})
