from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'Application2.views.home', name='home'),
    url(r'^exec_req/$', 'Application2.views.exec_req', name='home'),
]