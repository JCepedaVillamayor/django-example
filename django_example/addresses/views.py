from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.views import View


class AddressView(View):
    def get(self, request):
        all_users = User.objects.select_related().order_by("id").all()
        paginator = Paginator(all_users, 10)
        try:
            index = int(request.GET.get("page", "1"))
        except ValueError:
            index = 1
        if index > len(paginator.page_range):
            index = len(paginator.page_range)
        elif index <= 0:
            index = 1
        max_index = len(paginator.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]
        users = paginator.get_page(index)
        return render(
            request, "listing.html", {"users": users, "page_range": page_range}
        )
