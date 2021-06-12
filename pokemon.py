import random
import sys
import time

def delay_print(s):
    
    # Not my function; got it from stackoverflow
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    # Prints one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon():
    ''' A Pokemon class with the following instance attributes.
    
    Instance Attributes
    -------------------
    
    name: string
        Pokemon's name is specified under '# Create Pokemon'
    moves: list
        Pokemon's list of moves they can use to fight, specified under '# Create Pokemon'
    health: default int 20
        Pokemon's default health used to fight, default is 20 health
    
    '''
   
    def __init__(self, name = '', moves = None, health = 20):
        self.name = name
        self.moves = moves
        self.health = health

    
    def fight(self, pokemon2):
        ''' A fight method used for two pokemon to fight.
        
        Parameters
        ----------
        
        self: string
            Self-selected Pokemon, will be the Pokemon that goes first, can choose any Pokemon from '# Create Pokemon'
            
        pokemon2: string
            Self-selected Pokemon, will be the Pokemon that goes second, can choose any Pokemon from '# Create Pokemon'
            
        '''

        # Used f-strings to print instance attributes
        print('~~~~~POKEMON BATTLE~~~~~')
        print(f'\n{self.name}')
        print('LVL/', random.randint(30,35))
        print('\nVS')
        print(f'\n{pokemon2.name}')
        print('LVL ', random.randint(30,35))
        print(f'Go {self.name}!')
        print(f'Go {pokemon2.name}!')

        time.sleep(2)
         
        while (self.health > 0) and (pokemon2.health > 0):
            print(f'\n{self.name}\t\tHLTH\t{self.health}')
            print(f'{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n')
             
            # User Pokemon's turn, prints moves and allows user to choose one
            print(f'What will {self.name} do?')
            for i, x in enumerate(self.moves):
                # Lists moveset with number next to it
                print(f'{i+1}.', x)
            index = int(input('Pick a move: '))
            delay_print(f'\n{self.name} used {self.moves[index - 1]}!')
                # Allows for number chosen to correctly match move
            time.sleep(1)

            # Determines damage done to pokemon2
            pokemon2.health -= random.randint(7, 9)
            
            time.sleep(1)
            print(f'\n{self.name}\t\tHLTH\t{self.health}')
            print(f'{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n')
            time.sleep(.5)

            # If Pokemon2 fainted, will break out of fighting loop
            if pokemon2.health < 1:
                pokemon2.health = 0
                delay_print('\n...' + pokemon2.name + ' fainted.')
                break

            # Pokemon2's turn, prints moves and allows user to choose one
            print(f'\nWhat will {pokemon2.name} do?')
            for i, x in enumerate(pokemon2.moves):
                print(f'{i+1}.', x)
            index = int(input('Pick a move: '))
            delay_print(f'\n{pokemon2.name} used {pokemon2.moves[index - 1]}!')
            time.sleep(1)

            # Determines damage done to user's pokemon
            self.health -= random.randint(7, 9)


            # If user's pokemon fainted, will break out of fighting loop
            if self.health < 1:
                self.health = 0
                delay_print('\n...' + self.name + ' fainted.')
                break
        
        delay_print('\nGreat job! Come back another time for another battle.')
        
   
    def talk(self):
        ''' A method that allows user to see specified Pokemon's greeting.
        
        Parameters
        ----------
        
        self: string
            Self-selected Pokemon from '# Create Pokemon'
            
        Returns
        ----------
       
       output: string
           Greeting said by specified Pokemon
      '''
        
        faces = ['uwu', 'owo', ':D', ':)', 'ʕ•ᴥ•ʔ', '~(˘▾˘~)']
        # output returns a string with the Pokemon's name and a randomly selected face from the faces list
        output = print(f'{self.name}! ' + random.choice(faces))
        
        return output

# Create Pokemon
Eevee = Pokemon('Eevee', ['Last Resort', 'Baton Pass', 'Stored Power', 'Substitute'])
Vaporeon = Pokemon('Vaporeon', ['Scald', 'Ice Beam', 'Muddy Water', 'Signal Beam'])
Jolteon = Pokemon('Jolteon', ['Thunderbolt', 'Volt Switch', 'Shadow Ball', 'Weather Ball'])
Flareon = Pokemon('Flareon', ['Double Edge', 'Facade', 'Flare Blitz', 'Superpower'])
Espeon = Pokemon('Espeon', ['Psychic', 'Dazzling Gleam', 'Morning Sun', 'Psyshock'])
Umbreon = Pokemon('Umbreon', ['Foul Play', 'Moonlight', 'Foul Play', 'Toxic'])
Leafeon = Pokemon('Leafeon', ['Leaf Blade', 'Razor Leaf', 'Energy Ball', 'Solar Beam'])
Glaceon = Pokemon('Glaceon', ['Freeze-Dry', 'Ice Beam', 'Ice Shard', 'Avalanche'])
Sylveon = Pokemon('Sylveon', ['Hyper Voice', 'Moonblast', 'Stored Power', 'Iron Tail'])




# Vaporeon.fight(Eevee) #unhashtag to get them to fight     