import pickle
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report as cr
import matplotlib.pyplot as plt
import plotly.express as px
from yellowbrick.classifier.classification_report import classification_report
from yellowbrick.classifier import ClassificationReport
import plotly.express as px
from mlxtend.plotting import plot_confusion_matrix

dataset = pd.read_excel("Dataset/with decision.xlsx")

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = cr(y_test, y_pred,output_dict=True)
    return accuracy, report

st.write("<h1 style='text-align: center;color: #800080;'>Investment Decision System</h1>", unsafe_allow_html=True)

Y=dataset['Cluster']
X=dataset.drop('Cluster',axis=1)

with open("C:/DATA SCIENCE/PLACEMENT/Buckman/best_models.pkl", "rb") as model_file:
    models = pickle.load(model_file)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

st.sidebar.title("Select Model")

selected_model = st.sidebar.selectbox("Select a model", list(models.keys()))

if st.button("Evaluate"):
    st.write(f"**Selected Model:** {selected_model}")
    model = models[selected_model]

    accuracy, report = evaluate_model(model, X_test, y_test)
    viz = ClassificationReport(model,
                        classes=[0,1],
                        support=True,
                        fig1=plt.figure(figsize=(8,6)))
    viz.fit(X_train, y_train)
    viz.score(X_test, y_test)
    y_pred = model.predict(X_test)

    st.write(f"**Accuracy:** {accuracy}")
    st.write("**Classification Report:**")

    average_report_df = pd.DataFrame(report).transpose()

    metrics = ['precision', 'recall', 'f1-score']
    st.write(average_report_df)
