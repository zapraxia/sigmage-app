from django.forms import ModelForm, CharField

from app.models import Query


class QueryUpdateForm(ModelForm):
    signature = CharField()

    def save(self, commit=True):
        instance = super().save(commit)

        instance.signature = self.cleaned_data['signature']

        if commit:
            instance.save()

        return instance

    class Meta:
        model = Query
        fields = 'signature',
