from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


# Create your   views here.
def output_posts_on_page(request):
    posts = Post.objects.all().order_by('-created_at')    # получили все объекты в отсортированном порядке с даты создания сверху
    paginator = Paginator(posts, 3)    # укажем количество объектов на странице
    page_number = request.GET.get('page')    # получаем текущую страницу(номер) пользователя
    page_obj = paginator.get_page(page_number)    # к объекту paginator применяем метод get_page с указанием в параметрах текущей страницы пользователя
    return render(request, 'output_posts_on_page.html', {'page_obj': page_obj})
