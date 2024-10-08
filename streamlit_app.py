import streamlit as st

"""
# Battler Calculator!

"""

class Creature:
    def __init__(self, level, health, physical_attack, magic_attack, armor, magic_resistance, faith, speed):
        self.level = level
        self.health = health
        self.physical_attack = physical_attack
        self.magic_attack = magic_attack
        self.armor = armor
        self.magic_resistance = magic_resistance
        self.faith = faith
        self.speed = speed

    def calculate_damage(self, move, defender):
        attack_stat = self.physical_attack if move.type == MoveType.Physical else self.magic_attack
        defense_stat = defender.armor if move.type == MoveType.Physical else defender.magic_resistance
        damage = move.power * (attack_stat / defense_stat) * (self.level / defender.level) + 2
        return int(damage)

    def calculate_healing(self, move):
        healing = (move.power * self.faith) / ((self.level / 3.0) + 1)
        return int(healing)

    def attack(self, move, defender):
        if move.is_healing_move:
            healing_amount = self.calculate_healing(move)
            self.health += healing_amount
            return int(healing_amount)
        else:
            damage_amount = self.calculate_damage(move, defender)
            defender.health -= damage_amount
            return int(damage_amount)


class Move:
    def __init__(self, name, power, move_type, is_healing_move):
        self.name = name
        self.power = power
        self.type = move_type
        self.is_healing_move = is_healing_move


class MoveType:
    Physical = 1
    Magic = 2

def main():

    # Initialize attack_outputs list if not already present in session_state
    if "attack_outputs" not in st.session_state:
        st.session_state.attack_outputs = []

    if "turn_counter" not in st.session_state:
        st.session_state.turn_counter = 0

    if "turn_count" not in st.session_state:
        st.session_state.turn_count = 1

    if "creature1" not in st.session_state:
        st.session_state.creature1 = Creature(10, 100, 20, 30, 15, 10, 5, 50)

    if "creature2" not in st.session_state:
        st.session_state.creature2 = Creature(8, 80, 15, 25, 12, 8, 3, 60)

    move1 = Move("Fireball", 40, MoveType.Magic, False) # Define move1
    move2 = Move("Heal", 30, MoveType.Magic, True) # Define move2
    move3 = Move("Tackle", 20, MoveType.Physical, False) # Define move3
    move4 = Move("Firebolt", 40, MoveType.Magic, False)  # Define move4
    move5 = Move("Cure", 30, MoveType.Magic, True) # Define move5
    move6 = Move("Rush", 20, MoveType.Physical, False) # Define move6

    st.sidebar.header("Creature 1")
    creature1_level = st.sidebar.number_input("C1 Level", min_value=1, value=100)
    creature1_health = st.sidebar.number_input("C1 Health", min_value=1, value=100)
    creature1_physical_attack = st.sidebar.number_input("C1 Physical Attack", min_value=1, value=100)
    creature1_magic_attack = st.sidebar.number_input("C1 Magic Attack", min_value=1, value=100)
    creature1_armor = st.sidebar.number_input("C1 Armor", min_value=1, value=100)
    creature1_magic_resistance = st.sidebar.number_input("C1 Magic Resistance", min_value=1, value=100)
    creature1_faith = st.sidebar.number_input("C1 Faith", min_value=1, value=100)
    creature1_speed = st.sidebar.number_input("C1 Speed", min_value=1, value=100)

    st.session_state.creature1 = Creature(creature1_level, creature1_health, creature1_physical_attack, creature1_magic_attack, creature1_armor, creature1_magic_resistance, creature1_faith, creature1_speed)

    st.sidebar.header("Creature 2")
    creature2_level = st.sidebar.number_input("C2 Level", min_value=1, value=100)
    creature2_health = st.sidebar.number_input("C2 Health", min_value=1, value=100)
    creature2_physical_attack = st.sidebar.number_input("C2 Physical Attack", min_value=1, value=100)
    creature2_magic_attack = st.sidebar.number_input("C2 Magic Attack", min_value=1, value=100)
    creature2_armor = st.sidebar.number_input("C2 Armor", min_value=1, value=100)
    creature2_magic_resistance = st.sidebar.number_input("C2 Magic Resistance", min_value=1, value=100)
    creature2_faith = st.sidebar.number_input("C2 Faith", min_value=1, value=100)
    creature2_speed = st.sidebar.number_input("C2 Speed", min_value=1, value=100)

    st.session_state.creature2 = Creature(creature2_level, creature2_health, creature2_physical_attack, creature2_magic_attack, creature2_armor, creature2_magic_resistance, creature2_faith, creature2_speed)

    st.title("Test Battle")

    if st.button("Reset"):
    # Clears all st.cache_resource caches:
        st.cache_resource.clear()
        st.cache_data.clear()
        st.session_state.attack_outputs = []
        st.session_state.turn_counter = 0
        st.session_state.turn_count = 1

    if st.button("Start"):
    # Clears all st.cache_resource caches:
        check_speed(st.session_state.creature1, st.session_state.creature2, st.session_state.turn_count)
        st.session_state.turn_counter += 1
        st.session_state.turn_count += 1

    col1, col2 = st.columns(2)

    with col1:
        st.header("Creature 1")
        if st.button(f"{move1.name}"):
            output = attack_one(st.session_state.creature1, st.session_state.creature2, move1)
            st.session_state.attack_outputs.append(output)
            check_win_condition(st.session_state.creature1, st.session_state.creature2)

            if st.session_state.turn_counter == 2:
                check_speed(st.session_state.creature1, st.session_state.creature2, st.session_state.turn_count)
                st.session_state.turn_counter = 1
                st.session_state.turn_count += 1
            else:
                st.session_state.turn_counter += 1

        if st.button(f"{move2.name}"):
            output = attack_two(st.session_state.creature1, st.session_state.creature2, move2)
            st.session_state.attack_outputs.append(output)
            check_win_condition(st.session_state.creature1, st.session_state.creature2)

            if st.session_state.turn_counter == 2:
                check_speed(st.session_state.creature1, st.session_state.creature2, st.session_state.turn_count)
                st.session_state.turn_counter = 1
                st.session_state.turn_count += 1
            else:
                st.session_state.turn_counter += 1

        if st.button(f"{move3.name}"):
            output = attack_three(st.session_state.creature1, st.session_state.creature2, move3)
            st.session_state.attack_outputs.append(output)
            check_win_condition(st.session_state.creature1, st.session_state.creature2)

            if st.session_state.turn_counter == 2:
                check_speed(st.session_state.creature1, st.session_state.creature2, st.session_state.turn_count)
                st.session_state.turn_counter = 1
                st.session_state.turn_count += 1
            else:
                st.session_state.turn_counter += 1

    with col2:
        st.header("Creature 2")
        if st.button(f"{move4.name}"):
            output = attack_four(st.session_state.creature2, st.session_state.creature1, move4)
            st.session_state.attack_outputs.append(output)
            check_win_condition(st.session_state.creature1, st.session_state.creature2)

            if st.session_state.turn_counter == 2:
                check_speed(st.session_state.creature1, st.session_state.creature2, st.session_state.turn_count)
                st.session_state.turn_counter = 1
                st.session_state.turn_count += 1
            else:
                st.session_state.turn_counter += 1

        if st.button(f"{move5.name}"):
            output = attack_five(st.session_state.creature2, st.session_state.creature1, move5)
            st.session_state.attack_outputs.append(output)
            check_win_condition(st.session_state.creature1, st.session_state.creature2)

            if st.session_state.turn_counter == 2:
                check_speed(st.session_state.creature1, st.session_state.creature2, st.session_state.turn_count)
                st.session_state.turn_counter = 1
                st.session_state.turn_count += 1
            else:
                st.session_state.turn_counter += 1

        if st.button(f"{move6.name}"):
            output = attack_six(st.session_state.creature2, st.session_state.creature1, move6)
            st.session_state.attack_outputs.append(output)
            check_win_condition(st.session_state.creature1, st.session_state.creature2)

            if st.session_state.turn_counter == 2:
                check_speed(st.session_state.creature1, st.session_state.creature2, st.session_state.turn_count)
                st.session_state.turn_counter = 1
                st.session_state.turn_count += 1
            else:
                st.session_state.turn_counter += 1

    st.write("Attack Logs:")
    for output in st.session_state.attack_outputs:
        st.write(output)


