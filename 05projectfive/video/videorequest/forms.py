from socket import fromshare
from django import forms


class VideoForm(forms.Form):
    videoname = forms.CharField(max_length=20,
                                widget=forms.TextInput(
                                    attrs={
                                        'id': 'inputName',
                                        'class': "form-control",
                                        'placeholder': "Name",
                                    }))

    videodesc = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'rows': "5",
            'id': "comment",
            'placeholder': "Comment",
        }))
