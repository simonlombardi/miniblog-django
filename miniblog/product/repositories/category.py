from typing import List, Optional
from product.models import Category

class CategoryRepository:
    def get_all(self) -> List[Category]:
        return Category.objects.all()
    
    def create(self, nombre: str):
        return Category.objects.create(
            name=nombre,
        )

    def update(self, categoria: Category, nombre: str) -> Category:
        categoria.name = nombre
        categoria.save()

    def delete(self, categoria: Category):
        return categoria.delete()
    
    def get_by_id(self, id: int) -> Optional[Category]:
        try:
            category = Category.objects.get(id=id)
        except:
            category = None
        return category