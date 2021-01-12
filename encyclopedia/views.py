from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, article):
    return render(request, f"encyclopedia/article.html", {
        "article": util.get_entry(article),
        "name": article
    })