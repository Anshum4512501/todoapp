from django import template
from datetime import datetime
from django.utils import timezone
register = template.Library()

@register.filter(name='all_set') 
def all_set(value):

    delta = value.due_date - timezone.now()

    if delta.days == 0:
        return "Today!"
    elif delta.days < 1:
        return "%s %s ago!" % (abs(delta.days),
            ("day" if abs(delta.days) == 1 else "days"))
    elif delta.days == 1:
        return "Tomorrow"
    elif delta.days > 1:
        return "In %s days" % delta.days

# register.filter('cut', all_set)
    