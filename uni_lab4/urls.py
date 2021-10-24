from django.contrib import admin
from django.urls import path, include

from forms.views import MainView, AnalyticPage, ForecastPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='home'),
    path('analytic', AnalyticPage.as_view(), name='analytic'),
    path('accounts/', include('accounts.urls')),
    path('forecast', ForecastPage.as_view(), name='forecast'),
]
