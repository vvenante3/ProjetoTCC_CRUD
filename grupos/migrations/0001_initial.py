from django.db import migrations, models
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policial',
            fields=[
                ('idPolicial',  models.AutoField(primary_key=True, serialize=False)),
                ('Matricula',   models.CharField(max_length=10)),
                ('Nome', models.CharField(max_length=15)),
                ('Sobrenome', models.CharField(max_length=30)),
                ('DataCadastro', models.DateField()),
                ('DataNascimento', models.DateField()),
                ('Sexo', models.CharField(max_length=1)),
            ],
        ),
    ]
