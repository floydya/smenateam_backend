import tempfile
import json
from base64 import b64encode

import requests
from django.core import files

from app.utils import render_check, status_choices


def get_file(data):
    fp = tempfile.NamedTemporaryFile()
    fp.write(data)
    return fp


def generate_check_task(instance):
    rendered_html_check = render_check(instance.printer.check_type, instance.order)

    contents = b64encode(bytes(rendered_html_check, 'utf8')).decode('utf8')

    response = requests.post('http://localhost/', data=json.dumps({
        'contents': contents,
    }), headers={
        'Content-Type': 'application/json',
    })

    rendered_pdf_check = get_file(response.content)
    filename = '{}_{}.pdf'.format(instance.order['id'], instance.printer.check_type)
    instance.pdf_file = files.File(rendered_pdf_check, name=filename)
    instance.status = status_choices.rendered
    instance.save(update_fields=['pdf_file', 'status'])
    rendered_pdf_check.close()
