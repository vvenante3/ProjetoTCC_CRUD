from django.db import models

class Policial(models.Model):
    idPolicial      = models.AutoField(primary_key=True)
    DataCadastro    = models.DateField()
    DataNascimento  = models.DateField()
    Sexo            = models.CharField(max_length=1)
    #ImgPolicial     = ImageField(upload_to='')                  # <-- colocar caminho do arquivo 16:47

    def __str__(self):
        return f'{self.idPolicial} - {self.DataCadastro} - {self.DataNascimento} - {self.Sexo}'