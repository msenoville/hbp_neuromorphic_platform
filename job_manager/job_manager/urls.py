"""Job manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


from simqueue import views

# tastypie resource exposition
from tastypie.api import Api
from simqueue.api.resources import ResultsResource
from simqueue.api.resources import QueueResource
from simqueue.api.resources import DataItemResource
from simqueue.api.resources import LogResource
from simqueue.api.resources import (JobCountResource,
                                    CumulativeJobCountResource,
                                    CumulativeUserCountResource,
                                    QueueLength,
                                    JobDuration,
                                    ActiveUserCountResource,
                                    ProjectCountResource,
                                    QuotaUsageResource)

admin.autodiscover()

# instance
api = Api(api_name='v2')
api.register(ResultsResource())
api.register(QueueResource())
api.register(DataItemResource())
api.register(LogResource())
api.register(JobCountResource())
api.register(CumulativeJobCountResource())
api.register(CumulativeUserCountResource())
api.register(QueueLength())
api.register(JobDuration())
api.register(ActiveUserCountResource())
api.register(ProjectCountResource())
api.register(QuotaUsageResource())


urlpatterns = (
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^app/', views.home),
    url(r'^api/', include(api.urls)),
    url(r'^config.json$', views.config, name='config'),
    url(r'^copydata/(?P<target>\w+)/(?P<job_id>\d+)$', views.copy_datafiles_to_storage, name="copydata"),
    url(r'^dashboard/', TemplateView.as_view(template_name='dashboard.html')),
)