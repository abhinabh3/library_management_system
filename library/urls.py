from django.urls import path, include
from .views import CategoryViewset,AuthorViewset,BooksViewset,login,register
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("category/",CategoryViewset.as_view({"get":"list", "post":"create"})),
    path("category/<int:pk>",CategoryViewset.as_view({"put":"update","delete":"destroy","get":"retrieve"})),

    path("author/",AuthorViewset.as_view({"get":"list", "post":"create"})),
    path("author/<int:pk>",AuthorViewset.as_view({"put":"update","delete":"destroy","get":"retrieve"})),
    path("books/",BooksViewset.as_view({"get":"list", "post":"create"})),
    path("books/<int:pk>",BooksViewset.as_view({"put":"update","delete":"destroy","get":"retrieve"})),
    path("login/",login),
    path("register/",register)
    

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)