from django.forms import ModelForm

from shikshapp.models import worklist
class worklistForm(ModelForm):
    class Meta:
        model = worklist
        fields = ['title' , 'status' , 'priority']
        