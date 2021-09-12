from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='streamplatform'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform_detail'),
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')
]
    