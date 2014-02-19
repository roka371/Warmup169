from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warmup169.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.show'),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^users/add$', 'main.views.add'),
    url(r'^users/login$', 'main.views.login'),
    url(r'^welcome/(\d+)$', 'main.views.welcome'),
    url(r'^TESTAPI/resetFixture$', 'main.views.TESTAPI_resetFixture'),
    url(r'^TESTAPI/unitTests$', 'main.views.test'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
