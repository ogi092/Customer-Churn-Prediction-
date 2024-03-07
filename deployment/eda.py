# Phase 1 - Milestone 2
# Nama  : Ogi Hadicahyo
# Batch : HCK-012

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Explaration Data Analysis (EDA)')
    st.write('Further data analysis to gain in-depth insight into the dataset used.')   

    # Load Picture
    st.image("https://www.online-pajak.com/wp-content/uploads/2023/10/meningkatkan-cashflow-dengan-kartu-kredit.jpg")
    st.markdown('---')

    # Load csv Data 
    data = pd.read_csv(r'P1M2_Ogi_Hadicahyo.csv')

    # Displays the top 10 data
    st.header('Displays the top 10 data')
    st.table(data.head(10))
    st.markdown('---')

    # Displays the bottom 10 data
    st.header('Displays the bottom 10 data')
    st.table(data.tail(10))
    st.markdown('---')

    # Distribution of Chustomer Churn
    st.header('1. Data Distribution')
    image = Image.open('Distribution_data.png')
    st.image(image, caption='Figure 1:Data Distribution')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            From this visualization, The analysis shows that the majority of customers have credit scores around the middle, with the largest number coming from France, followed by Spain and Germany. Customer ages tend to be young, with a peak around the late 30s. The majority of customers have 1 or 2 products with the bank, as well as having a credit card. The proportions of active and inactive members are nearly equal, and the predicted salary distribution is uniform. The proportion of customers who have left (Exited = 1) is relatively small. This analysis can provide useful insights for customer retention strategies, marketing, and risk assessment in that business context.
            ''')
    st.markdown('---')
    
    # Distribution of Chustomer Churn
    st.header('2. Distribution of Chustomer Churn')
    image = Image.open('Distribution_Of_Customer_Churn.png')
    st.image(image, caption='Figure 2:Distribution of Chustomer Churn')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            From this visualization, it can be concluded that the dataset has a class imbalance between customers who churn (1) and customers who do not churn (0). The number of customers who did not churn was 79.63% (7963 customers), much more than the number of customers who churned which was only 20.37% (2037 customers).
            ''')
    st.markdown('---')

    # Relationship of exited customer and Gender
    st.header('3. Relationship of exited customer and Gender')
    image = Image.open('Relationship_of_exited_customer_and_Gender.png')
    st.image(image, caption='Figure 3:Relationship of exited customer and Gender')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            There are **more male customers than female customers**, with a difference of 1,000 customers. However, **the churn rate (quit rate) is almost the same for men and women**, with a difference of about 200 customers. This shows that the probability of quitting male and female customers tends to be equal.
            ''')
    st.markdown('---')

    # Age Group That Prefer To Churn
    st.header('4. Age Group That Prefer To Churn')
    image = Image.open('Visualization_Age_Group_That_Prefer_To_Churn.png')
    st.image(image, caption='Figure 4: Age Group That Prefer To Churn')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            Based on the visualization results, the age distribution of customers who have left the bank tends to be right skewed. This shows that *the majority of customers who leave the bank have various ages and are evenly distributed, while the majority of customers who remain at the bank tend to be younger.* In addition, it can be concluded that **the above age group 40 year olds are more likely to leave the bank.**
            ''')
    st.markdown('---')

    # Distribution in Various Countries
    st.header('5. Distribution in Various Countries')
    image = Image.open('Customer_Distribution_in_Various_Countries.png')
    st.image(image, caption='Figure 5: Distribution in Various Countries')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            France has the largest number of customers and also the number of customer churn is almost equal to the number in Germany, showing that despite having a large market, the churn rate (the number of customer churn) remains high in Germany. On the other hand, Germany and Spain have almost the same number of customers. However, the number of customer churn in Spain is the lowest of the three countries. This shows that even though Spain has a small market, it can do a good job of preventing churn.
            ''')
    st.markdown('---')

    # Impact of Estimated Salary on customer churn
    st.header('6. Impact of Estimated Salary on customer churn')
    image = Image.open('Estimated_Salary_on_customer_churn.png')
    st.image(image, caption='Figure 6: Impact of Estimated Salary on customer churn')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            It can be seen that the number of customers who have not yet left (in blue) is much higher across the salary range compared to those who have already left (in green). The distribution of customers who have not left appears relatively even, indicating that the decision to stay is not strongly correlated with a particular salary range. Although the number of customer exits showed a slight increase in the middle salary range, overall there were fewer customer exits across the salary range compared to those who had not left.
            ''')
    st.markdown('---')

if __name__== '__main__':
    run()