full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    # --- Phase 1: Name Validation ---
    if type(name) is not str:
        return 'The character name should be a string'
    
    if name == '':
        return 'The character should have a name'
    
    if len(name) > 10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces'

    # --- Phase 2: Stat Validation ---
    stats = {'STR': strength, 'INT': intelligence, 'CHA': charisma}
    
    # We use one loop to check the individual rules for each stat
    for stat in stats.values():
        if type(stat) is not int:
            return 'All stats should be integers'
        
        if stat < 1:
            return 'All stats should be no less than 1'
        
        if stat > 4:
            return 'All stats should be no more than 4'

    # We check the grand total OUTSIDE the loop
    if sum(stats.values()) != 7:
        return 'The character should start with 7 points'

    # --- Phase 3: Building the Output ---
    character_string = name
      
    for key, stat in stats.items():
        character_string += f'\n{key} {full_dot * stat}{empty_dot * (10 - stat)}'

    return character_string

# Test it out!
print(create_character('ren', 4, 2, 1))