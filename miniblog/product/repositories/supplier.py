from typing import List, Optional
from product.models import Supplier

class SupplierRepository:
    def get_all(self) -> List[Supplier]:
        return Supplier.objects.all()
    
    def create(self, nombre: str, direccion: str, numero: str):
        return Supplier.objects.create(
            name = nombre,
            address = direccion,
            phone = numero
        )

    def update(self, supplier: Supplier, nombre: str, direccion: str, numero: str) -> Supplier:
        supplier.name = nombre
        supplier.address = direccion
        supplier.phone = numero
        supplier.save()

    def delete(self, supplier: Supplier):
        return supplier.delete()
    
    def get_by_id(self, id: int) -> Optional[Supplier]:
        try:
            supplier = Supplier.objects.get(id=id)
        except:
            supplier = None
        return supplier