# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 
import pandas as pd 

import streamlit as st

from PIL import Image

pickle_in = open("lr.pkl","rb")
lr = pickle.load(pickle_in)

def welcome():
    return "Welcome All"


def predict_diabetes_result(Age,Pregnancies,BloodPressure,BMI,SkinThickness,DiabetesPedigreeFunction,Insulin):
    
    prediction = lr.predict([[Age,Pregnancies,BloodPressure,BMI,SkinThickness,DiabetesPedigreeFunction,Insulin]])
    print(prediction)
    return prediction 


def main():
    #st.title("Women Diabetes Prediction")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;">Women Diabetes Prediction Web App </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input("Age")
    Pregnancies = st.slider("Pregnancies",min_value=0,max_value=13)
    BloodPressure = st.text_input("Blood Pressure")
    BMI = st.text_input("BMI")
    SkinThickness = st.text_input("Skin Thickness")
    DiabetesPedigreeFunction = st.slider("Diabetes Pedigree Function",min_value=0.0,max_value=1.0)
    Insulin = st.text_input("Insulin")
    result = ""
    if st.button("Predict"):
        result = predict_diabetes_result(Age, Pregnancies, BloodPressure, BMI, SkinThickness, DiabetesPedigreeFunction, Insulin)
    
    st.success('Patient Having Diabetes :  {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with StreamLit")
        
if __name__=='__main__': 
    main()          