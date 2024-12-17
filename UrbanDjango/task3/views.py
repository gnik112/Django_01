from django.shortcuts import render


def index_platform(request):
    return render(request, 'third_task/platform.html')


def index_games(request):
    content = {
        'title_1': 'Atomic Heart',
        'title_2': 'Cyberpunk 2077',
        'title_3': 'PayDay 2'
    }
    return render(request, 'third_task/games.html', content)


def index_cart(request):
    return render(request, 'third_task/cart.html')
