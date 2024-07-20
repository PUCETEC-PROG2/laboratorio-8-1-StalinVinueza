from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.template import loader
from pokedex.forms import PokemonsForm
from .models import Pokemon

def index(request):
    ##pokemons = Pokemon.objects.all() ##select*from pokedex_pokemon
    pokemons = Pokemon.objects.order_by('name') ##select*from pokedex_pokemon order by type
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, pokemon_id):
    ## select *from pokedex_pokemon where id ='pokemon_id
    pokemon=Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonsForm(request.POST, request.FILES)
        if form. is_valid():
            form.save()
            return redirect('pokedex:index')
    else: 
        form = PokemonsForm()
        
    return render(request, 'add_pokemon.html', {'form: form'})