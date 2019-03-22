from django import forms


class FileUploadFile(forms.Form):
    name = forms.CharField(max_length=20, min_length=3, required=True, label='name:')
    my_file = forms.FileField(label='file_name:')


