import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('random_forest_pipeline.pkl', 'rb'))

def main():
    st.title("Credit Score Prediction App")
    st.write("Enter the details below to predict your credit score")

    num_delayed_payment = st.number_input("Number of Delayed Payments", min_value=0, max_value=100, value=0, step=1)
    credit_utilization_ratio = st.number_input("Credit Utilization Ratio (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    outstanding_debt = st.number_input("Outstanding Debt ($)", min_value=0.0, value=0.0, step=100.0)
    annual_income = st.number_input("Annual Income ($)", min_value=0.0, value=0.0, step=1000.0)
 
    input_data = pd.DataFrame({
        'Num_of_Delayed_Payment': [num_delayed_payment],
        'Credit_Utilization_Ratio': [credit_utilization_ratio],
        'Outstanding_Debt': [outstanding_debt],
        'Annual_Income': [annual_income]
    })

    if st.button("Predict Credit Score"):
        prediction = model.predict(input_data)
        st.write(f"Model Prediction: {prediction}")

        if isinstance(prediction[0], int):
            credit_score_mapping = {2: "Good", 1: "Standard", 0: "Bad"}  
            result = credit_score_mapping[prediction[0]]  
        else:
            result = prediction[0]
        
        st.success(f"Predicted Credit Score: {result}")
        
        
        
        if result == "Good":
            st.write("Loan Status: Approved - 100% Loan Provided")
        elif result == "Standard":
            st.write("Loan Status: Pending - Ground Check Recommended")
        elif result == "Bad":
            st.write("Loan Status: Denied - Loan Not Approved")
            
            
if __name__ == "__main__":
    main()
