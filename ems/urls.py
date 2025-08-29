from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls
