from django.forms import ModelForm, TextInput, Textarea, URLInput

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
        