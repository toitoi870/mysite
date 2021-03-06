# Generated by Django 2.1.7 on 2019-03-12 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('phase_id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('trade_id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('phase_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trade.Phase')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('player_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='trade.Player')),
                ('fund', models.IntegerField(default=10000)),
                ('stock', models.IntegerField(default=50)),
            ],
        ),
        migrations.AddField(
            model_name='trade',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trade.Player'),
        ),
    ]
