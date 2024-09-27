from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Item
from .forms import ItemForm

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Item Added',
                'An item has been added to the inventory.',
                'your_email@example.com',
                ['admin@example.com'],
                fail_silently=False,
            )
            return redirect('list_items')
    else:
        form = ItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})

def list_items(request):
    items = Item.objects.all()
    return render(request, 'inventory/list_items.html', {'items': items})

def deduct_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        item.quantity -= quantity
        item.save()
        send_mail(
            'Item Deducted',
            f'Item {item.name} quantity has been deducted.',
            'your_email@example.com',
            ['admin@example.com'],
            fail_silently=False,
        )
        return redirect('list_items')
    return render(request, 'inventory/deduct_item.html', {'item': item})
