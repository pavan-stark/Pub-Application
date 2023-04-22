import streamlit as st
import pandas as pd
import numpy as np

# Load the pub dataset
pub_data = pd.read_csv('open_pubs.csv', header=None)
pub_data.columns = ['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing', 'latitude', 'longitude', 'local_authority']

# Replace \N values with NaN
pub_data = pub_data.replace('\\N', np.nan)

# Drop rows with NaN values
pub_data = pub_data.dropna()

pub_data['longitude'] = pd.to_numeric(pub_data['longitude'], errors='coerce')
pub_data['latitude'] = pd.to_numeric(pub_data['latitude'], errors='coerce')

# Set the page layout to centered
st.set_page_config(layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #EB6864; font-weight: bold;'>🍺 OPEN PUBS APPLICATION 🍻</h1>", unsafe_allow_html=True)

# Display some basic information about the dataset
st.markdown("<h2 style='text-align: center; color: #7F45FA;'>Pub Data</h2>", unsafe_allow_html=True)
st.markdown("<style>div.stDataFrame div[data-testid='stHorizontalBlock'] div[data-testid='stDataFrameContainer'] {margin: 0 auto;}</style>", unsafe_allow_html=True)
st.write(pub_data)
st.write(f"The dataset contains **{len(pub_data)}** pub locations.")
st.write(f"The dataset covers **{len(pub_data['local_authority'].unique())}** local authorities.")

#  Display some statistics about the dataset
st.write("Describing the data:")
# st.write(pub_data.describe())
stats = pub_data.describe().T
stats['count'] = stats['count'].astype(int)
stats = stats[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
st.dataframe(stats.style.highlight_max(axis=0, color='#EB6864'))

