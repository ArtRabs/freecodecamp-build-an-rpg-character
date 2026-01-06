full_dot = '●'
empty_dot = '○'

# 1. You should have a function named create_character.
def create_character(character_name, strength, intelligence, charisma):

    # Character Name

# 2. When create_character is called with a first argument that is not a string it should return The character name should be a string.
    if not isinstance(character_name, str):

        return "The character name should be a string"

# 3. When create_character is called with a first argument that is an empty string, it should return The character should have a name.
    if not character_name:

        return "The character should have a name"

# 4. When create_character is called with a first argument that is longer than 10 characters it should return The character name is too long.
# 5. The create_character function should not say that the character is too long when it's not longer than 10 characters.
    if len(character_name) > 10:    

        return "The character name is too long"

# 6. When create_character is called with a first argument that contains a space it should return The character name should not contain spaces.
    if " " in character_name:

        return "The character name should not contain spaces"

    # Character Stats

# 7. When create_character is called with a second, third or fourth argument that is not an integer it should return All stats should be integers.
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        
        return "All stats should be integers"

# 8. When create_character is called with a second, third or fourth argument that is lower than 1 it should return All stats should be no less than 1.
    if strength < 1 or intelligence < 1 or charisma < 1:

        return "All stats should be no less than 1"

# 9. When create_character is called with a second, third or fourth argument that is higher than 4 it should return All stats should be no more than 4.
    if strength > 4 or intelligence > 4 or charisma > 4:

        return "All stats should be no more than 4"

# 10. When create_character is called with a second, third or fourth argument that do not sum to 7 it should return The character should start with 7 points.
    if strength + intelligence + charisma != 7:
    
        return "The character should start with 7 points"

# 11. create_character('ren', 4, 2, 1) should return ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○.
    character = f"{character_name}\nSTR {(strength * full_dot) + ((10 - strength) * empty_dot)}\nINT {(intelligence * full_dot) + ((10 - intelligence) * empty_dot)}\nCHA {(charisma * full_dot) + ((10 - charisma) * empty_dot)}"

    return character

# 12. When create_character is called with valid values it should output the character stats as required.
