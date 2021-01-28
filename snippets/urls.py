from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #path('language/', views.language, name='language'),
    path('usuario/', views.snippets_user, name='snippets_user'),
    path('añadir/', views.añadir_snippets, name='añadir'),
    path('category/python', views.CategoryPython, name='category_python'),
    path('category/java', views.CategoryJava, name='category_java'),
    path('category/c++', views.CategoryC, name='category_c'),
    path('category/html', views.CategoryHTML, name='category_html'),     
    path('edit/<int:snippet_id>', views.snippet_edit, name='snippet_edit'),
    path('delete/<int:snippet_id>', views.snippet_delete, name='snippet_delete'),
    path('detail/<int:snippet_id>', views.detail, name='detail')
]