import streamlit as st
import pandas as pd

st.set_page_config(page_title="Investment Decision System", page_icon="📈", layout="wide")
st.write("<h1 style='text-align: center;color:#800080;-webkit-text-stroke: 0.2px black;'>Investment Decision System</h1>", unsafe_allow_html=True)
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

# CSS style for formatting
css_style = """
<style>
  .container {
    background-color: rgba(0, 0, 0, 0.5);
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 20px 0;
  }

  .title {
    font-size: 24px;
    font-weight: bold;
    align:center;
    margin-bottom: 10px;
    color:#800080;
  }

  .content {
    font-size: 16px;
    margin-bottom: 15px;
  }

  .about-data {
    font-weight: bold;
    margin-top: 10px;
  }

  .italic {
    font-style: italic;
  }
</style>
"""

# HTML content with CSS
html_content = f"""
<div class="container">
  <div class="title">Context</div>
  <div class="content">
    This Investment Decision Recommendation System, that aims to find the best Investment Decision based on various factors including,
    <ul>
      <li>Demographic distribution analysis</li>
      <li>Employment details</li>
      <li>Investment behaviour insights</li>
    </ul>
  </div>

  <div class="title">About the Data</div>
  <div class="content">
    
  </div>

  <div class="about-data">
    <span class="italic">
  </div>
</div>
"""

# Display the content using st.markdown
st.markdown(css_style, unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)
