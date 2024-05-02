from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
from grupos.models import Policial

class TesteSalvarPolicial(TestCase):
    def test_salvar_policial(self):
        matricula = '123456'
        nome = 'nomeTeste'
        sobrenome = 'sobrenomeTeste'
        data_cadastro = timezone.now().date()
        data_nascimento = datetime.strptime('1990-01-01', '%Y-%m-%d').date()
        sexo = 'M'

        response = self.client.post(reverse('salvar'), {
            'Matricula'     : matricula,
            'Nome'          : nome,
            'Sobrenome'     : sobrenome,
            'DataCadastro'  : data_cadastro,
            'DataNascimento': data_nascimento,
            'Sexo'          : sexo,
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        policiais = Policial.objects.filter(Matricula=matricula)
        self.assertEqual(policiais.count(),1)
        policial = policiais.first()
        self.assertEqual(policial.Matricula, matricula)
        self.assertEqual(policial.Nome, nome)
        self.assertEqual(policial.Sobrenome, sobrenome)
        self.assertEqual(policial.DataCadastro, data_cadastro)
        self.assertEqual(policial.DataNascimento, data_nascimento)
        self.assertEqual(policial.Sexo, sexo)

class TesteEditarPolicial(TestCase):
    def setUp(self):
        self.policial = Policial.objects.create(
        Matricula       = '123456',
        Nome            = 'nomeTeste',
        Sobrenome       = 'sobrenomeTeste',
        DataCadastro   = '2024-01-01',
        DataNascimento = '1990-01-01',
        Sexo            = 'M'
    )

    def test_editar_policial(self):
        response = self.client.get(reverse('editar', kwargs={'id': self.policial.idPolicial}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'atualizar.html')

        self.assertEqual(response.context['policial'], self.policial)

class TesteDeletarPolicial(TestCase):
    def setUp(self):
        self.policial = Policial.objects.create(
        Matricula       = '123456',
        Nome            = 'nomeTeste',
        Sobrenome       = 'sobrenomeTeste',
        DataCadastro   = '2024-01-01',
        DataNascimento = '1990-01-01',
        Sexo            = 'M'
    )
    def test_deletar_policial(self):
        response = self.client.get(reverse('deletar', args=(self.policial.idPolicial,)))

        self.assertFalse(Policial.objects.filter(idPolicial=self.policial.idPolicial).exists())

        self.assertRedirects(response, reverse('home'))