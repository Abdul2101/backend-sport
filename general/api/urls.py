from rest_framework.routers import DefaultRouter
from .views import LeagueViewSet, MatchViewSet, EventViewSet

router = DefaultRouter()
router.register(r'leagues', LeagueViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'events', EventViewSet)

urlpatterns = router.urls
