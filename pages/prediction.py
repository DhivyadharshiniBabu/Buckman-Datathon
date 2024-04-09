import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

css_style = """
    text-align:center;
    color: #800080; 
    font-size: 1000px; 
    font-family: Arial, sans-serif; 
    
"""
css_style1 = """
    align:center;
    width: 300px;
    padding: 10px;
    border: 2px solid #333;
    background-color:rgba(0,0,0, 0.5);
    font-family: Arial, sans-serif;
    text-align: center; 
    margin: 0 auto; /* Center the box horizontally */
    color: yellow;
"""

st.write("<h1 style='text-align: center;color: #800080;'>Prediction</h1>", unsafe_allow_html=True)

