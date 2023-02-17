from django.contrib import admin
from .models import User
from .models import Sheba
from cart.models import Cart
from cartanother.models import Order
from cartanother.models import Ordernew
from cartanother.models import Cartanothernew
# Register your models here.
admin.site.register(User)
admin.site.register(Sheba)
admin.site.register(Cart)
admin.site.register(Ordernew)
admin.site.register(Cartanothernew)