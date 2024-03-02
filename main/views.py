from django.shortcuts import render
from django.utils import timezone
from .models import Product, Group
from random import shuffle
from django.shortcuts import get_object_or_404
from django.http import HttpResponse





def users_to_groups(request, product_id):
    products_on = Product.objects.all()

    if not products_on:
        return HttpResponse('No products')


    product = get_object_or_404(Product, id=product_id)
    user = request.user


    if product.start_date > timezone.now():
        groups = Group.objects.filter(product=product)


        if user in groups.values_list('members', flat=True):
            return render(request, 'already_in_group.html')


        if not groups:
            group = Group.objects.create(product=product, name='Group 1')
            group.members.add(user)
        else:
            redistribute_groups(groups, user)


def redistribute_groups(groups, user):
    num_groups = len(groups)
    total_users = sum(groups.values_list('members__count', flat=True))

    target_group_size = total_users // num_groups

    shuffle(groups)

    for group in groups:
        current_group_size = group.members.count()

        if current_group_size < target_group_size:
            group.members.add(user)
            break

    for group in groups:
        group.save()