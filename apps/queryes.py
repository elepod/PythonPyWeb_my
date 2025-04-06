import django
import os

from django.db.models import Count, Max

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    # from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag
    #
    # # TODO Сделайте здесь запросы
    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)
    # """<QuerySet [<Entry: Оазисы Сахары: красота и опасность>,
    # <Entry: Новые гаджеты и устройства: обзор рынка>]>"""
    # print('-'*50)
    #
    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)
    # """<QuerySet [<Entry: Знакомство с Парижем>,
    # <Entry: Инновации в области виртуальной реальности>]>"""
    # print('-' * 50)
    #
    # print(Entry.objects.get(id__exact=4))
    # print(Entry.objects.get(id=4))  # Аналогично exact
    # print(Blog.objects.get(name__iexact="Путешествия по миру"))
    # print('-' * 50)
    #
    # print(Entry.objects.filter(headline__contains='мод'))
    # # <QuerySet [
    # # <Entry: Тенденции моды на текущий сезон>,
    # # <Entry: История моды: от ретро до современности>,
    # # <Entry: Интервью с известными модельерами и дизайнерами>
    # # ]>
    # print('-' * 50)
    #
    # print(Entry.objects.filter(id__in=[1, 3, 4]))
    # # <QuerySet [<Entry: Изучение красот Мачу-Пикчу>, <Entry: Знакомство с Парижем>, <Entry: Открывая тайны Колизея>]>
    #
    # print(Entry.objects.filter(number_of_comments__in='123'))  # число комментариев 1 или 2 или 3
    # """
    # <QuerySet [
    # <Entry: Изучение красот Мачу-Пикчу>,
    # <Entry: Открывая тайны Колизея>,
    # <Entry: Экзотические специи и их использование>,
    # <Entry: Упражнения для поддержания физической формы>,
    # <Entry: Топ-10 фитнес-тренеров для вдохновения>,
    # <Entry: История моды: от ретро до современности>
    # ]>
    # """
    # print('-' * 50)
    #
    # inner_qs = Blog.objects.filter(name__contains='Путешествия')
    # entries = Entry.objects.filter(blog__in=inner_qs)
    # print(entries)
    # """
    # <QuerySet [
    # <Entry: Изучение красот Мачу-Пикчу>,
    # <Entry: Приключения в Амазонке>,
    # <Entry: Знакомство с Парижем>,
    # <Entry: Открывая тайны Колизея>,
    # <Entry: Оазисы Сахары: красота и опасность>
    # ]>
    # """
    # print('-' * 50)
    #
    # # Вывести все записи, у которых число комментарием больше 10
    # print(Entry.objects.filter(number_of_comments__gt=10))
    # """
    # <QuerySet [
    # <Entry: Приключения в Амазонке>,
    # <Entry: Новые гаджеты и устройства: обзор рынка>,
    # <Entry: Кибербезопасность: защита вашей конфиденциальности>,
    # <Entry: Инновации в области виртуальной реальности>
    # ]>
    # """
    # # Вывести все записи, которые опубликованы (поле pub_date) позже и равное 01.06.2023
    # import datetime
    #
    # print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
    # """
    # <QuerySet [
    # <Entry: Приготовление собственного хлеба>,
    # <Entry: Десерты для настоящих сладкоежек>,
    # <Entry: Упражнения для поддержания физической формы>,
    # <Entry: Топ-10 фитнес-тренеров для вдохновения>,
    # <Entry: Как правильно заниматься йогой>,
    # <Entry: Последние тренды в мире искусственного интеллекта>,
    # <Entry: Как создать стильный образ на каждый день>,
    # <Entry: История моды: от ретро до современности>
    # ]>
    # """
    # # Вывести все записи, у которых число комментарием больше 10 и рейтинг < 4
    # print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
    # """
    # <QuerySet [
    # <Entry: Новые гаджеты и устройства: обзор рынка>,
    # <Entry: Кибербезопасность: защита вашей конфиденциальности>
    # ]>
    # """
    # # Вывести все записи, у которых заголовок статьи лексиграфически <= "Зя"
    # print(Entry.objects.filter(headline__lte="Зя"))
    # """
    # <QuerySet [
    # <Entry: Знакомство с Парижем>,
    # <Entry: Десерты для настоящих сладкоежек>,
    # <Entry: Гастрономическое путешествие по Франции>,
    # <Entry: Здоровое питание: полезные рецепты>
    # ]>
    # """
    #
    # print('-' * 50)
    # # Вывести записи старше 2022 года
    # print(Entry.objects.filter(pub_date__year__lt=2022))
    # """
    # <QuerySet [
    # <Entry: Новые гаджеты и устройства: обзор рынка>,
    # <Entry: Кибербезопасность: защита вашей конфиденциальности>,
    # <Entry: Инновации в области виртуальной реальности>
    # ]>
    # """
    # # Вывести все записи за февраль доступных годов, отобразить название, дату публикации, заголовок
    # print(Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline'))
    # """
    # <QuerySet [
    # {'blog__name': 'ИТ-новости и технологии', 'pub_date': datetime.date(2022, 2, 1), 'headline': 'Развитие интернета вещей: будущее или реальность?'},
    # {'blog__name': 'Мода и стиль', 'pub_date': datetime.date(2023, 2, 1), 'headline': 'Уход за кожей и волосами: лучшие советы'},
    # {'blog__name': 'Мода и стиль', 'pub_date': datetime.date(2023, 2, 1), 'headline': 'Интервью с известными модельерами и дизайнерами'}
    # ]>
    # """
    # # Вывести username авторов у которых есть публикации с 1 по 15 апреля 2023 года, вывести без использования range. Пример для работы с __day
    # print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(
    #     pub_date__day__lte=15).values_list("author__name").distinct())
    # # Сначала отфильтровываем по году, затем по дням, затем получаем значения имен у авторов и говорим, чтобы не было повторов
    # """
    # <QuerySet [
    # ('andrey_author',),
    # ('dmitriy_creative',),
    # ('alexander89',),
    # ('irina_blogger',),
    # ('ivan_wordsmith',),
    # ('maxim_writer',)
    # ]>
    # """
    # # Вывести статьи опубликованные в понедельник (так как datetime работает по американской системе,
    # # то начало недели идёт с воскресенья, а заканчивается субботой, поэтому понедельник второй день в неделе)
    # print(Entry.objects.filter(pub_date__week_day=2).values('blog__name', 'pub_date', 'headline'))
    # """
    # <QuerySet [
    # {'blog__name': 'Путешествия по миру', 'pub_date': datetime.date(2022, 8, 1), 'headline': 'Приключения в Амазонке'},
    # {'blog__name': 'Фитнес и здоровый образ жизни', 'pub_date': datetime.date(2023, 5, 1), 'headline': 'Здоровое питание: полезные рецепты'},
    # {'blog__name': 'Фитнес и здоровый образ жизни', 'pub_date': datetime.date(2024, 1, 1), 'headline': 'Топ-10 фитнес-тренеров для вдохновения'},
    # {'blog__name': 'Фитнес и здоровый образ жизни', 'pub_date': datetime.date(2024, 4, 1), 'headline': 'Как правильно заниматься йогой'},
    # {'blog__name': 'ИТ-новости и технологии', 'pub_date': datetime.date(2024, 4, 1), 'headline': 'Последние тренды в мире искусственного интеллекта'}
    # ]>
    # """
    # # week, quarter, hour, minute, second рассматривается аналогично как и всё что было ранее
    # print('-' * 50)

    from apps.db_train.models import Author, AuthorProfile, Entry, Tag
    # # TODO Какой автор имеет наибольшее количество опубликованных статей?
    # count_authors = Entry.objects.aggregate(
    #     count_authors=Count('author', distinct=True)
    # )
    # print(count_authors)  # {'count_authors': 12}
    #
    #
    # # Вычислить число уникальных авторов статей(которые написали хотя бы одну статью)
    # count_authors = Entry.objects.aggregate(
    #     count_authors=Count('author', distinct=True)
    # )
    # print(count_authors)  # {'count_authors': 12}
    #
    # # Получить статьи с количеством тегов
    # entries_with_tags_count = Entry.objects.annotate(
    #     tag_count=Count('tags')).values('id', 'tag_count')
    # print(entries_with_tags_count)
    # """
    # <QuerySet [
    # {'id': 1, 'tag_count': 2},
    # {'id': 2, 'tag_count': 1},
    # {'id': 3, 'tag_count': 2},
    # {'id': 4, 'tag_count': 2},
    # ...
    # """

    # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
    entries = Entry.objects.filter(
        tags__name__in=['Кино', 'Музыка']
    ).distinct
    print(entries)
    # print(Entry.objects.filter(tag__in=['Кино','Музыка']))
    # TODO Сколько авторов женского пола зарегистрировано в системе?
    print(Author.objects.filter(gender='ж'))
    print(Author.objects.filter(status_rule=1))
    # TODO Какие авторы имеют стаж от 1 до 5 лет?
    from django.db.models import Q
    print(Author.objects.filter(
        authorprofile__stage__in=[1,2,3,4,5]))
    max_age = Author.objects.aggregate(max_age=Max('age'))
    print(max_age)
    print(Author.objects.annotate(entry_count=Count('entries')).values('username', 'entry_count'))
    print(Author.objects.filter(status_rule=1).count()/Author.objects.count())











