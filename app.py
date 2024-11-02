''' Main application to launch with streamlit'''
import os

import numpy as np
import pandas as pd
import streamlit as st

from reader import Reader
from joiner import Joiner

# Function to read CSV files from a directory
def load_data_from_directory(directory):
    return [f for f in os.listdir(directory)]

# Load the wishlists and sharelists
cwd = os.getcwd()
wishlist_dir = os.path.join(cwd, 'data/wishlists')
sharelist_dir = os.path.join(cwd, 'data/sharelists')

wishlists = load_data_from_directory(wishlist_dir)
sharelists = load_data_from_directory(sharelist_dir)

# Streamlit interface
st.title("Join Wishlists and Sharelists")

# Dropdown for wishlists
selected_wishlist = st.selectbox("Select a Wishlist", wishlists)

# Dropdown for sharelists
selected_sharelist = st.selectbox("Select a Sharelist", sharelists)

# Button to perform the join
if st.button("Join"):
    
    reader = Reader()
    # Load selected data
    wishlist_df = reader.read_dataframe(os.path.join(wishlist_dir, selected_wishlist))
    sharelist_df = reader.read_dataframe(os.path.join(sharelist_dir, selected_sharelist))
    
    # Join the dataframes
    joiner = Joiner(sharelist_df, wishlist_df)
    result_df = joiner.mix_lists(method='inner')
    
    # Display the resulting dataframe
    st.subheader("Resulting DataFrame")
    st.dataframe(result_df)

# Optionally, add error handling for cases where the join might fail
