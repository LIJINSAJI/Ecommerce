from.models import Catagory
def menu_links(request):
    links=Catagory.objects.all()
    return dict(links=links)