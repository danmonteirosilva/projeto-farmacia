from django.contrib import admin
<<<<<<< HEAD
from .models import Balconista
<<<<<<< HEAD


admin.site.register(Balconista)
=======
from .models import Caixa
>>>>>>> refs/remotes/origin/master

admin.site.register(Balconista)
admin.site.register(Caixa)
# Register your models here.
=======
from .models import Balconista,Farmaceutico


admin.site.register(Balconista)
admin.site.register(Farmaceutico)


>>>>>>> efae385e7f2c20931325f446663af7ba0ddb6162
