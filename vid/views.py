from django.shortcuts import render, redirect, get_object_or_404
from .models import Item,Detail,Comment
from django.http import Http404, HttpResponse
from django.db.models import Q
from .forms import CommentForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
# Create your views here.
# THIS FUNCTION RETURNS THE VIDEO EMBEDDING REQUEST
@login_required
def video(request):
    obj = Item.objects.all()
    return render(request,'video.html',{'obj':obj})

# THIS FUNCTION RETURNS THE PAYMENT REQUEST
# @login_required   
def payment(request, title):
    school = get_object_or_404(Detail, pk=title)
    return render(request,'payment.html',{'school': school})

# THIS FUNCTION RETURNS THE THUMBNAIL REQUESTS ie THE HOME PAGE OF A USER

def thumbnail(request):
    obj2 = Detail.objects.all()
    return render (request,'thumbnail.html',{'obj2':obj2})

# THIS FUNCTION RENDERS THE PAGE TO CORRESPONDING VIDEO PLAYER FOR THE SELECTED THUMBNAIL

def vidDetails(request, title):
    school = get_object_or_404(Detail, pk=title)
    return render(request, 'show.html', {'school': school})

# THIS FUNCTION IMPLEMENTS THE SEARCH FEATURE
@login_required
def search(request):
    query=None
    results=[]
    if request.method=="GET":
        query=request.GET.get('search')
        results=Detail.objects.filter(Q(title__icontains=query) | Q(des__icontains=query) )
    return  render(request,'search.html',{'query': query,
                                          'results': results}) 
@login_required
def comment(request,title):
        comm = request.POST("comment")
        com2 = Comment.objects.all.filter(pk = title)
        com2.content = comm
        if com2.is_valid:
            comm2.save()
            return HttpResponse(resp)
        else:
           return HttpResponse('NOt Done')

