from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Adinais Football',
        'name': 'Rafasyah Miyauchi',
        'class': 'PBD KKI'
    }

    return render(request, "main.html", context)
