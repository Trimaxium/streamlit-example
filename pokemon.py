import random
import streamlit as st

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

    # Rest of your battle logic
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
            
            st.write("---")
            st.write("Opponent's turn:")
            damage = random.randint(10, 20)
            defender = pokemon1

            st.write(f"{pokemon2.name} used a random attack and dealt {damage} damage.")
            defender.take_damage(damage)

            st.write(f"{pokemon1.name}: {pokemon1.health} HP")
            st.write(f"{pokemon2.name}: {pokemon2.health} HP")

        elif t_bolt:
            damage = random.randint(10, 20)
            defender = pokemon2

            st.write(f"{pokemon1.name} used Thunderbolt and dealt {damage} damage.")
            defender.take_damage(damage)

        elif i_tail:
            damage = random.randint(10, 20)
            defender = pokemon2

            st.write(f"{pokemon1.name} used Iron Tail and dealt {damage} damage.")
            defender.take_damage(damage)

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
