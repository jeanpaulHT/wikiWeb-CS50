from django import forms
from django.shortcuts import redirect,render
from django.http import HttpResponse
import markdown2

from . import util

class searchForm(forms.Form):
    article = forms.CharField(label="", widget=forms.TextInput(attrs={
        "class": "search",
        "placeholder":"Search Encyclopedia"}
    ))


class addForm(forms.Form):
    title = forms.CharField(label="", widget=forms.Textarea(attrs={
        "style": "height: 61px;"}
        ))
    text = forms.CharField(label="", widget=forms.Textarea(attrs={
        "style": "height: 500px;"}
        ))

class editForm(forms.Form):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={
        "style": "height: 500px;"}
        ))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": searchForm()
    })

def article(request, article):


    return render(request, f"encyclopedia/article.html", {
        "article": markdown2.markdown(util.get_entry(article)),
        "name": article
    })

def editPage(request,article):
    
    text = util.get_entry(article)

    if text == None:
        return render(request, f"encyclopedia/article.html", {
            "article": util.get_entry(None),
            "name": article
        })

    edit_form = editForm(initial={'text':text})
    edit_form.name = article
    
    return render(request, f"encyclopedia/editPage.html", {
        "name": article,
        "editForm": edit_form
    })

def editArticle(request,article):


    if request.method == "POST":

        form = editForm(request.POST)


        if form.is_valid():

            text = form.cleaned_data["text"]
            util.save_entry(article,text)
            
            return render(request, f"encyclopedia/article.html", {
                "article": util.get_entry(article),
                "name": article
            })

    return render(request, f"encyclopedia/article.html", {
                    "article": util.get_entry(None),
                    "name": article
                    })



def add_page(request):
    return render(request, f"encyclopedia/newPage.html", {
        "addForm": addForm()
    })

def addArticle(request):

    if request.method == "POST":

        form = addForm(request.POST)

        if form.is_valid():

            article = form.cleaned_data["title"]
            text = form.cleaned_data["text"]

            md = util.get_entry(article)

            if md is None:
                util.save_entry(article,text)
            
            else:
                return render(request, f"encyclopedia/article.html", {
                    "article": util.get_entry(None),
                    "name": article
                    })
            
            return render(request, f"encyclopedia/article.html", {
                "article": util.get_entry(article),
                "name": article
            })


    return redirect("/add")

def search(request):

    if request.method == "GET":

        form = searchForm(request.GET)

        if form.is_valid():

            article = form.cleaned_data["article"]
            md = util.get_entry(article)

            if md is None:
                similar = util.getSubString(article)

                return render(request, "encyclopedia/index.html", {
                    "entries": similar,
                    "form": searchForm()
                })

    
            else:
                return render(request, f"encyclopedia/article.html", {
                    "article": md,
                    "name": article
                })


    return redirect("/")

def getRandom(request):
    name  = util.randomTitle()
    print(name)
    
    return render(request, f"encyclopedia/article.html", {
        "article": util.get_entry(name),
        "name": name
    })
