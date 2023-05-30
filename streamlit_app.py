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

import random
from streamlit import session_state as state

class Pokemon:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

def battle(pokemon1, pokemon2):
    st.write(f"Battle between {pokemon1.name} and {pokemon2.name} begins!")
    st.write(f"{pokemon1.name}: {pokemon1.health} HP")
    st.write(f"{pokemon2.name}: {pokemon2.health} HP")

    while pokemon1.health > 0 and pokemon2.health > 0:
        st.write("---")
        st.write("Player's turn:")
        st.write("Select your move:")
        
        quick_attack = st.button("Quick Attack")
        t_bolt = st.button("Thunderbolt")
        i_tail = st.button("Iron Tail")

        if quick_attack:
            damage = random.randint(10, 20)
            defender = pokemon2

            st.write(f"{pokemon1.name} used Quick Attack and dealt {damage} damage.")
            defender.take_damage(damage)
            st.write(f"{pokemon1.name}: {pokemon1.health} HP")
            st.write(f"{pokemon2.name}: {pokemon2.health} HP")

        elif t_bolt:
            damage = random.randint(10, 20)
            defender = pokemon2

            st.write(f"{pokemon1.name} used Thunderbolt and dealt {damage} damage.")
            defender.take_damage(damage)
            st.write(f"{pokemon1.name}: {pokemon1.health} HP")
            st.write(f"{pokemon2.name}: {pokemon2.health} HP")

        elif i_tail:
            damage = random.randint(10, 20)
            defender = pokemon2

            st.write(f"{pokemon1.name} used Iron Tail and dealt {damage} damage.")
            defender.take_damage(damage)
            st.write(f"{pokemon1.name}: {pokemon1.health} HP")
            st.write(f"{pokemon2.name}: {pokemon2.health} HP")

        if pokemon2.health <= 0:
            break

        st.write("---")
        st.write("Opponent's turn:")
        damage = random.randint(10, 20)
        defender = pokemon1

        st.write(f"{pokemon2.name} used a random attack and dealt {damage} damage.")
        defender.take_damage(damage)
        st.write(f"{pokemon1.name}: {pokemon1.health} HP")
        st.write(f"{pokemon2.name}: {pokemon2.health} HP")

    if pokemon1.health > 0:
        st.write(f"{pokemon1.name} wins the battle!")
    else:
        st.write(f"{pokemon2.name} wins the battle!")

def main():
    st.title("Pokemon Battle")

    pokemon1 = Pokemon("Pikachu", 100, 20)
    pokemon2 = Pokemon("Charizard", 120, 18)

    st.write("Welcome to the Pokemon Battle!")
    st.write(f"Today's battle is between {pokemon1.name} and {pokemon2.name}.")

    start_battle = st.button("Start Battle")

    if start_battle:
        battle(pokemon1, pokemon2)


if __name__ == "__main__":
    main()
