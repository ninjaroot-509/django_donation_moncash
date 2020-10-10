from django.urls import path
from .views import *
# la ou importer toute sa q nan views la

urlpatterns = [
    #dwe creer route nan ap la konnya
    path('', index, name="index"),
    #konnya nap f route pou page donation an
    #wap jis mete yon virgule apre chak path
    path('donate/', donate, name="donate")
]
