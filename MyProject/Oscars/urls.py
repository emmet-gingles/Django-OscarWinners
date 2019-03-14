from django.conf.urls import url		# For URL patterns
from django.contrib import admin		# For admin login
from Oscars.views import *				# Import views from file

# List of valid URL patterns. Each pattern corresponds to a view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^actor/winners', showActorWinners ),
	url(r'^actor/nominees', showActorNominees ),
	url(r'^actor/', showActorWinners ),
	url(r'^actress/winners', showActressWinners ),
	url(r'^actress/nominees', showActressNominees ),
	url(r'^actress/', showActressWinners ),
	url(r'^supportingactor/winners', showSupportingActorWinners ),
	url(r'^supportingactor/nominees', showSupportingActorNominees ),
	url(r'^supportingactor/', showSupportingActorWinners ),
	url(r'^supportingactress/winners', showSupportingActressWinners ),
	url(r'^supportingactress/nominees', showSupportingActressNominees ),
	url(r'^supportingactress/', showSupportingActressWinners ),	
	url(r'^director/winners', showDirectorWinners ),
	url(r'^director/nominees', showDirectorNominees ),
	url(r'^director/', showDirectorWinners ),
	url(r'^picture/winners', showPictureWinners ),
	url(r'^picture/nominees', showPictureNominees ),
	url(r'^picture/', showPictureWinners ),
	url(r'^winners/year/(?P<year>\d{4})/$', showYear ),						# Example: winners/year/2018		
	url(r'^nominees/year/(?P<year>\d{4})/$', showYear ),					# Example: nominees/year/2018
	url(r'^search/actor/(?P<search>[\w\-]+)/$', searchActor ),				# Example: search/actor/tom_hanks
	url(r'^search/actress/(?P<search>[\w\-]+)/$', searchActress ),			# Example:	search/actress/meryl_streep
	url(r'^search/director/(?P<search>[\w\-]+)/$', searchDirector ),		# Example: search/director/steven_spielberg
	url(r'^nominations/actor', showActorsByNomination ),
	url(r'^nominations/actress', showActressesByNomination ),
	url(r'^nominations/director', showDirectorsByNomination ),
	url(r'^wins/actor', showActorsByWins ),
	url(r'^wins/actress', showActressesByWins ),
	url(r'^wins/director', showDirectorsByWins ),
]
