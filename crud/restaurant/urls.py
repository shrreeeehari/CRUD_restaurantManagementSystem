from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.item_list),
    path('form/',views.form_display,name="form_display"),
    path('list/',views.item_list, name="item_list"),
    path('Edit/<int:id>',views.Edit_item,name="Edit_item"),
    path('list/Edit/<int:id>',views.Edit_item, name="Edit_item"),
    path('Update/<int:id>',views.Update_item,name="Update_item"),
    path('Delete/<int:id>',views.Delete_item,name="Delete_item"),
    path('Delete/<int:id>',views.Delete_item,name="Delete_item"),
    path('Delete/Delete/<int:id>',views.Delete_item,name="Delete_item")
]