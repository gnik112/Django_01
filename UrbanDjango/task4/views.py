from django.shortcuts import render


def index_platform(request):
    content = {
        'title': 'Главная страница',
    }
    return render(request, 'fourth_task/platform.html', content)


def index_games(request):
    content = {
        'title': 'Магазин',
        'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    }
    return render(request, 'fourth_task/games.html', content)


def index_cart(request):
    content = {
        'title': 'Корзина',
    }
    return render(request, 'fourth_task/cart.html', content)
