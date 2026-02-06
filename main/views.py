from django.shortcuts import render
from pyexpat.errors import messages

from .models import*

def index_view(request):
    togri=None
    notogrilar=None
    message=None
    search = request.GET.get('search')
    if search:
        search = search.lower()
        togrilar=Togri.objects.filter(soz=search)
        if togrilar.exists():
            togri=togrilar.first()
            notogrilar=Notogri.objects.filter(togri=togri)
        else:
            notogrilar=Notogri.objects.filter(soz=search)
            if notogrilar.exists():
                notogri=notogrilar.first()
                togri=notogri.togri
                notogrilar=togri.notogri_set.all()
            else:
                if not search.isalpha():
                    message="Noto'g'ri kiritish! faqat harflardan iborat qil"
                elif 'h' not in search and 'x' not in search:
                    message="So'z tarkibida hx qatnashmagan"
                else:
                    message="So'z bazada yo'q"

    context = {
        'search': search,
        'togri': togri,
        'notogrilar': notogrilar,
        'message': message,
    }
    return render(request, "index.html", context )
