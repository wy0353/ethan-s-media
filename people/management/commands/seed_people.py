from random import choice
from django.core.management.base import BaseCommand
from django_seed import Seed
from people.models import Person

photos = [
    "https://i.pinimg.com/736x/b0/f6/ec/b0f6ec2d28bab32555d1ff77badb1112.jpg",
    "https://i.pinimg.com/originals/c3/94/5d/c3945d51a82107338d8cabb3c62fe068.jpg",
    "https://file3.instiz.net/data/file3/2018/01/29/9/8/c/98c1e823ab8d5543eaeeffc4c262ad16.jpg",
    "https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile5.uf.tistory.com%2Fimage%2F141FF344501F851412E147",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRj-q9iESsg06N1LlM_wxPPN1eSfI_1OujyCg&usqp=CAU",
    "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/mh-12-16-australians-1608143046.jpg?crop=0.231xw:0.462xh;0.731xw,0.0705xh&resize=640:*",
    "https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fdam%2Fimageserve%2F968210608%2F960x0.jpg%3Ffit%3Dscale",
    "https://images2.minutemediacdn.com/image/upload/c_crop,h_1357,w_2016,x_0,y_0/v1582008115/shape/mentalfloss/573683-gettyimages-1171013004.jpg?itok=66fUf5U8",
    "https://media.glamour.com/photos/5cf2a848ea090e3db8e89a3b/1:1/w_1344,h_1344,c_limit/GettyImages-457687980.jpg",
    "https://www.eatthis.com/wp-content/uploads//media/images/ext/491198872/Hugh-Jackman-weight-loss-tip.jpg",
    "https://hips.hearstapps.com/cos.h-cdn.co/assets/15/12/461614366.jpg?crop=1.0xw:1xh;center,top&resize=480:*",
    "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-459792838-1496268209.jpg?crop=0.997xw:0.757xh;0.00326xw,0.229xh&resize=480:*",
    "https://i.pinimg.com/736x/ba/28/ef/ba28ef28c5b72ab9e02c86e0da2b03c8.jpg",
    "https://lambsramblings.files.wordpress.com/2014/04/kaya-scodelario1.jpg",
    "https://img.culturacolectiva.com/content/2016/09/Handsome-Actors-jake-Gyllenhaal.jpg",
    "https://mblogthumb-phinf.pstatic.net/MjAyMDAyMDdfMTYw/MDAxNTgxMDg1NzUxMTUy.eV1iEw2gk2wt_YqPWe5F7SroOCkXJy2KFwmTDNzM0GQg.Z3Kd5MrDh07j86Vlb2OhAtcw0oVmGCMXtTDjoHyem9og.JPEG.7wayjeju/%EB%B0%B0%EC%9A%B0%ED%94%84%EB%A1%9C%ED%95%84%EC%82%AC%EC%A7%84_IMG7117.jpg?type=w800",
    "https://i.pinimg.com/736x/2c/2c/60/2c2c60b20cb817a80afd381ae23dab05.jpg",
    "https://mblogthumb-phinf.pstatic.net/MjAyMDAyMDdfODMg/MDAxNTgxMDg1ODA0MjM5.n92cLjlatR-jZmPEazuOVrpDFLJ_u6DX4KC1bspLCMog.Pbp9CqjIH1dhOXjOlwwzSFSkirrm8M4JeBilWvoQrJwg.JPEG.7wayjeju/%EB%B0%B0%EC%9A%B0%ED%94%84%EB%A1%9C%ED%95%84%EC%82%AC%EC%A7%84_IMG7124.jpg?type=w800",
    "https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99530A3B5BE7C18033",
    "https://mblogthumb-phinf.pstatic.net/MjAyMDAyMDdfMTg0/MDAxNTgxMDg1ODQzNjk1.Zg4taBuKiW1b8vRn7xd7s4EDhz7x7avletUkgN55xm8g.OjYtFokmE4AIlXEZTONvn1aRWiEtCnmiR_bTzB51s4Qg.JPEG.7wayjeju/%EB%B0%B0%EC%9A%B0%ED%94%84%EB%A1%9C%ED%95%84%EC%82%AC%EC%A7%84_IMG7129.jpg?type=w800",
    "https://cdn.imweb.me/upload/S20170720597014723fac6/193c177bb2a60.jpg",
    "https://photo.jtbc.joins.com/news/2019/01/16/20190116203411597.jpg",
    "https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F991CED4A5C9EE86F26",
    "https://thumbnail.forsnap.com/normal/crop/320x320/product/fd/2522/d8909c026361dd253edf93699b53a4a6.jpg",
    "https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FehODyV%2FbtqGgGmsPl7%2Fx7O3z9GCbVdvcB7BMDMQ11%2Fimg.jpg",
    "https://i.pinimg.com/736x/fb/03/06/fb0306599d767d8090859d50fa88bb29.jpg",
    "https://lh3.googleusercontent.com/proxy/Gju8FAoosEHKAbgVlkZzy44_X7WHmYu5fXcTQ9hvf14Rfhlomfo77sTmbyjJ3hMY3YEjStwuIc3P3Go6QXQobBgUfFyubpcI5c524rOHlE6HaiT7kUAwN9eemBLkgq-lvUYhhfi5L2BdYgITemxwFF7BW9mayjTRhj7e08rwnAbsL8BHoRl7sPATLwQk877f6r-9kP_IUhrio2EpV67EohmMImp9Nf00Yxh86CykDgvgphvdbElxYZQP7_RX2_J4Zsq5LwM3LU_aCm3Ca-QzQgWRzOf3tLLDkr5OVYEs6bkbNzM8BrP4dQXldKdEtjV7s1BoFuI",
    "https://images.chosun.com/resizer/MbNKralpUHbyZ-ccWvPqNXBiE8c=/464x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/UJKXLJ22PS7XWRYNMNKGT2DPFM.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmhhbsvjl-dGQwkSjR08a0wtDbF50cnoz5og&usqp=CAU",
]

class Command(BaseCommand):

    help = "This command seeds people"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total", help="How many people do you want to create?", default=5)

    def handle(self, *args, **options):
        total = int(options.get('total'))
        seeder = Seed.seeder()
        seeder.add_entity(Person, total, {
            "name": lambda x: seeder.faker.name(),
            "kind": lambda x: choice([Person.KIND_ACTOR, Person.KIND_DIRECTOR, Person.KIND_WRITER])
            "photo_url": lambda x: choice(photos)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{total} people created!'))
