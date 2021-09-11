from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='streamplatform'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform_detail')
]
    