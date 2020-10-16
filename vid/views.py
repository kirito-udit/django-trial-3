from django.shortcuts import render, redirect, get_object_or_404
from .models import Item,Detail,Comment
from django.http import Http404, HttpResponse, JsonResponse
from django.db.models import Q
from .forms import CommentForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
# Create your views here.
# THIS FUNCTION RETURNS THE VIDEO EMBEDDING REQUEST
@login_required
def video(request):
    obj = Item.objects.all()
    return render(request,'video.html',{'obj':obj})

# THIS FUNCTION RETURNS THE PAYMENT REQUEST
@login_required   
def payment(request, title):
    school = get_object_or_404(Detail, pk=title)
    return render(request,'payment.html',{'school': school})

# THIS FUNCTION RETURNS THE THUMBNAIL REQUESTS ie THE HOME PAGE OF A USER
@login_required
def thumbnail(request):
    obj2 = Detail.objects.all()
    return render (request,'thumbnail.html',{'obj2':obj2})

# THIS FUNCTION RENDERS THE PAGE TO CORRESPONDING VIDEO PLAYER FOR THE SELECTED THUMBNAIL
@login_required
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
def likepost(request, title):
    post = get_object_or_404(Detail,pk = title)
    is_liked = False
    if (post.likers.filter(username = request.user.username).exists()):
        post.likers.remove(request.user)
        is_liked = False
    else:
        post.likers.add(request.user)
        is_liked = True

    context = {
        'is_liked' : is_liked,
        'school' : post
    }
    html = render_to_string('like.html',context, request = request)
    return JsonResponse({'like':html})

def vidplay(request, title):
    school = get_object_or_404(Detail, pk=title)
    return render(request, 'player.html', {'school': school})


@login_required
def reportpost(request, title):
    post = get_object_or_404(Detail,pk = title)
    is_reported = False
    if (post.reporters.filter(username = request.user.username).exists()):
        post.reporters.remove(request.user)
        is_reported = False
    else:
        post.reporters.add(request.user)
        is_reported = True

    context = {
        'is_reported' : is_reported,
        'school' : post
    }
    html = render_to_string('report.html',context, request = request)
    return JsonResponse({'report':html})

@login_required
def commentpost(request, title):
    post = get_object_or_404(Comment,pk = title)
    is_commented = False
    if (post.commenters.filter(username = request.user.username).exists()):
        post.commenters.remove(request.user)
        is_commented = False
    else:
        post.commenters.add(request.user)
        is_commented = True

    context = {
        'is_commented' : is_commented,
        'school' : post
    }
    html = render_to_string('comment.html',context, request = request)
    return JsonResponse({'comment':html})