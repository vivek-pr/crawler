from django.shortcuts import render
from .utils import *
from .models import Content, Source, Media
from datetime import datetime
from django.core.validators import URLValidator

def home(request):
    contents = Content.objects.prefetch_related('media_set').all()
    return render(request, 'home.html', {"contents":contents})


def search(request):
    url = request.GET.get("search")
    try:
        if url and URLValidator(url):
            crawl_website(url)
    except:
        pass

    contents = Content.objects.prefetch_related('media_set').all()
    return render(request, 'home.html', {"contents": contents})


def crawl_website(url):
    """
    For provided url from frontend beutifull soup help us in fetching the content
    :param request:
    :return:
    """
    page = get_page(url)
    source, created = Source.objects.get_or_create(url=url)
    source.last_sync = datetime.now()
    source.save()
    properties = get_properties(page)
    title = properties[0][:49].replace("\n", " ")
    content = properties[1].replace("\n", " ").encode('unicode_escape')
    summary = properties[2]['text'][:500].replace("\n", " ").encode('unicode_escape')
    content = Content(source=source,
            title=title,
            summary=summary,
            content=content)
    content.save()
    Media(type="image", content=content, url=properties[3]).save()

    return properties



