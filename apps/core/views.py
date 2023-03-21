from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core import models
from apps.core.utils.generate_plot import generate_plot
import pandas as pd
import json


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        user.save()
        return redirect("/")


class HomeView(LoginRequiredMixin, generic.View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        try:
            device = models.Device.objects.get(user=request.user)
        except ObjectDoesNotExist:
            device = None

        try:
            exercises = list(models.Exercise.objects.filter(device=device).values())
        except ObjectDoesNotExist:
            exercises = []

        return render(
            request,
            self.template_name,
            {
                "device": device,
                "plot_div": generate_plot(pd.DataFrame()),
                "exercises": json.dumps(exercises, default=str),
            },
        )

    def post(self, request, *args, **kwargs):
        try:
            device = models.Device(user=request.user, uid=request.POST["uid"])
            try:
                device.save()
            except IntegrityError:
                return render(
                    request,
                    self.template_name,
                    {"device": device, "is_successful": False},
                )

            return render(
                request, self.template_name, {"device": device, "is_successful": True}
            )
        except KeyError:
            pass
        try:
            data = list(
                models.Datum.objects.filter(
                    exercise_id=request.POST["exercise_id"]
                ).values()
            )
        except ObjectDoesNotExist:
            data = []

        device = models.Device.objects.get(user=request.user)
        exercises = list(models.Exercise.objects.filter(device=device).values())

        try:
            df = pd.DataFrame(data)[["data_count", "value"]].set_index("data_count")
        except KeyError:
            df = pd.DataFrame()
        return render(
            request,
            self.template_name,
            {
                "device": True,
                "is_successful": None,
                "plot_div": generate_plot(df),
                "exercises": json.dumps(exercises, default=str),
            },
        )
