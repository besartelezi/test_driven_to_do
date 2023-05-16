from django import forms

from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm):

    # in meta we specify which model the form is for, and which fields we want to use
    class Meta:
        model = Item
        fields = ('text',)
        # even when using custom django CSS/HTML, you can override this using widgets
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        # like widgets, this is a Meta variable that can be adjusted
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }