from django.forms import ModelForm, CharField

from .models import UsersPosts


class UsersPostCreateForm(ModelForm):

    class Meta:
        model = UsersPosts
        fields = "name", "username", "email", "body"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print("name:", name, "field:", field, field.widget)
            # field.label_suffix = " ="
            field.widget.attrs["class"] = "model-form"
