def location(input):
    ''' A function that prints the location of where user would find specified Pokemon in Pokemon Sword.
        
        Parameters
        ----------
        
        input: string
            Name of Pokemon within eeveelutions_location dictionary 
        
        Returns
        ----------
        
        output: string
            Prints the location of specified Pokemon
        '''
        
    eeveelutions_location = {
            'Eevee': ['Bridge Field, East Lake Axewell, Motostoke Riverbank'],
            'Vaporeon': ['Lake of Outrage', "Giant's Mirror"],
            'Jolteon': ['Lake of Outrage', "Giant's Mirror"],
            'Flareon': ['Lake of Outrage', "Giant's Cap"],
            'Espeon': ['Lake of Outrage', 'Hammerlocke Hills'],
            'Umbreon': ['Lake of Outrage', "Giant's Mirror"],
            'Leafeon': ['Lake of Outrage', "Giant's Mirror"],
            'Glaceon': ['Lake of Outrage', 'Hammerlocke Hills'],
            'Sylveon': 'Lake of Outrage'     
        }
        
    # Output returns the value of specified key
    output = eeveelutions_location.get(input)

    return output