from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request, param):
    return HttpResponse("Hello Django ! "+param)

from lesTaches.models import Task

def task_listing(request):
    from django.template import Template, Context
    objects = Task.objects.all().order_by('due_date')
    template = Template('<ul>{% for elem in objects %}<li>{{elem}}{% endfor %}</ul>')
    print(str(template))
    context = Context({'objects': objects})
    print(str(template.render(context)))
    return HttpResponse(template.render(context))

class TaskForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email', 'message')
        widgets = {
            'message': forms.Textarea(attrs={'cols':20, 'rows': 10,
                'placeholder': 'Entrer votre message ici'}),
            'name': forms.TextInput(attrs={'placeholder': 'Doe'})
        }
        labels = {
            "name": "Nom",
            "firstname": "Prénom",
    }
    


from django import forms

class ContactForm2(forms.Form):
    
    name = forms.CharField(max_length=50, initial="Votre nom", label="nom")
    firstname = forms.CharField(max_length=50,  initial="Votre prénom", 
    label="prenom")
    email = forms.EmailField(max_length=200, label='mail')
    message = forms.CharField(max_length=1000, 
    widget=forms.Textarea(attrs={'cols':20, 'rows': 10}))


""" def contact(request):
    contact_form = ContactForm()
    contact_form2 = ContactForm2()
    return render(request, 'contact.html', 
    {'contact_form': contact_form,
    'contact_form2': contact_form2  })
 """

def contact(request):
    # on instancie un formulaire
    form = ContactForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ContactForm(request.POST)
     # on vérifie la validité du formulaire
        if form.is_valid():
            new_contact = form.save()
            messages.success(request,'Nouveau contact '+new_contact.name+' '+new_contact.email)
            #return redirect(reverse('detail', args=[new_contact.pk] ))
            context = {'pers': new_contact}
            return render(request,'detail.html', context)
    # Si méthode GET, on présente le formulaire
    context = {'form': form}
    return render(request,'contact.html', context)


def detail(request, cid):
    contact = Contact.objects.get(pk=cid)
    return HttpResponse('Nouveau contact '+contact.name+' '+contact.email)


def edit(request, pers_id):
    # on récupère la personne
    pers = Contact.objects.get(pk=pers_id)
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ContactForm(request.POST, instance=pers)
        # on vérifie la validité du formulaire
        if form.is_valid():
            form.save()
            messages.success(request, 'Personne '+pers.name+' modifiée!')
            #return redirect(reverse('detail', args=[pers_id] ))
            context = {'pers': pers}
            return render(request,'detail.html',context)
    # Si méthode GET, on présente le formulaire
    form = ContactForm(instance=pers)
    context = {'form': form,'pers': pers}
    return render(request,'edite-crispy.html', context)

def delete(request, pers_id):
    pers = Contact.objects.get(pk=pers_id)
    pers.delete()
    messages.success(request, 'Personne '+pers.name+' supprimée!')
    form = ContactForm()
    context = {'form': form}
    return render(request,'contact.html', context)


def liste(request):
    objects = Contact.objects.all().order_by('name')
    return render(request, template_name='contact_list.html', context={'objects': objects} )