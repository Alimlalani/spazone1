from django import forms
from .models import Appointment, Payment ,MyformModel
from datetimewidget.widgets import DateTimeWidget
from django.utils.safestring import mark_safe
import six
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name','email','date', 'time', 'service_type','sub_service','phone_no']
class MyForm(forms.ModelForm):
        # form_snippet = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}))
        class Meta: 
            # template_name = "form_snippets.html"
            model = MyformModel
            fields = ['name','email','date', 'time', 'service_type','sub_service','phone']
            templates = {
                'form':'makeupbooking/form_snippet.html',
            }
        def save(self, commit=True):
            instance = super(MyForm, self).save(commit=True)
            # do any additional processing or validation here
            if commit:
                instance.save()
            return instance
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     if self.instance and self.instance.form_snippet:
        #         self.fields['form_snippet'].widget = forms.HiddenInput()
        #         self.form_snippet_html = mark_safe(self.instance.form_snippet)

        # def clean(self):
        #     cleaned_data = super().clean()
        #     form_snippet = cleaned_data.get('form_snippet')
        #     if form_snippet:
        #         cleaned_data['form_snippet'] = mark_safe(form_snippet)
        #     return cleaned_data
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'card_number', 'card_expiry', 'card_cvv']
