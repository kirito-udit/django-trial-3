from django.shortcuts import render, redirect, get_object_or_404
from .models import Item,Comment,Detail
from django.http import Http404 
from django.db.models import Q
# Create your views here.
def video(request):
    obj = Item.objects.all()
    return render(request,'video.html',{'obj':obj})

def comment(request):
    comment = Comment.objects.all()
    return render(request,'video.html',{'comment':comment})
   
def payment(request):
    return render(request,'payment.html')

def thumbnail(request):
    obj2 = Detail.objects.all()
    return render (request,'thumbnail.html',{'obj2':obj2})

def vidDetails(request, title):
    #school = Detail.objects.get(pk=title)
    school = get_object_or_404(Detail, pk=title)
   # except school.DoesNotExist:
        #raise Http404
    return render(request, 'show.html', {'school': school})

def story_detail(request,id):
    story=get_object_or_404(Detail,id=id)
    return render(request,'thumbnail.html',{'story':story})
def search(request):
    query=None
    results=[]
    if request.method=="GET":
        query=request.GET.get('search')
        results=Detail.objects.filter(Q(title__icontains=query) | Q(des__icontains=query) )
    return  render(request,'search.html',{'query': query,
                                          'results': results}) 