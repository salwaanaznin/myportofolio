from django.db import migrations
from django.core.management import call_command

def load_fixture(apps, schema_editor):
    try:
        call_command('loaddata', 'initial_experiences.json')
    except Exception as e:
        print(f"Error loading fixture: {e}")

def reverse_load_fixture(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),  # Pastikan nama '0001_initial' sesuai dengan nama file migration pertama kamu
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_load_fixture),
    ]