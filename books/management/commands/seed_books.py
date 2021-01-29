from random import choice, randint
from django.core.management.base import BaseCommand
from django_seed import Seed
from books.models import Book
from categories.models import Category
from people.models import Person

posters = [
    "https://www.ejanews.co.kr/news/photo/201305/2013053120008779.jpg",
    "https://lh3.googleusercontent.com/proxy/IV-Fy2OWxBe7g7obEO8asv9zkR2-aN0xJjCTndFOAK1tN2dti-jPb6hIcU5ihwdeBjB244WqGdFHwqgKzbgPberZ",
    "https://lh3.googleusercontent.com/proxy/HOLkCtpoV7kUpWWLjAmnM_uhvORsBSFz3wkt9UhxNgJvogYJsLddXmlnpthJHrYMrrfQt6G9gX-zGFGjaDzywSkKb_NGioOqMnrlMVYQKWusn6PFW18dEUxJwBdW0iLUzAl4Xl8Yf6sDCcLgvpnnSu1HkcXLqCcEzmga78wQOPpt_oX_fSFavNsY04Fgl1nuUWK5o6tRNfvi8RMYPe3vHz9lHfDQ2PF3Mkf4tqQ0fpfjRsaJ2zWgT3o8ufv_yg4lm2UKrxN1S0s_IDRUKZSepPjkEik9GSo60GfPL-ObaeFF-8rt8b0Vv6qipx7Wq7POxpqj2ikTaqY2FzJTplVu"
    "https://lh3.googleusercontent.com/proxy/IcKdrCfbiLjAFwa8kHeEw11SmQwxi4RmnX6sMPn3SYXxsSeZMMycibuB6JBuZj82B6Q6nxFnhnuVCsfaRlNVCsWJwmE5Sj8-thtoJ6DKQ0x4UUZDMe6hsOWU",
    "https://www.mediapia.co.kr/news/photo/202003/42913_70278_2917.jpg",
    "https://pds.joins.com/news/component/htmlphoto_mmdata/202009/04/6d607748-7e6c-4c80-8229-e56f40c84373.jpg",
    "https://i.pinimg.com/474x/6f/31/b3/6f31b3f26e56f59db54ea406abc8e1c4.jpg",
    "https://menu.mt.co.kr/moneyweek/thumb/2019/10/25/06/2019102514108031998_2.jpg",
    "https://www.m-i.kr/news/photo/201809/456424_275995_385.jpg",
    "https://lh3.googleusercontent.com/proxy/A48WYv4aqnK1jb_XBGpRzaSGAWJ7nA6U4XedJCHiF6HhSrcbQ6hYJ75o2LSdixxkjRaKtf8IGxcJt79vwC-6dXt8heJq0UA0y4R6KBaJNZzbwFA2RUX81_NnXyDX7fpwZIL0HjT5MUUH4av8LLZpkT7oL3Dw6QImhKT0zv_tFsOw9us-AN4F2Gq1YFjMJdS7LlUkCB6_jpYT_2D8_0GFSZ0umNZYpUm6BZlYx8m-mbhBrYaKuqq_GfxeQ_uS7hFmeApb7tjrFQVUm8OxjyDingZi2Ap5l2zUSdgdYobnu12r4YZPa0A41wYK4Kjct0fTGUrv0sefblH8wg",
    "https://www.samnparkers.com/upload/2017/11/1511166498930_%EC%A0%95%EC%84%9C%EC%A0%81%ED%98%91%EB%B0%95%ED%91%9C%EC%A7%80(%EB%9D%A0%EC%A7%80%EA%B0%88%EC%9D%B4).jpg",
    "https://lh3.googleusercontent.com/proxy/GDZH61s7kDmaOcYvtXBsugj-UMDVUKwe_wUnQ5eaR2tlLzlq5umYncYA7u162pY8IFrUWkS03Zw5G_Hze6p984eaY9R39PkhIVvXjwzni63mUPWBxmA",
    "https://i.pinimg.com/originals/e6/e1/d5/e6e1d5538961ba87e3b6144478788559.png",
    "https://bookthumb-phinf.pstatic.net/cover/073/606/07360621.jpg",
    "https://pds.joins.com/news/component/htmlphoto_mmdata/201707/21/5d0ad4ad-1e51-4cef-a941-7317457aad4a.jpg",
    "https://i.pinimg.com/564x/bf/69/78/bf6978d06ec0087b3f9d2502b25b3cbe.jpg",
    "https://file3.instiz.net/data/file3/2018/03/14/f/1/f/f1f58d99c9a2cff3b3d25d673e647aef.jpg",
    "https://file3.instiz.net/data/file3/2018/03/14/b/7/0/b707998b4c80cf8a613701b209fa931a.jpg",
    "https://i.pinimg.com/originals/7b/8f/1e/7b8f1e3287a38700d88d1596c1144c9b.jpg",
    "https://inmun360.culture.go.kr/upload/board/image/80/2365880_201910152018133770.jpg",
    "https://file.newswire.co.kr/data/datafile2/thumb_480/2008/12/2039103817_20081216105125_3331463201.jpg",
    "https://www.readersnews.com/news/photo/202003/98102_64265_2629.jpg",
    "https://t1.daumcdn.net/cfile/tistory/99ED374C5A844ABE1D",
    "https://image.kyobobook.co.kr/images/book/xlarge/298/x9788925560298.jpg",
    "https://bimage.interpark.com/goods_image/1/4/0/8/207571408g.jpg",
    "https://img.ridicdn.net/cover/1508005669/xxlarge",
    "https://pbs.twimg.com/media/DVQZNUMVQAEeGcM.jpg",
    "https://lh3.googleusercontent.com/proxy/ZVCNDER3aoZANMAN68_rG1qhkz59KqItBgV86-u0vIVV7btPXqex9oFVYtZvAsxfOYg0rAX9xLRiiaA5jHPTAYOJ90nIC66ndm0b2cxb1vLGNUS-R9CbmFPTdIneNQGjlAs3s66wJn-9Y9GvU1DM34L1GX9gZaQNjw",
    "https://t1.daumcdn.net/cfile/tistory/99809B4C5D1022D71C",
    "https://bookthumb-phinf.pstatic.net/cover/146/525/14652575.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnKBeqoDD3LEZOTR_K8YPClSDFmo02aFbz1A&usqp=CAU",
    "https://file3.instiz.net/data/file3/2018/03/14/1/4/a/14a84cd5ff55da8d632dd633795336e1.jpg",
    "https://post-phinf.pstatic.net/MjAxNzA1MzFfMTkz/MDAxNDk2MTg4OTI3NzY2.2apvPn4yoFgPG_vUT8ln87O2MFdkyvN94mBlAfHSqGkg.3szS8yHsFKe6jwBjak327ZcfOD0pSrJyWE84KqiPqLwg.JPEG/image_6612355171496188894882.jpg?type=w1200",
    "https://lh3.googleusercontent.com/proxy/wyuU-AAwdmOtHywW_jfxMTze0QVYt0Bc_Ja98O2cpQwD3SyhFcGAZMFMBPt0Q6KtlXcgA2I0hdghnHAmdQ53iark-KCg9cqKNESY0j5LuY_c_CyfOFxJzIUYxZThXH8bfAYx5LwZYXVMIl9qXhVxiVbjMri7Gzc",
    "https://blog.kakaocdn.net/dn/c6VXsR/btqBowXSjLb/KK2rNimPyflxdymvZ21y5K/img.png",
    "https://www.mrepublic.co.kr/news/photo/202101/61575_91512_2255.jpg",
    "https://www.dtnews24.com/news/photo/201809/525773_158969_82.jpg",
    "https://image.newstomato.com/newsimg/2017/12/20/795948/1.jpg",
    "https://lh3.googleusercontent.com/proxy/S0AxmvA0-wlkU7WHJizlN1Bxy74CdUL__cqByW3nHD4FKY86GyfOiW9U7ePuSWINwnC_r7aPU2_x43N7ZgduhF-uJxDYiPvCAqT7wJQ6nwV1HYOYwZaSezcfuFkG",
]

class Command(BaseCommand):

    help = "This command seeds books"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            help="How many books do you want to create?",
            default=10, type=int)

    def handle(self, *args, **options):
        total = int(options.get('total'))
        categories = Category.objects.all()
        writers = Person.objects.filter(kind=Person.KIND_WRITER)
        seeder = Seed.seeder()
        seeder.add_entity(
            Book, total, {
                "year": lambda x: seeder.faker.year(),
                "rating": lambda x: randint(1, 5),
                "category": lambda x: choice(categories),
                "writer": lambda x: choice(writers),
                "cover_image_url": lambda x: choice(posters)
            })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{total} books created!'))
