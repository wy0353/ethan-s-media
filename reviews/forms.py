from django import forms
from . import models as review_models


class ReviewCreateForm(forms.ModelForm):

    """ For create variety item reviews. """

    class Meta:
        model = review_models.Review
        fields = (
            "text",
            "rating",
        )

    def save(self, *args, **kwargs):
        review = super().save()
        return review
