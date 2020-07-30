from django import forms


class ShowForm(forms.Form):
    reference = forms.IntegerField(
        # label='Numéro de commande',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
