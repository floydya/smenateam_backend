from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from app.models import Printer, Check
from app.utils import status_choices


@api_view(['POST'])
def create_checks(request: Request):
    printers = Printer.objects.filter(point_id=request.data.get('point_id'))
    if not printers:
        return Response(
            {"error": "Для данной точки не настроено ни одного принтера."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if Check.objects.filter(order__id=request.data.get('id')).exists():
        return Response(
            {"error": "Для данного заказа уже созданы чеки."},
            status=status.HTTP_400_BAD_REQUEST
        )

    for printer in printers:
        Check.objects.create(printer=printer, order=request.data)

    return Response(
        {"ok": "Чеки успешно созданы."},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def new_checks(request: Request):
    try:
        api_key = request.query_params.get('api_key')
        printer = Printer.objects.get(api_key=api_key)
    except Printer.DoesNotExist:
        return Response(
            {"error": "Ошибка авторизации."},
            status=status.HTTP_401_UNAUTHORIZED
        )
    checks = Check.objects.filter(printer=printer, status=status_choices.rendered).values('id')
    return Response(
        {"checks": checks},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def check(request: Request):
    try:
        api_key = request.query_params.get('api_key')
        printer = Printer.objects.get(api_key=api_key)
    except Printer.DoesNotExist:
        return Response(
            {"error": "Ошибка авторизации."},
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        pk = request.query_params.get('id')
        _check = Check.objects.get(printer=printer, pk=pk)
    except Check.DoesNotExist:
        return Response(
            {"error": "Данного чека не существует"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if _check.status == status_choices.new:
        return Response(
            {"error": "Для данного чека не сгенерирован PDF-файл."},
            status=status.HTTP_400_BAD_REQUEST
        )

    return FileResponse(_check.pdf_file, as_attachment=True, filename=_check.pdf_file.name)
