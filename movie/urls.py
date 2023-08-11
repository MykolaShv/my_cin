from django.urls import path

from .views import about, session_search, soon_list, buy_ticket, ticket_detail, ticket_list, ticket_create, \
    print_ticket, CreateHallView, HallDetailView, HallListView, HallEditView, HallDeleteView, \
    ReleaseDeleteView, ReleaseEditView, ReleaseDetailView, ReleaseListView, \
    CreateReleaseView, CreateSessionView, SessionListView, SessionDetailView, SessionEditView, SessionDeleteView

urlpatterns = [
    path('about/', about, name='about'),
    path('hall/create/', CreateHallView.as_view(), name='hall_create'),
    path('hall/update/<int:pk>/', HallEditView.as_view(), name='hall_update'),
    path('hall/delete/<int:pk>/', HallDeleteView.as_view(), name='hall_delete'),
    path('hall/list/', HallListView.as_view(), name='hall_list'),
    path('hall/detail/<int:pk>/', HallDetailView.as_view(), name='hall_detail'),
    path('session/create/', CreateSessionView.as_view(), name='session_create'),
    path('session/list/', SessionListView.as_view(), name='session_list'),
    path('session/<int:pk>/', SessionDetailView.as_view(), name='session_detail'),
    path('session/update/<int:pk>/', SessionEditView.as_view(), name='session_update'),
    path('session/delete/<int:pk>/', SessionDeleteView.as_view(), name='session_delete'),
    path('session/search/', session_search, name='session_search'),
    path('release/create/', CreateReleaseView.as_view(), name='release_create'),
    path('release/list/', ReleaseListView.as_view(), name='release_list'),
    path('release/edit/<int:pk>/', ReleaseEditView.as_view(), name='release_edit'),
    path('release/detail/<int:pk>/', ReleaseDetailView.as_view(), name='release_detail'),
    path('release/delete/<int:pk>/', ReleaseDeleteView.as_view(), name='release_delete'),
    path('soon/', soon_list, name='soon'),
    path('session_time/<int:session_id>/buy_ticket/', buy_ticket, name='buy_ticket'),
    path('ticket/<int:pk>/', ticket_detail, name='ticket_detail'),
    path('ticket/list/', ticket_list, name='ticket_list'),
    path('ticket/create/', ticket_create, name='ticket_create'),
    path('print_ticket/', print_ticket, name='print_ticket'),
]
