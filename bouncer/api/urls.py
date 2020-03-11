from bouncer.views import notfound
from django.urls import path, re_path
from .views.jhipster.jhipster_view import JhipsterView


urlpatterns = [
    path('jhipster', JhipsterView.as_view(), name='jhipster_view'),
    re_path(r'^(?:.*)$', notfound)
]

