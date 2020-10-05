from django.db import models
from datetime import date, timedelta
from django.utils.html import format_html
from django.template.defaultfilters import date as django_date
from django.forms.fields import DateField , ChoiceField ,MultipleChoiceField
from django.forms.widgets import RadioSelect ,CheckboxSelectMultiple
from django.forms.widgets import SelectDateWidget
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    """created_date = models.DateField(auto_now_add=True)"""
    scheduled_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    closed = models.BooleanField(default=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE, default = True)

    def __str__(self):
        return "%s %s" % (self.name, self.user)

    def colored_due_date(self):
        due_date = django_date(self.due_date,"d F Y")
        if self.due_date-timedelta(days=7) > date.today():
            color = "green"
        elif self.due_date < date.today():
            color = "red"
        else:
            color = "orange"
        return format_html("<span style=color:%s>%s</span>"
         % (color, due_date))

class User(models.Model):
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


