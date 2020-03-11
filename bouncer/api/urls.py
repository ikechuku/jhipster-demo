from bouncer.views import notfound
from django.urls import path, re_path
from .views.jhipster.jhipster_view import JhipsterView

urlpatterns = [
    # register other routes here ...
    path('jhipster', JhipsterView.as_view(), name='jhipster_view'),
    # match route that has not been registered above
    re_path(r'^(?:.*)$', notfound)
]
