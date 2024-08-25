from random import randint as rand
import inflect
p = inflect.engine()

def main():
    while True:
        man_ran = input("     First, lets roll some stats. Do you want to stat assignment to be random or manual? ")
        if man_ran.lower().strip() == "random":
            stats = roll_stats_random()
            break
        elif man_ran.lower().strip() == "manual":
            stats = roll_stats_manual()
            print("    These are your stats:")
            for s in stats:
                print(f"            {s}: {stats[s]}")
            break
        else:
            print("    Please choose random or manual.")
            pass
    character_class = choose_class()
    character_saves = generate_saves(character_class)
    character_race = choose_race()
    asi_updates = race_asi[character_race]
    if character_race == "Half-elf":
        print("     You can add 1 to two of the following: Strength, Dexterity, Constitution, Intelligence or Wisdom.")
        chosen_abilities = input("    Which do you want to choose? Separate input by commas please. ").split(",")
        choices = [a.strip().title() for a in chosen_abilities]
        stats.update({"Charisma": stats["Charisma"] + 2})
        stats.update({choices[0]: stats[choices[0]] + 1})
        stats.update({choices[1]: stats[choices[1]] + 1})
    else:
        for a in asi_updates:
            stats.update({a[0]: stats[a[0]] + a[1]})
        print("    These are your updated stats.")
    for s in stats:
        print(f"            {s}: {stats[s]}")
    skills = choose_skills(character_class)
    ability_mods = {}
    for s in stats:
        ability_mods[s] = as_mods[stats[s]]
    for m in skill_mods:
        skill_mods.update({m: ability_mods[skill_mods[m]]})
    for x in skills:
        skill_mods.update({x: skill_mods[x] +3})
    for y in character_saves:
        character_saves.update({y: character_saves[y] + ability_mods[y]})
    hp = class_dice[character_class] + ability_mods["Constitution"]
    name = choose_name()
    print("    This is your character:")
    print(f"        Name: {name} \n        Race: {character_race} \n        Class: {character_class} \n        HP: {hp} \n        Proficiency bonus: 3")
    print("        Ability scores:")
    for s in stats:
        print(f"            {s}: {stats[s]} ({as_mods[stats[s]]})")
    print("        Saves:")
    for b in character_saves:
        print(f"            {b}: {character_saves[b]}")
    print("        Skills:")
    for k in skill_mods:
        print(f"            {k}: {skill_mods[k]}")

class_dice = {       #dictionary of classes and their hit dice, used in main to generate hp
    "Barbarian": 12,
    "Bard": 8,
    "Cleric": 8,
    "Druid": 8,
    "Fighter": 10,
    "Monk": 8,
    "Paladin": 10,
    "Ranger": 10,
    "Rogue": 8,
    "Sorcerer": 6,
    "Warlock": 8,
    "Wizard": 6
}

as_mods = {        #list of ability scores and their corresponding modifiers, used in main to update skill_mods
    1: -5,
    2: -4,
    3: -4,
    4: -3,
    5: -3,
    6: -2,
    7: -2,
    8: -1,
    9: -1,
    10: 0,
    11: 0,
    12: 1,
    13: 1,
    14: 2,
    15: 2,
    16: 3,
    17: 3,
    18: 4,
    19: 4,
    20: 5,
    21: 5
}

skill_mods =  {                      #dictionary of skills and their ability scores, used in main to update skill_mods
    "Acrobatics": "Dexterity",
    "Animal Handling": "Wisdom",
    "Arcana": "Intelligence",
    "Athletics": "Strength",
    "Deception": "Charisma",
    "History": "Intelligence",
    "Insight": "Wisdom",
    "Intimidation": "Charisma",
    "Investigation": "Intelligence",
    "Medicine": "Wisdom",
    "Nature": "Intelligence",
    "Perception": "Wisdom",
    "Performance": "Charisma",
    "Persuasion": "Charisma",
    "Religion": "Intelligence",
    "Sleight of Hand": "Dexterity",
    "Stealth": "Dexterity",
    "Survival": "Wisdom"
}

