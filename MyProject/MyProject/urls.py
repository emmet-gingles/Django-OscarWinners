from django.conf.urls import url, include
from django.contrib import admin
from Oscars import urls as oscar_urls		# Import urls.py from Oscars app as variable

# URL patterns includes all URLs from Oscar app
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^oscars/', include(oscar_urls)),
]
