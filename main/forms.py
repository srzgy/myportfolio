from django.forms import ModelForm, TextInput, Textarea, URLInput

from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import Experience, Education

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
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Experience name can't contain only HTML tags.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()
    

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "description", "thumbnail"]

        labels = {
                    "institution": "Institution of Education",
                    "degree": "Degree of Education",
                    "description": "Description of Education",
                    "thumbnail": "Education Thumbnail"
                }

        widgets = {
                    "institution": TextInput(
                        attrs={
                            "placeholder": "SMAN 62 Jakarta",
                            "maxlength": 255,
                        }
                    ),
                    "degree": TextInput(
                        attrs={
                            "placeholder": "Undergraduate",
                            "rows": 3,
                        }
                    ),
                    "description": Textarea(
                        attrs={
                            "placeholder": "Write down what you did here!",
                        }
                    ),
                    "thumbnail": URLInput(
                        attrs={
                            "placeholder": "https://drive.google.com/thumbnail?id=1uFBiNVPitb4icMrYdONFDg2TeqyITB8T&sz=w1000",
                        }
                    ),
                }
        