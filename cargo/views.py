from django.shortcuts import render, get_object_or_404
from .models import Commande
from .forms import ShowForm


def index(request):
    return render(request, 'cargo/index.html')


# Create your views here.
def consulter(request):
    context = {
    }
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            reference = form.cleaned_data['reference']
            commande = Commande.objects.filter(reference=reference)
            if not commande.exists():
                context = {
                    'form': form,
                    'saisi_utilisateur': reference
                }
            else:
                form = ShowForm()
                context = {
                    'form': form,
                    'commande': commande
                }
        else:
            context['errors'] = form.errors.items()
            context['form'] = form
        return render(request, 'cargo/show.html', context)
    else:
        form = ShowForm()
    context = {
        'form': form,
    }
    return render(request, 'cargo/show.html', context)
