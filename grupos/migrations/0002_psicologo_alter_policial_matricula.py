# Generated by Django 5.0.4 on 2024-04-23 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Psicologo',
            fields=[
                ('idPsicologo', models.AutoField(primary_key=True, serialize=False)),
                ('nomePsicologo', models.CharField(max_length=30)),
                ('CRP', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='policial',
            name='Matricula',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
