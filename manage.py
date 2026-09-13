#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

from datetime import date
import datetime
from main.models import Experience

Experience.objects.create(
    title="Member of People Operations",
    category="RISTEK Fasilkom UI 2026",
    description="Drive member engagement through the end-to-end planning and execution of organizational bonding events and internal development programs.",
    started_at=date(2026, 2, 1),
    ended_at=None,
    thumbnail="https://docs.ristek.cs.ui.ac.id/img/ristek.png"
)

Experience.objects.create(
    title="Supermentor",
    category="Programming Foundation 0",
    description="DDP0 mentors to ensure all activities were well-organized and aligned with the program's core objectives.",
    started_at=date(2025, 12, 1),
    ended_at=date(2026, 1, 31),
    thumbnail="https://lh3.googleusercontent.com/d/1jqeCZY-ZgGdHZHbOPCr8eOGxzl_BIQun"
)

Experience.objects.create(
    title="Student Advocacy and Welfare Intern",
    category="BEM Fasilkom UI",
    description="Actively engaged in identifying and analyzing student welfare issues, proposing data-driven solutions to improve student life quality.",
    started_at=date(2025, 9, 1),
    ended_at=date(2025, 12, 31),
    thumbnail="https://lh3.googleusercontent.com/d/1xcws7p7XpBdZl_8FBIWnX15VBMJE__Hy"
)

Experience.objects.create(
    title="Mentor",
    category="BETIS Fasilkom UI",
    description="intensive academic mentorship for high school students, providing strategic guidance on university entrance exam preparations and curriculum navigation to achieve PTN admissions.",
    started_at=timezone.make_aware(datetime.datetime(2026, 1, 1)),
    ended_at=timezone.make_aware(datetime.datetime(2026, 3, 31)),
    thumbnail="https://lh3.googleusercontent.com/d/1iFBrAT1JYCQfjuDV5X7KDOsJIDtOWajr"
)