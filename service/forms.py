from django import forms
from .models import Sheba
class Service(forms.ModelForm):
    class Meta:
            model = Sheba
            # fields='__all__'
            fields=['user','servicetitle',
            'servicedetails','servicecategory',
            'serviceprice','servicelocation','featureservice'
            ]
            widgets = {
                'user':forms.HiddenInput(attrs={'class':'form-control'}),
                'featureservice':forms.HiddenInput(attrs={'class':'form-control'}),
            'servicetitle': forms.TextInput(attrs={'class':'form-control'}),
            'servicedetails': forms.TextInput(attrs={'class':'form-control'}),
            'servicecategory': forms.Select(attrs={'class':'form-control'}),
            'serviceprice':forms.TextInput(attrs={'class':'form-control'}),
            'servicelocation': forms.Select(attrs={'class':'form-control'}),

             }