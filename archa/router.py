'''
This file enables us to use regular views in the router alongside viewsets.
'''

from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSetMixin
from rest_framework.urlpatterns import format_suffix_patterns

class ArchaRouter(DefaultRouter):
    def get_routes(self, view):
        if issubclass(view, ViewSetMixin):
            return super(ArchaRouter, self).get_routes(view)
        return []

    def get_urls(self):
        urls = []
        for prefix, view, basename in self.registry:
            if issubclass(view, ViewSetMixin):
                continue
            urls.append(path(f'{prefix}{self.trailing_slash}', view.as_view(), name=f'{basename}-list'))
        urls = format_suffix_patterns(urls, allowed=['json', 'html'])
        return super(ArchaRouter, self).get_urls() + urls
