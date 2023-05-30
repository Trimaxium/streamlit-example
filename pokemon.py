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
