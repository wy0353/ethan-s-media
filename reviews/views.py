from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from . import models as review_models
from movies import models as movie_models
from books import models as book_models


class ReviewCreateView(View):

    def post(self, request):
        try:
            pk = request.POST.get("pk", None)
            category = request.POST.get("category", None)
            comment = request.POST.get("comment", None)
            rating = request.POST.get("rating", None)
            user = request.user
            ins = None

            review = review_models.Review()
            review.created_by = request.user
            review.text = comment
            review.rating = int(rating)
            if category == "movie":
                review.movie = movie_models.Movie.objects.get(pk=pk)
                review.save()
                return redirect(reverse("movies:movie", kwargs={"pk": pk}))
            elif category == 'book':
                review.book = book_models.Book.objects.get(pk=pk)
                review.save()
                return redirect(reverse("books:book", kwargs={"pk": pk}))
        except Exception as e:
            print(e)
            return redirect(reverse("core:home"))


class ReviewDeleteView(View):
    def post(self, request):
        try:
            print(request.POST)
            category = request.POST.get("category", None)
            obj_pk = request.POST.get("obj_pk", None)
            review_pk = request.POST.get("pk", None)
            review_models.Review.objects.get(pk=review_pk).delete()
            
            if category == "movie":
                return redirect(reverse("movies:movie", kwargs={"pk": obj_pk}))
            elif category == 'book':
                return redirect(reverse("books:book", kwargs={"pk": obj_pk}))
        except Exception as e:
            return redirect(reverse("core:home"))