from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from app.forms import QueryUpdateForm
from app.models import Query


class QueryCreateView(CreateView):
    model = Query
    fields = 'image',

    def get_success_url(self):
        return reverse('query-update', kwargs={'pk': self.object.id})


class QueryUpdateView(UpdateView):
    model = Query
    form_class = QueryUpdateForm
    template_name = 'app/query_update.html'

    def get_initial(self):
        return {
            **super().get_initial(),
            'signature': self.object.signature,
        }

    def get_success_url(self):
        return reverse('query-update', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'signature': self.object.signature,
        }
