from django import forms
from .models import Upload

class FunUploadForm(forms.ModelForm):

    class Meta:
        model = Upload
        fields = ['your_name', 'opponent_name', 'your_video', 'opponent_video']
