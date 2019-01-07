from django.forms import ModelForm, Form, ModelChoiceField, TextInput, Select, Textarea
from questoes.models import Pergunta, Modalidade, Ano, Staff, Nivel, Confederacao, Alternativa

class FiltroForm(Form):
    modalidade = ModelChoiceField(queryset = Modalidade.objects.all(), empty_label="Modalidade...", required=False, widget=Select(attrs={'class':'custom-select'}))
    ano = ModelChoiceField(queryset = Ano.objects.all(), empty_label="Ano...", required=False, widget=Select(attrs={'class':'custom-select'}))
    staff = ModelChoiceField(queryset = Staff.objects.all(), empty_label="Staff...", required=False, widget=Select(attrs={'class':'custom-select'}))
    nivel = ModelChoiceField(queryset = Nivel.objects.all(), empty_label="Nível...", required=False, widget=Select(attrs={'class':'custom-select'}))
    confederacao = ModelChoiceField(queryset = Confederacao.objects.all(), empty_label="Confederação...", required=False, widget=Select(attrs={'class':'custom-select'}))

class PerguntaForm(ModelForm):
    modalidade = ModelChoiceField(queryset = Modalidade.objects.all(), empty_label="Modalidade...", required=True, widget=Select(attrs={'class':'custom-select'}))
    ano = ModelChoiceField(queryset = Ano.objects.all(), empty_label="Ano...", required=True, widget=Select(attrs={'class':'custom-select'}))
    staff = ModelChoiceField(queryset = Staff.objects.all(), empty_label="Staff...", required=True, widget=Select(attrs={'class':'custom-select'}))
    nivel = ModelChoiceField(queryset = Nivel.objects.all(), empty_label="Nível...", required=True, widget=Select(attrs={'class':'custom-select'}))
    confederacao = ModelChoiceField(queryset = Confederacao.objects.all(), empty_label="Confederação...", required=True, widget=Select(attrs={'class':'custom-select'}))
    class Meta:
        model = Pergunta
        fields = ['texto', 'modalidade', 'ano', 'staff', 'confederacao', 'nivel']
        widgets = {'texto': Textarea(attrs={'class': 'form-control', 'placeholder': 'Pergunta'})}


class AlternativaForm(ModelForm):
    class Meta:
        model = Alternativa
        fields = ['texto', 'correta']
        widgets = {'texto': TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternativa'})}