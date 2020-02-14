from django import forms  
from pets.models import Pet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import formset_factory

class PetForm(forms.ModelForm):
    class Meta:  
        model = Pet  
        fields = ('spec', 'sex', 'name', 'age', 'breed', 'description', 'image')
        prepopulated_fields = {"slug": ("name",)}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить', css_class="btn-success"))
        