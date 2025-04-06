from django.shortcuts import render
from django.views import View
# from .models import ...
from .models import Author, AuthorProfile, Entry, Tag


# class TrainView(View):
#     def get(self, request):
#         context = {}  # Создайте здесь запросы к БД
#         return render(request, 'train_db/training_db.html', context=context)

from django.db.models import Q, Max, Min, Avg, Count

class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        # Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])
        # TODO Какой автор имеет наибольшее количество опубликованных статей?
        self.answer2 = Author.objects.annotate(num_entries=Count('entries')).order_by('-num_entries').first()
        # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer3 = Entry.objects.filter(tags__name__in=['Кино', 'Музыка']).distinct()
        # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer4 = Author.objects.filter(gender='ж').count()
        # TODO Какой процент авторов согласился с правилами при регистрации?
        self.answer5 = Author.objects.filter(status_rule=1).count()/Author.objects.count()
        # TODO Какие авторы имеют стаж от 1 до 5 лет?
        self.answer6 = Author.objects.filter(authorprofile__stage__in=[1, 2, 3, 4, 5])
        # TODO Какой автор имеет наибольший возраст?
        max_age = Author.objects.aggregate(max_age=Max('age'))
        self.answer7 = max_age['max_age'] # Author.objects.filter(age=max_age['max_age'])
        # TODO Сколько авторов указали свой номер телефона?
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()
        # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer9 = Author.objects.filter(age__lte=25)
        # TODO Сколько статей написано каждым автором?
        #  select e.author_id, count(e.author_id) from db_train_entry as e group by e.author_id
        self.answer10 = Author.objects.annotate(entry_count=Count('entries')).values('username', 'entry_count')

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)

