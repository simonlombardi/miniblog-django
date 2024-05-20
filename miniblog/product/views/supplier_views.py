from django.shortcuts import redirect, render

from product.repositories.supplier import SupplierRepository

repo = SupplierRepository()

def supplier_list(request):
    suppliers = repo.get_all()
    return render(
        request,
        'supplier/list.html',
        dict(
            suppliers = suppliers
        )
    )

def supplier_detail(request, id):
    supplier = repo.get_by_id(id=id)
    return render(
        request,
        'supplier/detail.html',
        {"supplier":supplier}
    )
def supplier_delete(request, id):
    supplier = repo.get_by_id(id=id)
    repo.delete(supplier=supplier)
    return redirect('supplier_list')

def supplier_update(request, id):
    supplier = repo.get_by_id(id = id)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        repo.update(supplier = supplier, nombre = name, direccion = address, numero = phone)
        return redirect('supplier_detail', supplier.id)

    return render(request, 'supplier/update.html', dict(supplier = supplier))

def supplier_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        supplier_nuevo = repo.create(nombre = name, direccion = address, numero = phone)
        return redirect('supplier_detail', supplier_nuevo.id)
    return render(request, 'supplier/create.html')