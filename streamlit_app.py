from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
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
            print(f"Creature healed for {healing_amount} health.")
        else:
            damage_amount = self.calculate_damage(move, defender)
            defender.health -= damage_amount
            print(f"Creature dealt {damage_amount} damage to the opponent.")


class Move:
    def __init__(self, name, power, move_type, is_healing_move):
        self.name = name
        self.power = power
        self.type = move_type
        self.is_healing_move = is_healing_move


class MoveType:
    Physical = 1
    Magic = 2


creature1 = Creature(10, 100, 20, 30, 15, 10, 5, 50)
creature2 = Creature(8, 80, 15, 25, 12, 8, 3, 60)

move1 = Move("Fireball", 40, MoveType.Magic, False)
move2 = Move("Heal", 30, MoveType.Magic, True)
move3 = Move("Tackle", 20, MoveType.Physical, False)

while creature1.health > 0 and creature2.health > 0:
    faster_creature = creature1 if creature1.speed > creature2.speed else creature2
    slower_creature = creature2 if faster_creature == creature1 else creature1

    st.write(f"\n{faster_creature}'s turn:")
    st.write(f"1. {move1.name}")
    st.write(f"2. {move2.name}")
    st.write(f"3. {move3.name}")

    move_choice = int(input("Enter your move (1-3): "))

    if move_choice == 1:
        faster_creature.attack(move1, slower_creature)
    elif move_choice == 2:
        faster_creature.attack(move2, faster_creature)
    elif move_choice == 3:
        faster_creature.attack(move3, slower_creature)
    else:
        st.write("Invalid move choice. Try again.")

    st.write(f"Creature 1 Health: {creature1.health}")
    st.write(f"Creature 2 Health: {creature2.health}")

if creature1.health > 0:
    st.write("Creature 1 wins!")
else:
    st.write("Creature 2 wins!")
