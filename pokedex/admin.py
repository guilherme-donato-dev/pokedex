from django.contrib import admin
from pokedex.models import Pokemon
# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display =  ('name', 'type')
    #usado para listar os campos que vão aparecer no registro do carro

admin.site.register(Pokemon, PokemonAdmin)