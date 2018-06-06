
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^create/', views.createItemView,name='create'),
    url(r'^contact/', views.contact,name='contact'),
    url(r'^manage/$',views.ManageProfile,name='manage'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^about/$',views.about,name='about'),
    url(r'^showItem/$',views.showItem.as_view(),name='showItem'),
    url(r'^itemDetail/(?P<pk>\d+)/$',views.itemDetail.as_view(),name='itemDetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)