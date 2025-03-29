import os
import pandas as pd
import pickle #pre trained model loading 
import streamlit as st # webapp
from streamlit_option_menu import option_menu

st.set_page_config(page_title= 'Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='👨‍⚕️')


diabetes_model = pickle.load(open(r"C:\Users\VENKY\Desktop\Disease\tranning_models\diabetes_model.sav", 'rb')) # 'rb : read binary'

heart_disease_model = pickle.load(open(r"C:\Users\VENKY\Desktop\Disease\tranning_models\heart_model.sav", 'rb'))

parkinsons_model = pickle.load(open(r"C:\Users\VENKY\Desktop\Disease\tranning_models\parkinson_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu('Prediction of disease outbreak system',
                           ['Diabetes Prediction','Heart Disease Prediction','parkinsons Prediction'],
                           menu_icon='hospital-fill',icons = ['activity','heart','person'],default_index=0)
    
    

if selected == 'Diabetes Prediction' :
        st.title('Diabetes Prediction using ML')
        col1,col2,col3 = st.columns(3)
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
        with col2:
            Glucose =  st.text_input('Glucose level ')
        with col3:
            BloodPressure  = st.text_input('Blood Pressure value')
        with col1:
            SkinThickness=  st.text_input('Skin Thickness Value')
        with col2:
            Insulin = st.text_input('Insulin level')
        with col3:
            BMI =  st.text_input('BMI value ')
        with col1:
            DiabetesPedigreeFunction  = st.text_input('DiabetesPedigreeFunction value')
        with col2:
            Age =  st.text_input('Age of the Person')

        dia_diagnosis = ""
        if st.button('Diabetes Test Result'):
            try :
                user_input =[Pregnancies,Glucose,BloodPressure, SkinThickness, Insulin, 
                                BMI, DiabetesPedigreeFunction, Age]
                user_input = [float(x) for x in user_input]
                diab_prediction = diabetes_model.predict([user_input])
                if diab_prediction[0] == 1:
                    dia_diagnosis = 'The Person is Diabetic'
                else:
                    dia_diagnosis = "The Person is not diabetic"

            except ValueError:
                 st.error("Please enter all the required  fields.")


        st.success(dia_diagnosis)


 
 


if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of the Person')
        trestbps = st.text_input("Resting Blood Pressure (trestbps)")
        restecg = st.text_input("Resting Electrocardiographic Results (restecg)")
        oldpeak = st.text_input('ST Depression Induced by Exercise (oldpeak)')
        thal = st.text_input('Thal: 0=Normal; 1=Fixed Defect; 2=Reversible Defect')
    
    with col2:
        sex = st.text_input("Sex (0=Female, 1=Male)")
        chol = st.text_input("Serum Cholesterol in mg/dl (chol)")
        thalach = st.text_input('Maximum Heart Rate Achieved (thalach)')
        slope = st.text_input('Slope of the Peak Exercise ST Segment (slope)')
    
    with col3:
        cp = st.text_input("Chest Pain Type (cp)")
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (fbs)")
        exang = st.text_input('Exercise Induced Angina (exang)')
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy (ca)')
    
    heart_diagnosis = ""
    
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The Person has Heart Disease'
        else:
            heart_diagnosis = "The Person does not have Heart Disease"
    
    st.success(heart_diagnosis)

  
if selected == 'parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        fhi = st.text_input("MDVP:Fhi(Hz)")
        flo = st.text_input("MDVP:Flo(Hz)")
        jitter = st.text_input('MDVP:Jitter(%)')
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    
    with col2:                 
        rap = st.text_input("MDVP:RAP")
        ppq = st.text_input("MDVP:PPQ")
        ddp = st.text_input('Jitter:DDP')
        shimmer = st.text_input('MDVP:Shimmer')
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')  
    
    with col3:
        shimmer_apq3 = st.text_input("Shimmer:APQ3")
        shimmer_apq5 = st.text_input("Shimmer:APQ5")            
        apq = st.text_input("MDVP:APQ")
        dda = st.text_input('Shimmer:DDA')
    
    with col4:
        NHR = st.text_input('NHR')
        HNR = st.text_input('HNR')
        RPDE = st.text_input('RPDE')
        DFA = st.text_input('DFA')  
    
    with col5:
        spread1 = st.text_input('spread1')
        spread2 = st.text_input('spread2')
        D2 = st.text_input('D2')
        PPE = st.text_input('PPE')
    
    parkinson_diagnosis = ""
    
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, jitter, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, 
                      shimmer_apq3, shimmer_apq5, apq, dda, NHR, HNR, RPDE, DFA, spread1, 
                      spread2, D2, PPE]  
        user_input = [float(x) for x in user_input]
        parkinson_prediction = parkinsons_model.predict([user_input])
        
        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = "The Person has Parkinson's Disease"
        else:
            parkinson_diagnosis = "The Person does not have Parkinson's Disease"
    
    st.success(parkinson_diagnosis)
