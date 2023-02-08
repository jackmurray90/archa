from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSetMixin
from rest_framework.urlpatterns import format_suffix_patterns

class ArchaRouter(DefaultRouter):
    def get_routes(self, viewset):
        if issubclass(viewset, ViewSetMixin):
            return super(ArchaRouter, self).get_routes(viewset)
        return []

    def get_urls(self):
        urls = []
        for prefix, viewset, basename in self.registry:
            if issubclass(viewset, ViewSetMixin):
                continue
            urls.append(path(f'{prefix}{self.trailing_slash}', viewset.as_view(), name=f'{basename}-list'))
        urls = format_suffix_patterns(urls, allowed=['json', 'html'])
        return super(ArchaRouter, self).get_urls() + urls
