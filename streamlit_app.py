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
import streamlit as st
from pokemon import Pokemon, battle

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
