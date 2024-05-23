from django.views import View
from django.shortcuts import render, redirect
from product.repositories.product_review import ProductReviewRepository
from product.repositories.product import ProductRepository

class ProductReviewView(View):
    def get(self, request):
        repo = ProductReviewRepository()
        reviews = repo.get_all()
        return render(request,"product_review/list.html"), dict(reviews = reviews)

class ProductReviewCreateView(View):
    def get(self, request):
        products = ProductRepository.get_all()
        return render(request, "product_review_create.html", dict(products = products))
    
    def post(self, request):
        product_id = request.POST.get("id_producto")
        review = request.POST.get("opinion")
        value = request.POST.get("valoracion")
        user = request.user
        ProductReviewRepository.create(
            product_id=product_id,
            author=user,
            text=review,
            rating=value
        )
        return redirect("product_reviews")