import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, F, Case, When, Value, BooleanField, Max, Count, F, Sum

# from django.db.models import Count, Case, When, Value, CharField, BooleanField
from main_app.models import Astronaut, Mission, Spacecraft
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


def get_last_completed_mission():
    last_completed_mission = Mission.objects.filter(status='Completed').order_by('-launch_date').first()

    if not last_completed_mission:
        return "No data."

    commander_name = last_completed_mission.commander.name if last_completed_mission.commander else "TBA"
    astronauts_names = ", ".join(astronaut.name for astronaut in last_completed_mission.astronauts.all().order_by('name'))
    total_spacewalks = sum(astronaut.spacewalks for astronaut in last_completed_mission.astronauts.all())
    
    return f"The last completed mission is: {last_completed_mission.name}. " \
           f"Commander: {commander_name}. " \
           f"Astronauts: {astronauts_names}. " \
           f"Spacecraft: {last_completed_mission.spacecraft.name}. " \
           f"Total spacewalks: {total_spacewalks}."
           
           
def get_most_used_spacecraft():
    most_used_spacecraft = Spacecraft.objects.annotate(
        num_missions=Count('mission')
    ).order_by('-num_missions', 'name').first()

    if not most_used_spacecraft:
        return "No data."

    num_astronauts = Astronaut.objects.filter(mission__spacecraft=most_used_spacecraft).distinct().count()

    return f"The most used spacecraft is: {most_used_spacecraft.name}, manufactured by {most_used_spacecraft.manufacturer}, " \
           f"used in {most_used_spacecraft.num_missions} missions, astronauts on missions: {num_astronauts}."
           
           
def decrease_spacecrafts_weight():
    affected_spacecrafts = Spacecraft.objects.filter(
        mission__status='Planned'
    ).annotate(
        current_weight=F('weight') - 200.0
    ).filter(
        current_weight__gte=0.0
    ).distinct()

    if not affected_spacecrafts.exists():
        return "No changes in weight."

    num_affected_spacecrafts = affected_spacecrafts.count()
    total_weight = Spacecraft.objects.aggregate(avg_weight=Sum('weight'))['avg_weight']
    new_avg_weight = total_weight / Spacecraft.objects.count()

    for spacecraft in affected_spacecrafts:
        spacecraft.weight -= 200.0
        spacecraft.save()

    return f"The weight of {num_affected_spacecrafts} spacecrafts has been decreased. " \
           f"The new average weight of all spacecrafts is {new_avg_weight:.1f}kg."                      
           