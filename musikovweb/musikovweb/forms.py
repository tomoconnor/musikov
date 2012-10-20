from django import forms

class UploadForm(forms.Form):
    userFile = forms.FileField(
        label='Select a file',
        help_text='max. 8 megabytes'
    )

