from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound, \
    HttpResponseForbidden, HttpResponseServerError


def custom_handler400(request, exception):
    # Call when SuspiciousOperation raised
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    # Call when PermissionDenied raised
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')


def main_view(request):
    # authors = Author.objects.all()
    # context = {
    #     "authors": authors
    # }
    return render(request, "index.html")


def departure_view(request, departure):
    # authors = Author.objects.all()
    # context = {
    #     "authors": authors
    # }
    return render(request, "departure.html")


def tour_view(request, id):
    # authors = Author.objects.all()
    # context = {
    #     "authors": authors
    # }
    return render(request, "tour.html")
