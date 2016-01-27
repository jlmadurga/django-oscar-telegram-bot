from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns

from oscar.app import application

urlpatterns = patterns(
    '',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^telegrambot/', include('telegrambot.urls', namespace='telegrambot')),
)
urlpatterns += i18n_patterns(
    '',
    (r'', include(application.urls)),
)