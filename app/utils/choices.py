from collections import namedtuple

check_choices = namedtuple('CheckChoices', ('kitchen', 'client'))(
    'kitchen',
    'client'
)
CHECK_CHOICES = ((name, getattr(check_choices, name)) for name in check_choices)

status_choices = namedtuple('StatusChoices', ('new', 'rendered', 'printed'))(
    'new',
    'rendered',
    'printed'
)
STATUS_CHOICES = ((name, getattr(status_choices, name)) for name in status_choices)
