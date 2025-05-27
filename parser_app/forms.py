from django import forms
from . import models, parser_kinov

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('kinovibe.co', 'kinovibe.co'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'kinovibe.co':
            kinovibe_films = parser_kinov.parsing_kinov()
            for i in kinovibe_films:
                models.Parser_Kinov.objects.create(**i)
