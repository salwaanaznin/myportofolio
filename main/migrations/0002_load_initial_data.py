from django.db import migrations

def insert_initial_experiences(apps, schema_editor):
    Experience = apps.get_model('main', 'Experience')
    
    # Keterangan: Field disesuaikan dengan 0001_initial.py milikmu
    experiences = [
        {
            "title": "Mentoring BETIS Fasilkom UI",
            "description": "Menjadi mentor akademik dan membimbing calon mahasiswa baru.",
            "category": "volunteer",
            "thumbnail": ""
        },
        {
            "title": "People Operations - RISTEK Fasilkom UI",
            "description": "Mengelola talenta dan kegiatan internal organisasi RISTEK.",
            "category": "volunteer",
            "thumbnail": ""
        },
        {
            "title": "SISTECH 2026 Internship - Digital Marketing Track",
            "description": "Mengembangkan strategi dan portofolio pemasaran digital.",
            "category": "internship",
            "thumbnail": ""
        },
        {
            "title": "TechCares Social Project",
            "description": "Panitia penyelenggara kegiatan sosial untuk panti asuhan di Jakarta.",
            "category": "volunteer",
            "thumbnail": ""
        }
    ]

    for item in experiences:
        Experience.objects.get_or_create(
            title=item["title"],
            defaults={
                "description": item["description"],
                "category": item["category"],
                "thumbnail": item["thumbnail"]
            }
        )

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_initial_experiences),
    ]