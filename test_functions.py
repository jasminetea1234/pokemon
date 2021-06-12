import location as loc
import pokedex_entry as dex
from pokemon import Pokemon

def test_Pokemon():
    Eevee = Pokemon('Eevee', ['Last Resort', 'Baton Pass', 'Stored Power', 'Substitute'])
    assert 'Last Resort', 'Substitute' in Eevee.Pokemon
    assert callable(Pokemon)
    
def test_fight():
    Vaporeon = Pokemon('Vaporeon', ['Scald', 'Ice Beam', 'Muddy Water', 'Signal Beam'], health = 0)
    assert Vaporeon.health == 0
    assert Vaporeon.moves[3] == 'Signal Beam'
    
def test_talk():
    Eevee = Pokemon('Eevee', ['Last Resort', 'Baton Pass', 'Stored Power', 'Substitute'])
    assert callable(Pokemon.talk)
    assert Eevee.talk == 'Eevee! uwu' or 'Eevee! owo' or 'Eevee! :D' or 'Eevee! :)' or 'Eevee! ʕ•ᴥ•ʔ' or 'Eevee! ~(˘▾˘~)' 
    
def test_location():
    eeveelutions_location = {'Eevee': ['Bridge Field, East Lake Axewell, Motostoke Riverbank']}
    assert callable(loc.location)
    assert isinstance(loc.location('Eevee'), list)
    assert loc.location('Eevee') == ['Bridge Field, East Lake Axewell, Motostoke Riverbank']
        
def test_pokedex_entry():
    eeveelutions_pokedex = {'Eevee': 'It has the ability to alter the composition' + \
                            'of its body to suit its surrounding environment.'}
    assert callable(dex.pokedex_entry)
    assert isinstance(dex.pokedex_entry('Eevee'), str)
    assert dex.pokedex_entry('Eevee') == 'It has the ability to alter the composition of its body to suit its surrounding environment.'