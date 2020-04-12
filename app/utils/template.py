from django.template.loader import render_to_string


def render_check(check_type, order_data):
    return render_to_string(f'{check_type}_check.html', order_data)
