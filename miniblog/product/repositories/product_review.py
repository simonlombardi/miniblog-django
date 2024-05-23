from typing import List
from product.models import ProductReview
from product.repositories.product import ProductRepository
from django.contrib.auth.models import User

class ProductReviewRepository:
    def get_all() -> List[ProductReview]:
        return ProductReview.objects.all()
    
    def create(
            self,
            product_id: int,
            author: User,
            text: str,
            rating: int,
    ) -> ProductReview:
        product_repo = ProductRepository
        producto = product_repo.get_by_id(product_id)
        review = ProductReview.objects.create(
            product = producto,
            
        ) 