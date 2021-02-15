
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView,ArticalDetailView,AddPost,UpdatePost,DeletePost,AddCategoryView,CategoryView,LikeView,AddComment,ProjectView,AddProject,Aboutus,Contactus,Customers,Privacy,Terms

urlpatterns = [
    # path('',home,name="home"),
    path('',HomeView.as_view(),name = 'home'),
    path('artical/<int:pk>',ArticalDetailView.as_view(),name = 'artical-detail'),
    path('addpost/',AddPost.as_view(),name = 'add-post'),
    path('addcategory/',AddCategoryView.as_view(),name = 'add-category'),
    path('artical/edit/<int:pk>',UpdatePost.as_view(),name = 'update-post'),
    path('artical/<int:pk>/delete',DeletePost.as_view(),name = 'delete-post'),
    path('category/<str:cats>/',CategoryView,name = 'category'),
    path('like/<int:pk>',LikeView,name = 'like_post'),
    path('artical/<int:pk>/comment',AddComment.as_view(),name = 'add-comment'),
    path('project/',ProjectView.as_view(),name = 'projects'),
    path('addproject/',AddProject.as_view(),name = 'add-project'),
    path('aboutus/',Aboutus,name = 'about-us'),
    path('contactus/',Contactus.as_view(),name = 'contact-us'),
    path('customers/',Customers,name = 'customers'),
    path('privary/',Privacy,name = 'privacy'),
    path('terms/',Terms,name = 'terms'),
    

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)