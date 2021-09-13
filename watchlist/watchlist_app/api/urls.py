from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchDetailAV,
                                     StreamPlatformAV, StreamPlatformDetailAV,
                                     ReviewList, ReviewDetail, StreamPlatformVS)


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch_detail'),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='streamplatform'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(),
    #      name='streamplatform_detail'),

    path('stream/<int:pk>/review/', ReviewList.as_view(),
         name='streamplatform_detail'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

]
 