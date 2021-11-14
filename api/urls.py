from rest_framework import routers
from .views import ArticlesView, TopBackView, FormbackView, FormView, BlogPostViewSet, BlogCategoryViewSet
from django.urls import path


urlpatterns = [
    path('articles/', ArticlesView.as_view()),
]


router = routers.SimpleRouter()
router.register('topback', TopBackView ,basename = 'topback')
urlpatterns += router.urls


router = routers.SimpleRouter()
router.register('formback', FormbackView ,basename = 'Formback')
router.register('category', BlogCategoryViewSet, basename = 'category' )
urlpatterns += router.urls


router = routers.SimpleRouter()
router.register('form', FormView ,basename = 'Form')
urlpatterns += router.urls


router = routers.SimpleRouter()
router.register('blog', BlogPostViewSet ,basename = 'blog')
urlpatterns += router.urls
