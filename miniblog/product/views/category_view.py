from django.shortcuts import redirect, render
from product.repositories.category import CategoryRepository

repo = CategoryRepository()

def category_list(request):
    categorias = repo.get_all()
    return render(request, 'categories/category_list.html', dict(categories = categorias))

def category_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        repo.create(nombre = name)
        return redirect('category_list')
    return render(request, 'categories/create.html')

def category_delete(request, id):
    categoria = repo.get_by_id(id = id)
    repo.delete(categoria)
    return redirect('category_list')

def category_update(request, id):
    category = repo.get_by_id(id = id)

    if request.method == "POST":
        name = request.POST.get('name')
    
        repo.update(category, nombre = name)
        return redirect('category_list')

    return render(request, 'categories/update.html', dict(category = category))
