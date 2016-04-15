from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import models
from django.contrib import auth
from django.contrib import comments
# from gluon.contrib.pymysql.constants.ER import USERNAME


# Create your views here.
def index(request):
    print request.user
    bbs_list = models.BBS.objects.all()
    return render_to_response('index.html', {
                                            'bbs_list': bbs_list,
                                            'user': request.user,
					    'home_page': True 
                                             })


def bbs_detail(request, bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    return render_to_response('bbs_detail.html', {'bbs_obj':bbs, "user":request.user})


def sub_comment(request):
    bbs_id =  request.POST.get("bbs_id")
    comment = request.POST.get('comment_content')
 
    comments.models.Comment.objects.create(
                                         content_type_id = 7,
                                         object_pk = bbs_id,
                                         site_id = 1,
                                         user = request.user,
                                        comment = comment,
                                         )

    return  HttpResponseRedirect('/detail/%s' % bbs_id )


def remove(request):
    bbs_id = request.GET.get('bbs_id')
    bbs = models.BBS.objects.get(id=bbs_id)
    q = bbs.delete()
    return HttpResponse( 'OK' ) 
    print q

###############################below is user renzheng system#############################
def account_login(request):
    print request.GET
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = auth.authenticate(username=username, password=password)
    print user
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html', {"login_err" : "wrong username or password "})
        
def logout_views(request):
    user = request.user
    print user
    auth.logout(request)
    return  HttpResponseRedirect('/login');

#    return HttpResponse("<b>%s</b>  logged out!  <br> <a href='/login'>Re_login</a>" % user)

def login(request):
    return render_to_response('login.html')



########################bbs content making and publish##########################
def pub(request):
       print request
       return render_to_response('pub.html', { "user": request.user })

def bbs_sub(request):
    print "====>" , request.POST
    title = request.POST.get('title')
    summary = request.POST.get('summary') or "web"
    content = request.POST.get('content')
    author = models.Bbs_User.objects.get(user__username=request.user)
    
    models.BBS.objects.create(
    	title = title,
    	summary = summary,
    	content = content,
    	author = author,
        view_count = 1,
        ranking = 1,
    )
#    return HttpResponse('YES')
    return  HttpResponseRedirect('/');
    

