full_dot = "●"
empty_dot = "○"
full_bar = empty_dot * 10
def create_character(name, strength, intelligence, charisma):
    stats = [strength, intelligence, charisma]
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    for stat in stats:
        if not isinstance(stat, int):
            return "All stats should be integers"
        if stat < 1:
            return "All stats should be no less than 1"
        if stat > 4:
            return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"
    str_dots = (full_dot * strength) + (empty_dot * (10 - strength))
    int_dots = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    char_dots = (full_dot * charisma) + (empty_dot * (10 - charisma))
    
    return f"{name}\nSTR {str_dots}\nINT {int_dots}\nCHA {char_dots}"

my_character = create_character("ren", 4, 2, 1)
print(my_character)
