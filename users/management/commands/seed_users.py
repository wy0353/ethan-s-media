import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from categories.models import Category

class Command(BaseCommand):

    help = "This command seeds users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total", help="How many users do you want to create?", default=1, type=int)

    def handle(self, *args, **options):
        total = options.get('total')
        seeder = Seed.seeder()
        movies = Category.objects.filter(kind=Category.KIND_MOVIE)
        books = Category.objects.filter(kind=Category.KIND_BOOK)
        seeder.add_entity(User, total, {
            "is_staff": False,
            "is_superuser": False,
            "preference": lambda x: random.choice([User.PREF_BOOKS, User.PREF_MOVIES]),
            "language": lambda x: random.choice([User.LANG_EN, User.LANG_KR]),
            "fav_book_cat": lambda x: random.choice(books),
            "fav_movie_cat": lambda x: random.choice(movies)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{total} users created!'))
