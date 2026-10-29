from django.http import HttpResponse


def index(request):
    return HttpResponse("INDEX PAGE. جیگر.")

def test_page(request):
    return HttpResponse("سلام عزیزم عزیزم سلام.")