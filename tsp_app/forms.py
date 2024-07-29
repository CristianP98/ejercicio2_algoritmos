from django import forms

class TSPForm(forms.Form):
    num_nodes = forms.IntegerField(label='Número de ciudades', min_value=2)
    min_weight = forms.IntegerField(label='Peso mínimo', min_value=1)
    max_weight = forms.IntegerField(label='Peso máximo', min_value=1)
    start_node = forms.IntegerField(label='Nodo de inicio', min_value=0)
