import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from datacleaner import autoclean
import warnings
import numpy as np
import plotly.io as pio
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns

warnings.filterwarnings('ignore')

df=pd.read_excel('C:/DATA SCIENCE/PLACEMENT/Buckman/Dataset/Sample Data for shortlisting.xlsx')
data=pd.read_excel('C:/DATA SCIENCE/PLACEMENT/Buckman/Dataset/modified investments.xlsx')

def genderdist():
    gender_distribution = data['Gender'].value_counts().reset_index()
    gender_distribution.columns = ['Gender', 'Count']

    # Create a Streamlit pie chart using Plotly Express
    st.title('Gender Distribution')
    fig = px.pie(gender_distribution, names='Gender', values='Count')
    st.plotly_chart(fig)

def marital():
    marital_status_distribution = data['Marital Status'].value_counts().reset_index()
    marital_status_distribution.columns = ['Marital Status', 'Count']

    # Create a Streamlit pie chart using Plotly Express
    st.title('Marital Status Distribution')
    fig = px.pie(marital_status_distribution, names='Marital Status', values='Count')
    st.plotly_chart(fig)

def age():
    age_distribution = data['Age'].value_counts().reset_index()
    age_distribution.columns = ['Age', 'Count']

    # Create a Streamlit bar chart using Plotly Express
    st.title('Age Distribution')
    fig = px.bar(age_distribution, x='Age', y='Count', title='Age Distribution')
    st.plotly_chart(fig)

def demogr():
    grouped_df = data.groupby(['Education', 'Role']).size().reset_index(name='Count')

    # Create a Streamlit bar chart using Plotly Express
    st.title('Demographic Distribution')
    stacked_fig = px.bar(grouped_df, x='Education', y='Count', color='Role', title='Demographic Distribution',
                        barmode='stack')
    st.plotly_chart(stacked_fig)

def sunbur():
    grouped_df = data.groupby(['Role', 'Education']).size().reset_index(name='Count')

    # Create a Streamlit Sunburst chart using Plotly Express
    st.title('Sunburst Chart - Role, Education')
    sunburst_fig = px.sunburst(grouped_df, path=['Role', 'Education'], values='Count',
                            title='Sunburst Chart - Role, Education')
    st.plotly_chart(sunburst_fig)

def rolenli():
    selected_df = data.loc[:, ['Role', 'Lower Income']]

    # Melt the DataFrame to create a long-form DataFrame for Plotly Express
    melted_df = selected_df.melt(id_vars='Role', var_name='Income Type', value_name='Income')

    # Split 'Lower Income' into separate bars based on income values
    melted_df['Income Type'] = melted_df['Income Type'] + '_' + melted_df['Income'].astype(str)

    # Create a Streamlit app
    st.title('Clustered Column Chart - Role vs. Lower Income')

    # Create clustered column chart with no separators within bars
    clustered_fig = px.bar(melted_df, x='Role', y='Income', color='Income Type',
                        barmode='group', title='Clustered Column Chart - Role vs. Lower Income')

    # Display the plot in Streamlit
    st.plotly_chart(clustered_fig)

def rolenui():
    selected_df = data.loc[:, ['Role', 'Upper Income']]

    # Melt the DataFrame to create a long-form DataFrame for Plotly Express
    melted_df = selected_df.melt(id_vars='Role', var_name='Income Type', value_name='Income')

    # Split 'Upper Income' into separate bars based on income values
    melted_df['Income Type'] = melted_df['Income Type'] + '_' + melted_df['Income'].astype(str)

    # Create a Streamlit app
    st.title('Clustered Column Chart - Role vs. Upper Income')

    # Create clustered column chart with no separators within bars
    clustered_fig = px.bar(melted_df, x='Role', y='Income', color='Income Type',
                        barmode='group', title='Clustered Column Chart - Role vs. Upper Income')

    # Display the plot in Streamlit
    st.plotly_chart(clustered_fig)

def citynuminv():
    st.title('Sunburst Chart - City and Number of Investors')

    # Create sunburst chart
    sunburst_fig = px.sunburst(data, path=['City', 'Number of investors in family'],
                            values='Number of investors in family',
                            title='Sunburst Chart - City and Number of Investors')

    # Display the plot in Streamlit
    st.plotly_chart(sunburst_fig)

def uli():
    low = data['Lower Percentage'].value_counts().reset_index()
    high = data['Upper Percentage'].value_counts().reset_index()

    # Print the value counts
    print(low)
    print(high)

    # Create a Streamlit app
    st.title('Upper and Lower Investment Percent')

    # Create a bar chart using Plotly Express
    fig = px.bar(data, x="City", y=["Lower Percentage", "Upper Percentage"], title="Upper and Lower Investment Percent")

    # Display the plot in Streamlit
    st.plotly_chart(fig)

def retrisk():
    risk_return_counts = data.groupby(['Return Earned', 'Risk Level']).size().reset_index(name='Count')

    # Create a Streamlit app
    st.title('Relationship between Return and Risk')

    # Create a bar chart using Plotly Express
    bar_chart = px.bar(risk_return_counts, x='Return Earned', y='Count', color='Risk Level',
                        title='Relationship between Return and Risk',
                        labels={'Return Earned': 'Return Level', 'Count': 'Frequency'})

    # Display the plot in Streamlit
    st.plotly_chart(bar_chart)

genderdist()
marital()
age()
demogr()
sunbur()
rolenli()
rolenui()
citynuminv()
uli()
retrisk()