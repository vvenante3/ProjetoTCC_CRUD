from django.db import migrations, models
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policial',
            fields=[
                ('idPolicial', models.AutoField(primary_key=True, serialize=False)),
                ('DataCadastro', models.DateField()),
                ('DataNascimento', models.DateField()),
                ('Sexo', models.CharField(max_length=1)),
            ],
        ),
    ]
