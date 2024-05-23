from typing import List
from product.models import ProductReview
from product.repositories.product import ProductRepository
from django.contrib.auth.models import User

class ProductReviewRepository:
    def get_all(self) -> List[ProductReview]:
        return ProductReview.objects.all()
    
    def create(
            self, product_id: int, author: User, text: str, rating: int,
    ) -> ProductReview:
        product_repo = ProductRepository()
        producto = product_repo.get_by_id(id = product_id)
        review = ProductReview.objects.create(
            product = producto,
            author = author,
            text = text,
            rating = rating,
        ) 
        return review