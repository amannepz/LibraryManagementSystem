from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from LBapp.forms import NewBookForm,searchform,issuebookform,returnbookform
from LBapp import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/LBapp/login/")
def newbook(request):
    form=NewBookForm()
    res=render(request,'LBapp/new_book.html',{'form':form})
    return res
def addbook(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.book()
        book.name=form.data['name']
        book.booknumber=form.data['number']
        book.author=form.data['author']
        book.date=form.data['date']
        book.price=form.data['price']
        book.quantity=form.data['quantity']
        book.save()
    s="<h1>Book Added Succesfully in library</h1><a href='/LBapp/add-book'>Back</a> "
    return HttpResponse(s)
@login_required(login_url="/LBapp/login/")
def viewbook(request):
    books=models.book.objects.all()
    res=render(request,'LBapp/view_book.html',{'books':books})
    return res
def editbook(request):
    book=models.book.objects.get(id=request.GET['bookid'])
    fields={'name':book.name,'number':book.booknumber,'author':book.author,'date':book.date,'price':book.price,'quantity':book.quantity}
    form=NewBookForm(initial=fields)
    res=render(request,'LBapp/edit_book.html',{'form':form,'book':book})
    return res
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.book()
        book.id=request.POST['bookid']
        book.name=form.data['name']
        book.booknumber=form.data['number']
        book.author=form.data['author']
        book.date=form.data['date']
        book.price=form.data['price']
        book.quantity=form.data['quantity']
        book.save()
    return HttpResponseRedirect('LBapp/view-book')
def deletebook(request):
    bookid=request.GET['bookid']
    book=models.book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('LBapp/view-book')

@login_required(login_url="/LBapp/login/")
def searchbook(request):
    form=searchform()
    res=render(request,'LBapp/search_book.html',{'form':form})
    return res
def search(request):
    form=searchform(request.POST)
    books=models.book.objects.filter(name=form.data['name'])
    res=render(request,'LBapp/search_book.html',{'form':form,'books':books})
    return res
def userlogin(request):
    data={}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/LBapp/view-book/')
        else:
            data['error']="Username or Password is incorrect"
            res=render(request,'LBapp/user_loginform.html',data)
            return res
    else:
        return render(request,'LBapp/user_loginform.html',data)
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/LBapp/login/')
def logintype(request):
    message="Choose your login type"
    res=render(request,'LBapp/chooselogintype.html',{'message':message})
    return res
def IssueBook(request):
    book=models.book.objects.get(id=request.GET['bookid'])
    fields={'bnumber':book.booknumber,'bname':book.name,'author':book.author,'aquantity':book.quantity}
    form=issuebookform(initial=fields)
    res=render(request,'LBapp/issue_book.html',{'form':form,'book':book})
    return res
def Issue(request):
    if request.method=='POST':
        book=models.book.objects.get(id=request.POST['bookid'])
        form=issuebookform(request.POST)
        std=models.issuebook()
        std.studentid=form.data['studentid']
        std.sname=form.data['sname']
        std.bookname=form.data['bname']
        std.booknumber=form.data['bnumber']
        std.author=form.data['author']
        std.issuedate=form.data['issuedate']
        std.returndate=form.data['returndate']
        std.aquantity=book.quantity-1
        std.save()
        book.quantity=book.quantity-1
        book.save()
    s="<h2>Book Issued Succesfully</h2><br><a href='/LBapp/show-detail'>View Issue Details</a>"
    return HttpResponse(s)
def showdetail(request):
    students=models.issuebook.objects.all()
    book=models.book.objects.all()
    res=render(request,'LBapp/view_issuedetail.html',{'students':students,'book':book})
    return res
def editissuebook(request):
    obj=models.issuebook.objects.get(id=request.GET['issuebookid'])
    fields={'studentid':obj.studentid,'sname':obj.sname,'bnumber':obj.booknumber,'bname':obj.bookname,'author':obj.author,
    'issuedate':obj.issuedate,'returndate':obj.returndate,'aquantity':obj.aquantity}
    form=issuebookform(initial=fields)
    res=render(request,'LBapp/edit_issuebook.html',{'form':form,'obj':obj})
    return res
def updateissue(request):
    if request.method=='POST':
        form=issuebookform(request.POST)
        sobj=models.issuebook()
        sobj.id=request.POST['sid']
        sobj.studentid=form.data['studentid']
        sobj.sname=form.data['sname']
        sobj.booknumber=form.data['bnumber']
        sobj.bookname=form.data['bname']
        sobj.author=form.data['author']
        sobj.issuedate=form.data['issuedate']
        sobj.returndate=form.data['returndate']
        sobj.aquantity=form.data['aquantity']
        sobj.save()
    return HttpResponseRedirect('/LBapp/show-detail')
def returnissue(request):
    book=models.issuebook.objects.get(id=request.GET['bookid'])
    fields={'studentid':book.studentid,'sname':book.sname,'bnumber':book.booknumber,'bname':book.bookname,'author':book.author,'issuedate':book.issuedate,'returningdate':book.returndate}
    form=returnbookform(initial=fields)
    res=render(request,'LBapp/return_book.html',{'form':form,'book':book})
    return res
def returnbook(request):
    if request.method=='POST':
        book=models.issuebook.objects.filter(id=request.POST['bookid'])
        book.delete()
        form=returnbookform(request.POST)
        std=models.returnbook()
        std.studentid=form.data['studentid']
        std.sname=form.data['sname']
        std.booknumber=form.data['bnumber']
        std.bookname=form.data['bname']
        std.author=form.data['author']
        std.issuedate=form.data['issuedate']
        std.returningdate=form.data['returningdate']
        std.returneddate=form.data['returneddate']
        std.latefee=form.data['latefee']
        std.save()
    s="<h2>Book Returned Succesfully</h2><br><a href='/LBapp/show-detail'>View Issue Details</a>"
    return HttpResponse(s)
#def userlogin(request):
#    return render(request,'LBapp/user_loginform.html')
#def adminlogin(request):
#    return render(request,'LBapp/admin_loginform.html')
#def choosetype(request):
#    return render(request,'LBapp/choosetype.html')
