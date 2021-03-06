from django import forms
from .models import PleaseSearch

class PleaseSearchForm(forms.Form):

    class Meta:
        model = PleaseSearch
        
    Cities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PleaseSearch.CITY_CHOICES)
    Categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PleaseSearch.CATEGORY_CHOICES)
    Counties = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PleaseSearch.COUNTY_CHOICES)

