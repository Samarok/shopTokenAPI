from django.forms.models import ModelForm
from .models import Good

class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = '__all__'