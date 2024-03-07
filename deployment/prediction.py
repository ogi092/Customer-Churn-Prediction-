# import library
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Set Config Halaman
st.set_page_config(
    page_title="Predicting Customer Churn",
    layout='wide',
)

# Load Model
with open('model.pkl', 'rb') as file_5:
  model = pickle.load(file_5)

#Function untuk menjalankan streamlit model predictor
def run():
   # Set title
    st.title("Classification Model for Predicting Customer Would be Churn From bank's services.")

    # Sub title
    st.subheader("Predicting the Possibility Customer Will Be Churn.")
    st.markdown('---')
    st.image("https://png.pngtree.com/png-vector/20230525/ourmid/pngtree-bank-workers-providing-service-to-clients-vector-financial-banner-vector-png-image_52210830.jpg")

    # Buat Form Untuk Data Inference
    st.markdown('## Input Data')
    with st.form('my_form'):
        CustomerId = st.number_input(label='Input youre customer ID', min_value = 15600000, step=1)
        Surname = st.text_input(label='Input your surname')
        CreditScore = st.number_input(label='Enter your credit score amount', min_value = 350, max_value= 850, step=1)
        Geography = st.selectbox(label='Select country that you lived', options=['Germany', 'Spain', 'France'])
        Gender = st.selectbox(label='Select your gender', options=['Female', 'Male'])
        Age = st.number_input(label='Enter your age', min_value = 18, max_value= 85, step=1)
        Tenure = st.selectbox(label='Select how many years you have been with the bank', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        Balance = st.number_input(label='Enter your balance amount', min_value = 0, step=1)
        NumOfProducts = st.selectbox(label='Select the number of bank products you use', options=[1, 2, 3, 4, 5])
        HasCrCard = st.selectbox(label='Do you hold a credit card at the bank or not? (0 = No, 1 = Yes)', options=[0, 1])
        IsActiveMember = st.selectbox(label='Are you an active member of the bank? (0 = No, 1 = Yes)', options=[0, 1])
        EstimatedSalary = st.number_input(label='Enter your estimated salary in Dollars', min_value = 0)

        submitted = st.form_submit_button("Predict!!")
    # dataframe
    data = {'CustomerId' : CustomerId,
            'Surname' : Surname,
            'CreditScore' : CreditScore,
            'Geography' : Geography,
            'Gender' : Gender,
            'Age' : Age,
            'Tenure' : Tenure,
            'Balance' : Balance,
            'NumOfProducts' : NumOfProducts,
            'HasCrCard' : HasCrCard,
            'IsActiveMember' : IsActiveMember,
            'EstimatedSalary' : EstimatedSalary}

    df = pd.DataFrame([data])
    st.dataframe(df)

    if submitted:
        y_pred_inf = model.predict(df)
        if y_pred_inf[0] == 0:
            st.write('Customers Will Not Churn')
        else:
            st.write('Customer Will Churn')

if __name__== '__main__':
    run()