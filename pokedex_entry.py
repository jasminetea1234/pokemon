def pokedex_entry(input):
        ''' A function used to see specified Pokemon's Pokedex entry in Pokemon Sword.
        
        Parameters
        ----------
        
        input: string
            Name of Pokemon within eeveelutions_pokedex dictionary
            
        Returns
        ----------
        
        output: string
            Pokedex entry of specified Pokemon
        '''
       
        eeveelutions_pokedex = {
            'Eevee': 'It has the ability to alter the composition of its body to suit its surrounding environment.',
            'Vaporeon': "When Vaporeon's fins begin to vibrate," + \
                        'it is a sign that rain will come within a few hours.',
            'Jolteon': 'If it is angered or startled,' + \
                        'the fur all over its body bristles like sharp needles that pierce foes.',
            'Flareon': 'Once it has stored up enough heat,' + ' ' + \
                        "this Pokemon's body temperature can reach up to 1700 degrees Fahreinheit.",
            'Espeon': "By reading air currents, it can predict things such as the weather or its foe's next move.",
            'Umbreon': 'When this Pokemon becomes angry, its pores secrete a poisonous sweat,' + \
                        "which it sprays at its opponent's eyes.",
            'Leafeon': "Galarians favor the distinctive aroma that drifts from this Pokemon's leaves." + \
                        'There is a popular perfume made using that scent.',
            'Glaceon': 'Any who become captivated by the beauty of the snowfall that' + \
                        'Glaceon creates will be frozen before they know it.',
            'Sylveon': 'By releasing enmity-erasing waves from its ribbonlike feelers, Sylveon stops any conflict.'
        }
        
        # Output returns the value of the specified key
        output = eeveelutions_pokedex.get(input)
        
        return output
        
        # to call this function, use 'pokedex_entry('Eevee')'