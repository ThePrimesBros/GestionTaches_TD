from lesTaches.models import Task, User
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.forms import ModelForm , Textarea
from django.forms.fields import DateField , ChoiceField ,MultipleChoiceField
from django import forms




class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'scheduled_date', 'due_date', 'closed', 'user')
        widgets = {
            'description': forms.Textarea(attrs={'cols':20, 'rows': 10,
                'placeholder': 'Entrer votre message ici'}),
            'name': forms.TextInput(attrs={'placeholder': 'Doe'})
        }
        labels = {
            "name": "Nom",
            "description": "Votre Message",
    }
    


def task(request):
    # on instancie un formulaire
    form = TaskForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = TaskForm(request.POST)
     # on vérifie la validité du formulaire
        if form.is_valid():
            new_contact = form.save()
            #messages.success(request,'Nouveau task '+new_contact.name)
            #return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'pers': new_contact}
            return render(request,'detail.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request,'task.html', context)


def detail(request, cid):
    tache = Task.objects.get(pk=cid)
    return HttpResponse('Nouvelle tache '+tache.name+' '+tache.email)


def edit(request, pers_id):
    # on récupère la personne
    pers = Task.objects.get(pk=pers_id)
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = TaskForm(request.POST, instance=pers)
        # on vérifie la validité du formulaire
        if form.is_valid():
            form.save()
            #messages.success(request, 'Personne '+pers.name+' modifiée!')
            #return redirect(reverse('detail', args=[pers_id] ))
            context = {'pers': pers}
            return redirect('http://localhost:8000/lesTaches/listing/')
    # Si méthode GET, on présente le formulaire
    form = TaskForm(instance=pers)
    context = {'form': form,'pers': pers}
    return render(request,'edite-crispy.html', context)

def delete(request, pers_id):
    pers = Task.objects.get(pk=pers_id)
    pers.delete()
    #messages.success(request, 'Personne '+pers.name+' supprimée!')
    form = TaskForm()
    context = {'form': form}
    return redirect('http://localhost:8000/lesTaches/listing/')


def liste(request):
    objects = Task.objects.all().order_by('name')
    return render(request, template_name='list2.html', context={'objects': objects} )

def liste_user(request, user_id):
    pers = User.objects.get(pk=user_id)
    objects = Task.objects.all().filter(user=pers)
    return render(request, template_name='user_list.html', context={'objects': objects} )