from django.db import models

class Policial(models.Model):
    idPolicial      = models.AutoField(primary_key=True)
    Matricula       = models.CharField(max_length=10, null=True)
    Nome            = models.CharField(max_length=15)
    Sobrenome       = models.CharField(max_length=30)
    DataCadastro    = models.DateField()
    DataNascimento  = models.DateField()
    Sexo            = models.CharField(max_length=1)
    #ImgPolicial    = ImageField(upload_to='',)                  # <-- colocar caminho do arquivo
    def __str__(self):
        return f'{self.idPolicial} - {self.Matricula} - {self.Nome} - {self.Sobrenome} - {self.DataCadastro} - {self.DataNascimento} - {self.Sexo}'

class Psicologo(models.Model):
    idPsicologo     = models.AutoField(primary_key=True)
    NomePsicologo   = models.CharField(max_length=30)
    CRP             = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.idPsicologo} - {self.NomePsicologo} - {self.CRP}'