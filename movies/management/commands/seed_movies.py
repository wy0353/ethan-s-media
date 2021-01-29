from random import choice, choices, randint
import math
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from movies.models import Movie
from categories.models import Category
from people.models import Person

posters = [
    "https://images.moviepostershop.com/replicas-movie-poster-1000778791.jpg",
    "https://i.pinimg.com/originals/96/a0/0d/96a00d42b0ff8f80b7cdf2926a211e47.jpg",
    "https://cdn11.bigcommerce.com/s-ydriczk/images/stencil/1280x1280/products/88997/93196/Avengers-Endgame-Final-Style-Poster-buy-original-movie-posters-at-starstills__42370.1563973516.jpg?c=2",
    "https://cdn.shopify.com/s/files/1/0969/9128/products/Joker_-_Joaquin_Phoenix_-_Hollywood_Action_Movie_Poster_08339151-d79a-4b7b-8bc7-dcad04881c2c.jpg?v=1573629460",
    "https://i.pinimg.com/originals/bc/d5/c9/bcd5c9519581acc60bd60a429ab0c88f.jpg",
    "https://www.washingtonpost.com/graphics/2019/entertainment/oscar-nominees-movie-poster-design/img/black-panther-web.jpg",
    "https://www.joblo.com/assets/images/joblo/posters/2019/01/IO-poster-1.jpg",
    "https://creativereview.imgix.net/content/uploads/2019/12/joker_full.jpg?auto=compress,format&q=60&w=1012&h=1500",
    "https://images-na.ssl-images-amazon.com/images/I/61Zf5g-xUxL._AC_SL1039_.jpg",
    "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/adventure-movie-poster-template-design-7b13ea2ab6f64c1ec9e1bb473f345547_screen.jpg?ts=1576732289",
    "https://images.moviepostershop.com/dora-and-the-lost-city-of-gold-movie-poster-1000779403.jpg",
    "https://i.etsystatic.com/16832842/r/il/ab3e04/1573128269/il_570xN.1573128269_4nw9.jpg",
    "https://cdn.seat42f.com/wp-content/uploads/2020/07/15192015/Project-Power-Movie-Poster-Jamie-Foxx.jpg",
    "https://cdn.shopify.com/s/files/1/0290/5663/0868/products/OneYearInLove_999x667_0a291051-f07b-4ceb-b37b-4c2a386683c4-134529_1200x.jpg?v=1580120124",
    "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/action-movie-poster-template-design-0f5fff6262fdefb855e3a9a3f0fdd361_screen.jpg?ts=1573101130",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjT7IrCLFHjHtB_mIKxSumVOVE9grrWPphjA&usqp=CAU",
    "https://images-na.ssl-images-amazon.com/images/I/91WNnQZdybL._AC_SL1500_.jpg",
    "https://www.washingtonpost.com/graphics/2019/entertainment/oscar-nominees-movie-poster-design/img/star-is-born-web.jpg",
    "https://assets.mubicdn.net/images/notebook/post_images/28127/images-w1400.jpg?1558009751",
    "https://upload.wikimedia.org/wikipedia/en/4/43/Enormity_of_Life_Movie_Poster.jpg",
    "https://mymodernmet.com/wp/wp-content/uploads/2020/02/parasite-film-tribute-1.jpg",
    "https://maxcdn.icons8.com/app/uploads/2019/05/poster-for-movie.png",
    "https://c8.alamy.com/comp/EJWNX5/home-alone-movie-poster-EJWNX5.jpg",
    "https://i.pinimg.com/originals/fd/5e/66/fd5e662dce1a3a8cd192a5952fa64f02.jpg",
    "https://cdn.shopify.com/s/files/1/0969/9128/products/Midway_2019_-_Ed_Skrein_-_Hollywood_War_WW2_Movie_Poster_e0326fd4-ec9a-48b8-a6f3-c702a01f75bc.jpg?v=1582782838",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShWxjWWVCu-62mQtmGtDEqUDTXCjm2oPS62g&usqp=CAU",
    "https://cdn11.bigcommerce.com/s-l71eudan7b/images/stencil/1280x1280/products/779/1378/51VLaiKIRHL__26097.1586531548.jpg?c=2",
    "https://lh3.googleusercontent.com/proxy/YmSFvDgy8CO3ETDQ0wMf_E6GPtbTeUu3fbtSfWyM7vFn_R3L2VLbxZY4LSDvUfwESq05WwipZvMPRBMKuwHst6U4oAjbxblhcsvFENrhj_FRQfxH3TM"
    "https://d13ezvd6yrslxm.cloudfront.net/wp/wp-content/images/2017-bestposter-starwarslastjedi.jpg",
    "https://cdn.shopify.com/s/files/1/0057/3728/3618/products/4c177c2b7f7bb9a679f089bcb50f844e_3e89eb5d-ffbd-4033-a00f-e595a3ef2e2a_240x360_crop_center.progressive.jpg?v=1573587540",
    "https://www.filmink.com.au/wp-content/uploads/2018/01/john_wick_chapter_two_ver2_xlg-195x300.jpg",
    "https://cdnb.artstation.com/p/assets/images/images/011/694/837/large/editician-zone-editician-zone-113.jpg?1530897875",
    "https://cdn.shopify.com/s/files/1/0057/3728/3618/products/black_widow_ver9_xlg_240x360_crop_center.progressive.jpg?v=1598017338",
    "https://images.fandango.com/ImageRenderer/0/0/redesign/static/img/default_poster.png/0/images/masterrepository/other/ant_man_ver5.jpg",
    "https://lh3.googleusercontent.com/proxy/EztCdRDQ2pc2TIRWhdw8TpmumEjsbxwvkVIvfbxXTBtbv6Kk0b8XxKK3vPKBeDDMMoIvIoCohuajj27r4JO4UdNS4cwPrfOXOqb6bkPrY_Rd6xivZEM8-xk5sfKOaIWZD2vi9LchnbVMCuE",
    "https://images.complex.com/complex/images/fl_lossy,pg_1/wjnhpz3osrai5aningjl/titanic",
    "https://media.comicbook.com/2017/10/spider-man-homecoming-movie-poster-marvel-cinematic-universe-1038913.jpg",
    "https://www.filmjabber.com/movie-poster-thumbs/free-guy-movie-poster-6492.jpg",
]

class Command(BaseCommand):

    help = "This command seeds movies"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            help="How many movies do you want to create?",
            default=10, type=int)

    def handle(self, *args, **options):
        total = options.get('total')
        categories = Category.objects.all()
        directors = Person.objects.filter(kind=Person.KIND_DIRECTOR)
        actors = Person.objects.filter(kind=Person.KIND_ACTOR)
        seeder = Seed.seeder()
        seeder.add_entity(
            Movie, total, {
                "year": lambda x: seeder.faker.year(),
                "rating": lambda x: randint(1, 5),
                "category": lambda x: choice(categories),
                "director": lambda x: choice(directors),
                "cover_image_url": lambda x: choice(posters),
            })
        movies_pk = seeder.execute()
        cleaned_pks = flatten(list(movies_pk.values()))
        for pk in cleaned_pks:
            movie = Movie.objects.get(pk=pk)
            s_num = randint(5, math.floor(33/3))
            s_actors = choices(actors, k=s_num)
            for actor in s_actors:
                movie.cast.add(actor)

        self.stdout.write(self.style.SUCCESS(f'{total} movies created!'))

