from django.shortcuts import render
from .models import Item
from django.contrib import messages
from django.http import HttpResponse
from .forms import Itemforms

# Create your views here.
def item_list(request):
    showall = Item.objects.all()
    return render(request,'index.html',{"data": showall})


def form_display(request):
    if request.method == "POST":
        if request.POST.get('itemname') and request.POST.get('amount') and request.POST.get('bought_from') and request.POST.get('bought_on') and request.POST.get('price') and request.POST.get('gst_applied') and request.POST.get('image') and request.POST.get('ref'):
            saverecord = Item()
            saverecord.itemname = request.POST.get('itemname')
            saverecord.amount = request.POST.get('amount')
            saverecord.bought_from = request.POST.get('bought_from')
            saverecord.bought_on = request.POST.get('bought_on')
            saverecord.price = request.POST.get('price')
            saverecord.gst_applied = request.POST.get('gst_applied')
            saverecord.ref = request.POST.get('ref')
            saverecord.image = request.POST.get('image')
            saverecord.save()

            messages.success(request,'Item '+saverecord.itemname+' has been added successfully!')
            return render(request,'form.html')

    else:
        return render(request,'form.html')

    
def Edit_item(request,id):
    Edit_item_obj = Item.objects.get(id=id)
    return render(request,'Edit.html',{"Item":Edit_item_obj})

def Update_item(request,id):
    Update_item_obj = Item.objects.get(id=id)
    form=Itemforms(request.POST,instance=Update_item_obj)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updated successfully!')
        return render(request,'Edit.html',{"Item":Update_item_obj})
    

def Delete_item(request,id):
    Delete_item_obj = Item.objects.get(id=id)
    Delete_item_obj.delete()
    showdata = Item.objects.all
    return render(request,'Index.html',{"data":showdata})

