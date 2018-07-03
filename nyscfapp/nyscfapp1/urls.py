# howdy/urls.py
from django.conf.urls import url
from django.urls import path
from nyscfapp1 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^hank/$', views.HankPageView.as_view(), name = 'hank'), # Add this /Hank/ route
    url(r'^nyscf_home/$', views.NYSCFHomeView.as_view(), name='NYSCFHomeView'), # Add this /Hank/ route
    url(r'^nyscf_filers/$', views.NYSCFFilerView.as_view(), name='filers'),
    url(r'^nyscf_filers_filter/$', views.NYSCFFilerFilterView.as_view(), name='filers_filter'),
    url(r'^nyscf_contributions_filter/$', views.NYSCFContributionFilterView.as_view(), name='contributions_filter'),
    url(r'^nyscf_filers_detail/(?P<slug>\w+)$', views.NYSCFFilerDetailView.as_view(), name='filers_detail'),
    url(r'^nyscf_filers_detail2/(?P<slug>\w+)$', views.NYSCFFilerDetail2View.as_view(), name='filers_detail2'),
    url(r'^$', views.dex, name='dex'),
    url(r'^api/chart/data/$', views.ChartData.as_view(), name='api-chart-data'),
    url(r'^dashboard/api/chart/data/$', views.ChartDataView.as_view(), name='chart-data-view'),
    url(r'^api/contbyfiler/data/$', views.ContByFilerAPIData.as_view(), name='api-cont-by-filer-data'),
    url(r'^nyscf_filers_detail/(?P<slug>\w+)/chart_year/$', views.ChartContribByYearView.as_view(), name='chart-cont-by-year-data-view'),
    url(r'^nyscf_filers_detail/(?P<slug>\w+)/chart_state/$', views.ChartContribByStateView.as_view(), name='chart-cont-by-state-data-view'),
    # ex: /polls/5/ ChartContribByYearView
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]

