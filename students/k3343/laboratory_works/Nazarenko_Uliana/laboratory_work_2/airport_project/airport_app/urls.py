from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

app_name = "airport_app"

urlpatterns = [
	path('auth/', include('djoser.urls')),
	path('auth/token', obtain_auth_token, name='token'),

	path('flights/', FlightsView.as_view()),
	path('flights/<int:pk>', FlightView.as_view()),

	path('companies/', CompanysView.as_view()),
	path('companies/<int:pk>', CompanyView.as_view()),

	path('planes/', PlanesView.as_view()),
	path('planes/<int:pk>', PlaneView.as_view()),

	path('flights/transit/', TransitLandingsView.as_view()),
	path('flights/transit/<int:pk>', TransitLandingView.as_view()),

	path('flights/arrival/', ArrivalDeparturesView.as_view()),
	path('flights/arrival/<int:pk>', ArrivalDepartureView.as_view()),

	path('companies/workers/', WorkersView.as_view()),
	path('companies/workers/<int:pk>', WorkerView.as_view()),

	path('flights/crew/', CrewsView.as_view()),
	path('flights/crew/<int:pk>', CrewView.as_view()),

	path('challengers/', ChallengerView.as_view()),
]