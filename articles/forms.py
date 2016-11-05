from django import forms


class EmailMessageForm(forms.Form):
    name = forms.CharField(max_length=70)
    from_email = forms.EmailField()
    message = forms.CharField(required=True,
                              widget=forms.Textarea)
