import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, F, Case, When, Value, BooleanField

from django.db.models import Count, Case, When, Value, CharField, BooleanField
from main_app.models import Astronaut, Mission
# Create queries within functions
def get_astronauts(search_string=None):
    if search_string is None:
        astronauts = Astronaut.objects.none()
    else:
        # Case-insensitive partial match for name or phone_number
        astronauts = Astronaut.objects.filter(
            Q(name__icontains=search_string) |
            Q(phone_number__icontains=search_string)
        ).order_by('name')

    if not astronauts.exists():
        return ""

    result = []
    for astronaut in astronauts:
        status = "Active" if astronaut.is_active else "Inactive"
        result.append(f"Astronaut: {astronaut.name}, phone number: {astronaut.phone_number}, status: {status}")

    return "\n".join(result)


def get_top_astronaut():
    top_astronaut = Astronaut.objects.annotate(
        num_missions=Count('mission')
    ).order_by('-num_missions', 'phone_number').first()

    if not top_astronaut:
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.num_missions} missions."


def get_top_commander():
    top_commander = Astronaut.objects.annotate(
        num_commanded_missions=Count(
            Case(
                When(mission__commander_id=F('id'), then=Value(1)),
                output_field=BooleanField()
            )
        )
    ).order_by('-num_commanded_missions', 'phone_number').first()

    if not top_commander or top_commander.num_commanded_missions == 0:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.num_commanded_missions} commanded missions."