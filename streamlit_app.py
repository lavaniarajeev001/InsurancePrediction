import streamlit as st
import numpy as np
import pickle

from PIL import Image

pickle_in=open("C:/Users/user/Docker/InsurancePrediction/classifier.pkl","rb")
classifier = pickle.load(pickle_in)


def predict_insurance(Age,Employment_Type,GraduateOrNot,AnnualIncome,FamilyMembers,ChronicDiseases,FrequentFlyer,EverTravelledAbroad):
    input_data = [[Age,Employment_Type,GraduateOrNot,AnnualIncome,FamilyMembers,ChronicDiseases,FrequentFlyer,EverTravelledAbroad]]
    input_array = np.array(input_data)
    prediction=classifier.predict(input_array)
    print(prediction)
    return prediction

def main():
    st.title("Insurance Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10x">
    <h2 style="color:white;text-align:center;">Streamlit Insurance Prediction ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input("Age","Type here")
    Employment_Type = st.text_input("Employment Type","Type here")
    GraduateOrNot = st.text_input("GraduateOrNot","Type here")
    FamilyMembers = st.text_input("FamilyMembers","Type here")
    AnnualIncome = st.text_input("AnnualIncome","Type here")
    ChronicDiseases = st.text_input("ChronicDiseases","Type here")
    FrequentFlyer = st.text_input("FrequentFlyer","Type here")
    EverTravelledAbroad = st.text_input("EverTravelledAbroad","Type here")
    result = " "
    if st.button("Predict"):
        result= predict_insurance(Age,Employment_Type,GraduateOrNot,AnnualIncome,FamilyMembers,ChronicDiseases,FrequentFlyer,EverTravelledAbroad)
    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with streamlit")


if __name__ == "__main__":
    main()