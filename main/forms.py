from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Experience Name",
            "description": "Experience Description",
            "category": "Institution of Experience",
            "thumbnail": "Experience Thumbnail"
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Project Officer",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us your experience!",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "SMAN 62 Jakarta",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=1uFBiNVPitb4icMrYdONFDg2TeqyITB8T&sz=w1000",
                }
            ),
        }