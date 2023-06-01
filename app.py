import streamlit as st
import pandas as pd
import pickle


pickle_in = open("xgb.pkl", "rb") 
classifier = pickle.load(pickle_in)

def predict_note_authentication(cough, fever, sore_throat, shortness_of_breath, head_ache,age_60_and_above, gender, test_indication):
    prediction = classifier.predict([[cough, fever, sore_throat, shortness_of_breath, head_ache,age_60_and_above, gender, test_indication]])
    print(prediction)
    return prediction


def main():

    st.title("COVID 19 Predictor")

    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Covid 19 Detection App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    cough  =  st.number_input("Cough = No : 0, Yes : 1", format="%.0f")

    fever = st.number_input("Fever = No : 0, Yes : 1", format="%.0f")

    sore_throat = st.number_input("Sour Throat = No : 0, Yes : 1", format="%.0f")

    shortness_of_breath = st.number_input("ShortNess of Breath = No : 0, Yes : 1", format="%.0f")

    head_ache = st.number_input("head_ache = No : 0, Yes : 1", format="%.0f")

    age_60_and_above = st.number_input("Age 60 Above = No : 0, Yes : 1", format="%.0f")

    gender = st.number_input("Gender = Female : 0, Male : 1", format="%.0f")

    test_indication = st.number_input("Test Indication", format="%.0f")


    result= ""

    if st.button("Predict"):
        result = predict_note_authentication(cough, fever, sore_throat, shortness_of_breath, head_ache,age_60_and_above, gender, test_indication)
    
    
    if result == 0:
        st.success('Covid is not Detected : Negative')
    elif result == 1:
        st.success("Covid is Detected : Positive")


if __name__=='__main__':
    main()
