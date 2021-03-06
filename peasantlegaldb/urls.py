from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views
from . import dal_views

index_urls = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
]

autocomplete_urls = [
    url(r'^person', dal_views.PersonAutocomplete.as_view(),
        name='person'),
    url(r'^village', dal_views.VillageAutocomplete.as_view(),
        name='village')
]

archive_urls = [
    url(r'^list/$', views.ArchiveListView.as_view(template_name='archive/_archive_list.html'),
        name='list'),
    url(r'^(?P<pk>\d+)/$', views.ArchiveDetailView.as_view(template_name='archive/_archive_detail.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/case_list', TemplateView.as_view(template_name='archive/case_list.html'),
        name='cases'),
    url(r'^(?P<pk>\d+)/record_list', TemplateView.as_view(template_name='archive/record_list.html'),
        name='records'),
    url(r'^(?P<pk>\d+)/session_list', TemplateView.as_view(template_name='archive/session_list.html'),
        name='sessions'),
    url(r'^add/$', views.ArchiveAddView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/edit/$', views.ArchiveEditView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.ArchiveDeleteView.as_view(), name='delete'),

]

case_urls = [
    url(r'^list/$', views.CaseListView.as_view(template_name='case/_case_list.html'), name='list'),
    url(r'^(?P<pk>\d+)/$', views.CaseDetailView.as_view(template_name='case/_case_detail.html'), name='detail'),
    url(r'^(?P<pk>\d+)/cornbot$', TemplateView.as_view(template_name='case/cornbot_list.html'), name='cornbot'),
    url(r'^(?P<pk>\d+)/extrahura$', TemplateView.as_view(template_name='case/extrahura_list.html'), name='extrahura'),
    url(r'^(?P<pk>\d+)/land$', TemplateView.as_view(template_name='case/land_list.html'), name='land'),
    url(r'^(?P<pk>\d+)/mentioned$', TemplateView.as_view(template_name='case/mentioned_list.html'), name='mentioned'),
    url(r'^(?P<pk>\d+)/murrain$', TemplateView.as_view(template_name='case/murrain_list.html'), name='murrain'),
    url(r'^(?P<pk>\d+)/pledges$', TemplateView.as_view(template_name='case/pledge_list.html'), name='pledges'),
    url(r'^add/$', views.add_case, name='add'),
    url(r'^(?P<pk>\d+)/edit/$', views.case_edit_view, name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.CaseDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/litigants/$', views.LitigantListforAddCase.as_view(template_name='case/litigant_table_body_for_case.html')
        , name='litigant_list_for_add_case'),
    url(r'^(?P<pk>\d+)/add_litigant/$', views.add_litigant, name='add_litigant'),
    url(r'^ajax/load_case_types/', views.load_case_types, name='ajax_case_types'),
    url(r'^ajax/load_verdict_types/', views.load_verdict_types, name='ajax_verdict_types'),
]

county_urls = [
    url(r'^(?P<pk>\d+)/$', views.CountyDetailView.as_view(template_name='county/_county_detail.html'), name='detail'),
    url(r'^(?P<pk>\d+)/village_list$', TemplateView.as_view(template_name='county/village_list.html'),
        name='villages'),
    url(r'^(?P<pk>\d+)/case_list$', TemplateView.as_view(template_name='county/case_list.html'),
        name='cases'),
    url(r'^(?P<pk>\d+)/resident_list$', TemplateView.as_view(template_name='county/resident_list.html'),
        name='residents'),
    url(r'^(?P<pk>\d+)/litigant_list$', TemplateView.as_view(template_name='county/litigant_list.html'),
        name='litigants'),
    url(r'^(?P<pk>\d+)/hundred_list$', TemplateView.as_view(template_name='county/hundred_list.html'),
        name='hundreds'),
    url(r'^list/$', views.CountyListView.as_view(template_name='county/_county_list.html'),
        name='list'),
]

hundred_urls = [
    url(r'^(?P<pk>\d+)/$', views.HundredDetailView.as_view(template_name='hundred/_hundred_detail.html'), name='detail'),
    url(r'^(?P<pk>\d+)/case_list$', TemplateView.as_view(template_name='hundred/case_list.html'),
        name='cases'),
    url(r'^(?P<pk>\d+)/resident_list$', TemplateView.as_view(template_name='hundred/resident_list.html'),
        name='residents'),
    url(r'^(?P<pk>\d+)/litigant_list$', TemplateView.as_view(template_name='hundred/litigant_list.html'),
        name='litigants'),
    url(r'^(?P<pk>\d+)/village_list$', TemplateView.as_view(template_name='hundred/village_list.html'),
        name='villages'),
    url(r'^list/$', views.HundredListView.as_view(template_name='hundred/_hundred_list.html'),
        name='list'),
]

land_urls = [
    url(r'^(?P<pk>\d+)/$', views.LandDetailView.as_view(template_name='land/_land_detail.html'), name='detail'),
    url(r'^(?P<pk>\d+)/tenants', TemplateView.as_view(template_name='land/tenant_history.html'), name='tenants'),
    url(r'^(?P<pk>\d+)/split_history', TemplateView.as_view(template_name='land/split_history.html'),
        name='split_history'),
    url(r'^(?P<pk>\d+)/case_history', TemplateView.as_view(template_name='land/case_history.html'),
        name='cases'),
]

litigant_urls = [
    url(r'^(?P<pk>\d+)/delete', views.delete_litigant, name='delete'),
    url(r'^(?P<pk>\d+)/edit', views.edit_litigant, name='edit'),
]

person_detail_urls = [
    url(r'^(?P<pk>\d+)/$', views.PersonDetailView.as_view(template_name='person/_person_detail.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/amercement_list', TemplateView.as_view(template_name='person/amercement_list.html'),
        name='amercements'),
    url(r'^(?P<pk>\d+)/case_list', TemplateView.as_view(template_name='person/case_list.html'),
        name='cases'),
    url(r'^(?P<pk>\d+)/capitagium_list', TemplateView.as_view(template_name='person/capitagium_list.html'),
        name='capitagia'),
    url(r'^(?P<pk>\d+)/damage_list', TemplateView.as_view(template_name='person/damage_list.html'),
        name='damages'),
    url(r'^(?P<pk>\d+)/fine_list', TemplateView.as_view(template_name='person/fine_list.html'),
        name='fines'),
    url(r'^(?P<pk>\d+)/heriot_list', TemplateView.as_view(template_name='person/heriot_list.html'),
        name='heriots'),
    url(r'^(?P<pk>\d+)/impercamentum_list', TemplateView.as_view(template_name='person/impercamentum_list.html'),
        name='impercamenta'),
    url(r'^(?P<pk>\d+)/land_list', TemplateView.as_view(template_name='person/land_list.html'),
        name='lands'),
    url(r'^(?P<pk>\d+)/pledges', TemplateView.as_view(template_name='person/pledges_list.html'),
        name='pledges'),
    url(r'^(?P<pk>\d+)/position_list', TemplateView.as_view(template_name='person/position_list.html'),
        name='positions'),
    url(r'^(?P<pk>\d+)/relationship_list', views.RelationshipList.as_view(),
        name='relationships'),
    url(r'^(?P<pk>\d+)/add_relationship/$', views.RelationshipAddView,
        name='add_relationship'),
    url(r'^list/$', views.PeopleListView.as_view(template_name='person/_person_list.html'),
        name='list'),
    url(r'^add/$', views.PersonAddView.as_view(),
        name='add'),
    url(r'^(?P<pk>\d+)/edit', views.PersonEditView.as_view(),
        name='edit'),
    url(r'^(?P<pk>\d+)/delete', views.PersonDeleteView.as_view(),
        name='delete'),
]

record_urls = [
    url(r'^(?P<pk>\d+)/$', views.RecordDetailView.as_view(template_name='record/_record_detail.html'), name='detail'),
    url(r'^(?P<pk>\d+)/session_list.html$', TemplateView.as_view(template_name='record/session_list.html'),
        name='sessions'),
    url(r'^add/$', views.RecordAddView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/edit/$', views.RecordEditView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.RecordDeleteView.as_view(), name='delete'),
    url(r'^list/$', views.RecordListView.as_view(template_name='record/_record_list.html'), name='list'),
]

relationship_urls = [
    url(r'^(?P<pk>\d+)/edit/$', views.RelationshipEditView,
        name='edit'),
]

session_urls = [
    url(r'^list/$', views.SessionListView.as_view(template_name='session/_session_list.html'),
        name='list'),
    url(r'^(?P<pk>\d+)/$', views.SessionDetailView.as_view(template_name='session/_session_detail.html'), name='detail'),
    url(r'^(?P<pk>\d+)/case_list$', TemplateView.as_view(template_name='session/case_list.html'),
        name='cases'),
    url(r'^(?P<pk>\d+)/litigant_list$', TemplateView.as_view(template_name='session/litigant_list.html'),
        name='litigants'),
    url(r'^add/$', views.SessionAddView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/edit/$', views.SessionEditView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.SessionDeleteView.as_view(), name='delete'),
]

village_urls = [
    url(r'^(?P<pk>\d+)/$', views.VillageDetailView.as_view(template_name='village/_village_detail.html'), name='detail'),
    url(r'^(?P<pk>\d+)/case_list$', TemplateView.as_view(template_name='village/case_list.html'),
        name='cases'),
    url(r'^(?P<pk>\d+)/land_list$', TemplateView.as_view(template_name='village/land_list.html'),
        name='lands'),
    url(r'^(?P<pk>\d+)/litigant_list$', TemplateView.as_view(template_name='village/litigant_list.html'),
        name='litigants'),
    url(r'^(?P<pk>\d+)/mentioned_elsewhere$', TemplateView.as_view(
        template_name='village/mentioned_elsewhere_list.html'), name='mentioned_elsewhere'),
    url(r'^(?P<pk>\d+)/mentioned_here$', TemplateView.as_view(template_name='village/mentioned_here.html'),
        name='mentioned_here'),
    url(r'^(?P<pk>\d+)/resident_list$', TemplateView.as_view(template_name='village/resident_list.html'),
        name='residents'),
    url(r'^(?P<pk>\d+)/session_list.html$', TemplateView.as_view(template_name='village/session_list.html'),
        name='sessions'),
    url(r'^list/$', views.VillageListView.as_view(template_name='village/_village_list.html'),
        name='list'),
]

filter_urls = [
    url(r'^$', TemplateView.as_view(template_name='filter/filter.html'), name='main'),
    url(r'^people$', views.PeopleFilterView.as_view(), name='people'),
    url(r'^people/table', views.people_filter_table_view, name='people_table'),
    url(r'^cases$', views.CaseFilterView.as_view(), name='cases'),
    url(r'^cases/table', views.cases_filter_table_view, name='cases_table'),
    url(r'^counties$', views.CountyFilterView.as_view(), name='counties'),
    url(r'^counties/table', views.counties_filter_table_view, name='counties_table'),
    url(r'^hundreds$', views.HundredFilterView.as_view(), name='hundreds'),
    url(r'^hundreds/table', views.hundreds_filter_table_view, name='hundreds_table'),
    url(r'^villages$', views.VillageFilterView.as_view(), name='villages'),
    url(r'^villages/table', views.villages_filter_table_view, name='villages_table'),
    url(r'^archives$', views.ArchiveFilterView.as_view(), name='archives'),
    url(r'^records$', views.RecordFilterView.as_view(), name='records'),
    url(r'^records/table', views.records_filter_table_view, name='records_table'),
    url(r'^sessions$', views.SessionFilterView.as_view(), name='sessions'),
    url(r'^sessions/table', views.sessions_filter_table_view, name='sessions_table'),
]

# consolidation of detail views.
urlpatterns = [
    url(r'^', include(index_urls)),
    url(r'^filter/', include(filter_urls, namespace='filter')),
    url(r'^archive/', include(archive_urls, namespace='archive')),
    url(r'^case/', include(case_urls, namespace='case')),
    url(r'^county/', include(county_urls, namespace='county')),
    url(r'^hundred/', include(hundred_urls, namespace='hundred')),
    url(r'^land/', include(land_urls, namespace='land')),
    url(r'^litigant/', include(litigant_urls, namespace='litigant')),
    url(r'^person/', include(person_detail_urls, namespace='person')),
    url(r'^record/', include(record_urls, namespace='record')),
    url(r'^session/', include(session_urls, namespace='session')),
    url(r'^village/', include(village_urls, namespace='village')),
    url(r'^relationship/', include(relationship_urls, namespace='relationship')),
    url(r'^case_test/', views.nested_test),
    url(r'^autocomplete/', include(autocomplete_urls, namespace='autocomplete')),
    url(r'^relationship_fix/', TemplateView.as_view(template_name='analysis/relationships.html')),
    url(r'^currency_converter/', views.currency_conversion, name='currency_converter')
]
