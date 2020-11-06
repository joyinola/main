from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Value
from django.db.models.functions import Replace
from .models import User,bidding,comment,product,category
from django.contrib.auth.decorators import login_required

def index(request):
    products=product.objects.all()
    group=category.objects.all()
    

    return render(request, "auctions/index.html", {'products':products,'group':group})
@login_required
def new_bid(request,item_no):
    if request.method=='POST':
        productt=product.objects.get(id=item_no)

        current=request.POST.get('current_bid')
        

        #p=bidding.objects.get(listing=item_no).item_price
        filt=bidding.objects.filter(listing=productt)
        p=filt.latest('item_price').item_price
        #return HttpResponse(p)
        if float(current)<=float(p):
            bid=p
            use=filt.latest('item_price').user
            return render(request,'auctions/item.html',{
            'message':'Bid must be higher than current bid','product':productt,'use':use, 'bid':bid})
        else:

            bidding.objects.create(
                user=request.user,
                item_price=current,
                listing=productt)
            return HttpResponseRedirect(reverse(item, args=(item_no,)))
def item(request,item_id):

    entry=product.objects.get(id=item_id)
    bidd=bidding.objects.filter(listing=entry)
    bids=bidd.latest('item_price')
    active=False
    hightest_bidder=False
    close=False
    #return HttpResponse(bids.item_price)
    if entry.price == bids.item_price:
        
        bid="No bid placed yet"
        use="No user yet"
    else:
        bid=bids.item_price
        #use=bidd.latest('user')
        use=bidd.latest('item_price').user
    commentt=entry.comment.all()
    if request.user==entry.user and entry.is_active:
        active=True
    if request.user==use:
        hightest_bidder=True
    if request.method=='POST':
        commentt=request.POST['comment']
        c=comment.objects.create(user=request.user,comment=commentt)
        
        #comments=comment.objects.all()
        entry.comment.add(c)
        if entry.is_active is False:
            close=True
        commentt=entry.comment.all()
        #return HttpResponse(c)
        #return HttpResponseRedirect(reverse(item,args=(item_id,)))
        return render(request,'auctions/item.html', {'product':entry,'use':use,'closed':close,'bidder':hightest_bidder, 'active':active, 'bid':bid,'comment':commentt})
    
    if entry.is_active is False:
        close=True
    return render(request,'auctions/item.html', {'product':entry,'use':use,'bid':bid,'comment':commentt, 'active':active,
        'closed':close,
        'bidder':hightest_bidder})

    

   # return render(request,'auctions/item.html', {'product':entry,'state':True,'bid':bid,'comment':commentt})        
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
@login_required
def listin(request):

    if request.method=='POST':

        l=request.POST['title']
        i=request.POST['img']
        d=request.POST['description']
        p=request.POST['price']
        c=request.POST['category']
        
        categoryy=category.objects.get(category=c)
        productt=product.objects.create(item=l,img=i,category=categoryy,price=p,description=d,user=request.user)

        price=bidding.objects.create(user=request.user,item_price=p,listing=productt)
        
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'auctions/forms.html')
@login_required 
def watchlist(request,itm_id):
    item=product.objects.get(id=itm_id)
    state=False

    if request.user.watchlist.filter(id=itm_id).exists():
        message='Item already on your watchlist'
        watch=request.user.watchlist.all()
        state=True
        return render(request, 'auctions/index.html', {'watch':watch,'message':message,'state':state})
       # request.user.watchlist.remove(item)

    else:
        request.user.watchlist.add(item)

    watch=request.user.watchlist.all()
    return render(request, 'auctions/index.html', {'watch':watch,'text':'Added to watchlist'
        })
def al_watchlist(request):
    everything=request.user.watchlist.all()
    if not everything:
        return render(request, 'auctions/watchlist.html',{
            'message':'Watchlist is empty'})

    return render(request, 'auctions/watchlist.html',{'everything':everything})

def r_watchlist(request, itm_no):
    everything=request.user.watchlist.all()
    item=product.objects.get(id=itm_no)
    request.user.watchlist.remove(item)
    return render(request, 'auctions/watchlist.html',{'everything':everything,
        'text':'Item has been removed from watchlist'})
def close_bid(request,list_no):
    entry=product.objects.get(id=list_no)
    entry.is_active=False
    entry.save()
    try:
        bid=bidding.objects.filter(listing=entry)
        h_bid=bid.latest('item_price').item_price
    except:
        pass
    return HttpResponseRedirect(reverse(item, args=(list_no,)))
def categories(request,categoryy):
    #cate=category.objects.filter(id=category)
    products=product.objects.all()
    group=category.objects.all()
    section=product.objects.filter(category=categoryy)
    if not section:
        section='No listing present in this category'
    return render(request, 'auctions/index.html',{'section':section,'product':products,'group':group})
    #return render(request,'auctions/index.html',{'category':section})
def my_listing(request):
    my_listing=product.objects.filter(user=request.user)
    return render(request,'auctions/my_listing.html',{'my_listing':my_listing})


    