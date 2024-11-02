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

# Function to save uploaded files
def save_uploaded_file(uploaded_file, save_path):
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

# Load the wishlists and sharelists
cwd = os.getcwd()
wishlist_dir = os.path.join(cwd, 'data/wishlists')
sharelist_dir = os.path.join(cwd, 'data/sharelists')

wishlists = load_data_from_directory(wishlist_dir)
sharelists = load_data_from_directory(sharelist_dir)

# Streamlit interface
st.title("Join Wishlists and Sharelists")

# Sidebar for uploading new lists
st.sidebar.title("Upload New Lists From MANABOX")
name = st.sidebar.text_input("Name (required)")
wishlist_file = st.sidebar.file_uploader("Upload a Wishlist (TXT)", type=["txt"])
sharelist_file = st.sidebar.file_uploader("Upload a Sharelist (TXT)", type=["txt"])

if st.sidebar.button("Upload"):
    if name:
        if wishlist_file:
            wishlist_path = os.path.join(wishlist_dir, f"{name}_wishlist.txt")
            save_uploaded_file(wishlist_file, wishlist_path)
            st.sidebar.success(f"Uploaded {wishlist_file.name} as {name}_wishlist.txt")

        if sharelist_file:
            sharelist_path = os.path.join(sharelist_dir, f"{name}_sharelist.txt")
            save_uploaded_file(sharelist_file, sharelist_path)
            st.sidebar.success(f"Uploaded {sharelist_file.name} as {name}_sharelist.txt")
        
        if not wishlist_file and not sharelist_file:
            st.sidebar.warning("Please upload at least one file (wishlist or sharelist).")
    else:
        st.sidebar.error("Please provide a name.")

    # Refresh the lists after upload
    wishlists = load_data_from_directory(wishlist_dir)
    sharelists = load_data_from_directory(sharelist_dir)

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
    st.subheader("Here are the cards that you can trade!")
    st.dataframe(result_df)
