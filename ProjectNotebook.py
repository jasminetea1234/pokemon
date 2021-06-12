#!/usr/bin/env python
# coding: utf-8

# # Project Description

# I made a text based Pokemon simulator where the user can battle two Pokemon. A list of available Pokemons and their moveset are provided below. Please make sure to run that cell before calling the fight! I also have another method within the class that allows the user to see the greeting of a specified Pokemon. I have two extra functions that allows the user to check the locations of where a specified Pokemon will spawn as well as their Pokedex description. 
# 
# Whenever I say pokemon1 or pokemon2, please refer to the list titled '# Pokemon List' to choose Pokemon.
# 
# - In order to run the battle, type pokemon1.fight(pokemon2) and replace *pokemon1* with the Pokemon that will go first and *pokemon2* with the Pokemon that will go second.
# - To use the talk method, type *pokemon1.talk()* to see a Pokemon's greeting and replace pokemon1 with a Pokemon of your choosing.
# - To see the location of a specific Pokemon, type *location('pokemon1')* and replace pokemon1 with a Pokemon of your choosing.
# - To see the Pokedex entry of a specific Pokemon, type *pokedex_entry('pokemon1')* and replace pokemon1 with a Pokemon of your choosing.

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


import random, sys, time
from my_module import pokemon, location as loc, pokedex_entry as dex
from my_module.pokemon import Pokemon

# Pokemon List
Eevee = Pokemon('Eevee', ['Last Resort', 'Baton Pass', 'Stored Power', 'Substitute'])
Vaporeon = Pokemon('Vaporeon', ['Scald', 'Ice Beam', 'Muddy Water', 'Signal Beam'])
Jolteon = Pokemon('Jolteon', ['Thunderbolt', 'Volt Switch', 'Shadow Ball', 'Weather Ball'])
Flareon = Pokemon('Flareon', ['Double Edge', 'Facade', 'Flare Blitz', 'Superpower'])
Espeon = Pokemon('Espeon', ['Psychic', 'Dazzling Gleam', 'Morning Sun', 'Psyshock'])
Umbreon = Pokemon('Umbreon', ['Foul Play', 'Moonlight', 'Foul Play', 'Toxic'])
Leafeon = Pokemon('Leafeon', ['Leaf Blade', 'Razor Leaf', 'Energy Ball', 'Solar Beam'])
Glaceon = Pokemon('Glaceon', ['Freeze-Dry', 'Ice Beam', 'Ice Shard', 'Avalanche'])
Sylveon = Pokemon('Sylveon', ['Hyper Voice', 'Moonblast', 'Stored Power', 'Iron Tail'])


# In[2]:


# Get two Pokemon to fight!
pokemon1.fight(pokemon2)


# In[ ]:


# See what a Pokemon says!
pokemon1.talk()


# In[ ]:


# See the location of a Pokemon!
loc.location('pokemon1')


# In[4]:


# See the Pokedex entry of a Pokemon!
dex.pokedex_entry('pokemon1')


# ## Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. Your Python Background
# 2. How your project went above and beyond the requirements of the project and/or how you challenged yourself to learn something new with the final project

# I had absolutely no programming experience before this class. My project went beyond the requirements of the project because I challenged myself to use code sourced from the internet and successfully implement it into my own code mostly because I wanted the text to appear character by character just like in the older Pokemon games. I also used the enumerate() function that we didn't learn in class in my code.
