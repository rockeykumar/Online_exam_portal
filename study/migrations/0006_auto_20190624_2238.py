# Generated by Django 2.2.2 on 2019-06-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_auto_20190624_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ques', models.TextField()),
                ('Ans1', models.TextField()),
                ('Ans2', models.TextField()),
                ('Ans3', models.TextField()),
                ('Ans4', models.TextField()),
                ('RightAns', models.IntegerField()),
                ('StudentAns', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='registeration',
            name='C_Password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='Contact',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='Email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='Password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='gc',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='gp',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='gy',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='ic',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='ip',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='iy',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='my',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='oc',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='op',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='oy',
            field=models.CharField(max_length=5),
        ),
    ]