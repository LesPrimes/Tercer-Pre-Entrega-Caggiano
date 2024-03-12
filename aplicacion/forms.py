from django import forms 

class ArticuloForm(forms.Form):
    titulo = forms.CharField(max_length=45,required= True)
    genero = forms.CharField(max_length=45,required= True)
    fecha_de_publicacion  = forms.DateTimeField(required=True)

class EscritorForm(forms.Form):
    nombre = forms.CharField(max_length=45,required= True)
    apellido = forms.CharField(max_length=45,required= True)
    email = forms.EmailField(required = True)

class LectorForm(forms.Form):
    nombre = forms.CharField(max_length=45,required= True)
    apellido = forms.CharField(max_length=45,required= True)
    email = forms.EmailField (required= True)