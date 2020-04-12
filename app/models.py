from django.contrib.postgres.fields import JSONField
from django.db import models

from app.utils import CHECK_CHOICES, STATUS_CHOICES, status_choices


def upload_to(instance, filename):
    return 'pdf/{}_{}.pdf'.format(instance.order['id'], instance.printer.check_type)


class Printer(models.Model):
    name = models.CharField(
        max_length=256
    )
    api_key = models.CharField(
        max_length=256,
        unique=True,
    )
    check_type = models.CharField(
        max_length=8,
        choices=CHECK_CHOICES
    )
    point_id = models.IntegerField()

    def __str__(self):
        return f"{self.name} [Point №{self.point_id}]"


class Check(models.Model):
    printer = models.ForeignKey(
        Printer,
        on_delete=models.CASCADE,
        related_name="checks"
    )
    order = JSONField()
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=status_choices.new
    )
    pdf_file = models.FileField(null=True, blank=True, upload_to=upload_to)