def attack_one(attacker, defender, move):
    damage = attacker.attack(move, defender)
    return f"Creature 1 dealt {damage} damage to Creature 2. Creature 2 now has {defender.health} HP."


def attack_two(attacker, defender, move):
    healing = attacker.attack(move, defender)
    return f"Creature 1 healed for {healing} HP. Creature 1 now has {attacker.health} HP."


def attack_three(attacker, defender, move):
    damage = attacker.attack(move, defender)
    return f"Creature 1 dealt {damage} damage to Creature 2. Creature 2 now has {defender.health} HP."


def attack_four(attacker, defender, move):
    damage = attacker.attack(move, defender)
    return f"Creature 2 dealt {damage} damage to Creature 1. Creature 1 now has {defender.health} HP."


def attack_five(attacker, defender, move):
    healing = attacker.attack(move, defender)
    return f"Creature 2 healed for {healing} HP. Creature 2 now has {attacker.health} HP."


def attack_six(attacker, defender, move):
    damage = attacker.attack(move, defender)
    return f"Creature 2 dealt {damage} damage to Creature 1. Creature 1 now has {defender.health} HP."

def check_speed(creature1, creature2, turn_count):
    if creature1.speed < creature2.speed:
        st.session_state.attack_outputs.append(f"Turn {turn_count}! Creature 1 is slower. Creature 2 goes first.")
    elif creature2.speed < creature1.speed:
        st.session_state.attack_outputs.append(f"Turn {turn_count}! Creature 2 is slower. Creature 1 goes first.")

def check_win_condition(creature1, creature2):
    if creature1.health <= 0:
        st.session_state.attack_outputs.append("Creature 1 has 0 HP. Creature 2 Wins!")
    elif creature2.health <= 0:
        st.session_state.attack_outputs.append("Creature 2 has 0 HP. Creature 1 Wins!")


if __name__ == "__main__":
    main()
