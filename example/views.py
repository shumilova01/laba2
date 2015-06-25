# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from models import Produkty, Sklady, Postavki

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        producty = Produkty.objects.all()
        sklady = Sklady.objects.all()
        postavki = Postavki.objects.all()
        context.update(
            {
                'producty': producty,
                'sklady': sklady,
                'postavki': postavki
            }
        )
        return context