class_skills = {            #dictionary of classes skills to choose from and number of choices, used in choose_skills
    "Barbarian": [2, "Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
    "Bard": [3, "Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception",
    "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception",
    "Performance", "Persuasion", "Religion", "Sleight Of Hand", "Stealth", "Survival"],
    "Cleric": [2, "History", "Insight", "Medicine", "Persuasion", "Religion"],
    "Druid": [2, "Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
    "Fighter": [2, "Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
    "Monk": [2, "Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
    "Paladin": [2, "Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
    "Ranger": [3, "Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
    "Rogue": [4, "Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance",
    "Persuasion", "Sleight of Hand", "Stealth"],
    "Sorcerer": [2, "Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
    "Warlock": [2, "Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
    "Wizard": [2, "Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
}

race_asi = {                #dictionary of races and their ability score increases at 1st level, used in main to update ability_mods
    "Dragonborn": [("Strength", 2), ("Charisma", 1)],
    "Dwarf": [("Constitution", 2)],
    "Elf": [("Dexterity", 2)],
    "Gnome": [("Intelligence", 2)],
    "Half-elf": [("Charisma", 2), ("Choice", 1), ("Choice", 1)],
    "Halfling": [("Dexterity", 2)],
    "Half-orc": [("Strength", 2), ("Constitution", 1)],
    "Human": [("Strength", 1), ("Dexterity", 1), ("Constitution", 1), ("Intelligence", 1), ("Wisdom", 1), ("Charisma", 1)],
    "Tiefling": [("Charisma", 2), ("Intelligence", 1)]
}

saving_throws = {        #dictionary of classes and save proficiencies, used in generate_saves
    "Barbarian": ["Strength", "Constitution"],
    "Bard": ["Dexterity", "Charisma"],
    "Cleric": ["Wisdom", "Charisma"],
    "Druid": ["Intelligence", "Wisdom"],
    "Fighter": ["Strength", "Constitution"],
    "Monk": ["Strength", "Dexterity"],
    "Paladin": ["Wisdom", "Charisma"],
    "Ranger": ["Strength", "Dexterity"],
    "Rogue": ["Dexterity", "Intelligence"],
    "Sorcerer": ["Constitution", "Charisma"],
    "Warlock": ["Wisdom", "Charisma"],
    "Wizard": ["Intelligence", "Wisdom"]
}

def generate_saves(c):   #generates the character's save proficiences based on class selection
    saves = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0,
    }
    save_proficiencies = saving_throws[c]
    for save in save_proficiencies:
        saves.update({save: saves[save] + 3})
    return saves


def choose_skills(c):    #gives user a choice of skills based on class selection
    print(f"    Next, pick your skills. You can choose {class_skills[c][0]} from the following: " + p.join(class_skills[c][1:]) + ".")
    while True:
        chosen_skills = input("    Which ones do you want? Separate input by commas please. ").split(",")
        character_skills = [s.strip().title() for s in chosen_skills]
        if set(character_skills).issubset(class_skills[c]) and len(character_skills) == class_skills[c][0]:
            return character_skills
        else:
            print(f"    Please choose {class_skills[c][0]} from the available skills.")
            pass

def choose_name():     #asks user for a character name
    name = input("    Finally, pick a name. What's your character's name? ")
    return name

def choose_class():    #gives user a choice of basic dnd classes, returns chosen class
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    print(f"    Next, choose your class. Available classes: " + p.join(classes) + ".")
    while True:
        character_class = input("    What class do you want to be? ").title().strip()
        if character_class.title().strip() in classes:
            return character_class
        else:
            print("    Please choose from the available classes.")
            pass

def choose_race():   #gives user a choice of basic dnd races, returns chosen race
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-elf", "Halfling", "Half-orc", "Human", "Tiefling"]
    print(f"    Next, choose your race. The available races are: "  + p.join(races) + ".")
    while True:
        character_race = input("    What race do you want to be? ").capitalize().strip()
        if character_race.capitalize().strip() in races:
            return character_race
        else:
            print("    Please choose from the available races.")
            pass

def roll_stats_random():    #rolls stats and assigns them to attributes randomly
    attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    stats = {}
    for a in attributes:
        stats.update({a: roll_for_stats()})
    for s in stats:
        print(f"        {s}: {stats[s]}")
    return stats

def roll_stats_manual():
    rolls = []
    stats = {
        "Strength":0,
        "Dexterity":0,
        "Constitution":0,
        "Intelligence":0,
        "Wisdom":0,
        "Charisma":0
    }
    counter=0
    while counter < 6:
        rolls.append(roll_for_stats())
        counter+=1
    print("    Your rolls are: " + p.join(rolls) + ".")
    print("    Please assign them to the following attributes: Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma.")
    for s in stats:
        assignment = int(input(s + ": "))
        if assignment in rolls:
            stats.update({s: assignment})
            rolls.remove(assignment)
        else:
            print("    Not one of your rolls. Choose again.")
            assignment = int(input(s + ": "))
            stats.update({s: assignment})
            rolls.remove(assignment)
    return stats

def roll_for_stats():   #rolls 4 d6 and drops the lowest, outputs result
    stat_rolls = []
    counter = 0
    while counter < 4:
        stat_rolls.append(rand(1,6))
        counter+=1
    stat_rolls.sort()
    stat_rolls.remove(stat_rolls[0])
    score = stat_rolls[0] + stat_rolls[1] + stat_rolls[2]
    return score

main()

#bug in half-elf skills - needs to catch no comma -- while statement
#bug in manual stat rolling - make correction loop infinite