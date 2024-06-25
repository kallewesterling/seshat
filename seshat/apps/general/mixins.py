# mixins.py

class PolityIdMixin:
    def get_initial(self):
        initial = super().get_initial()
        polity_id_x = self.request.GET.get('polity_id_x')
        other_polity_id_x = self.request.GET.get('other_polity_id_x')
        if polity_id_x:
            initial['polity'] = polity_id_x
        if other_polity_id_x:
            initial['other_polity'] = other_polity_id_x
        return initial

    