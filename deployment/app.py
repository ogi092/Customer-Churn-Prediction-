# Phase 1 - Milestone 2
# Nama  : Ogi Hadicahyo
# Batch : HCK-012

import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox(label='Menu:', options=['Home', 'Exploration Data Analysis', 'Model Inference'])

if page == 'Home':
    st.image("https://img.freepik.com/vector-premium/lugar-trabajo-creativo-gabinete-moderno-vacio-gente-interior-oficina-centro-trabajo-conjunto-contemporaneo_48369-42849.jpg")
    st.title('Weclome to, MILESTONE 2')
    st.write('FTDS - Phase 1')
    st.header('')

    col1, col2 = st.columns(2)

    # ======================= Columns 1 =======================
    col1.write('**Name             :**')
    col1.write('**Batch            :**')
    col1.write('**Milestone Purpose :**')

    # ======================= Columns 2 =======================
    col2.write('Ogi Hadicahyo')
    col2.write('HCK-012')
    col2.write("This project was created to create a classification prediction model to predict whether customers will churn.")
    col2.write("We'll also look at what the characteristics of someone who has the potential to churn are like.")
    col2.write("The models that will be tried are KNN, SVM, Decision Tree, Random Forest. In the process we will try to implement Pipelines, Cross Validation, and Hyperparameter Tuning. The final model that has been determined will then be deployed with streamlit in HuggingFace .")

    st.header('')
    st.write('**Please select another menu in the Select Box on the left of your screen to get started!**')
    st.write('')
    with st.expander("Background"):
        st.caption('I am a Data Scientist who is currently taking part in a learning program at Hacktive8, Pondok Indah. I found an interesting dataset on Kaggle that contains information about customer churn at a bank. I realized that this dataset was valuable because it could be used to create machine learning models that could predict whether a customer would abandon the bank services. This model is very useful for banks to take appropriate preventive measures to retain customers and allocate resources more efficiently. By increasing customer retention, banks can increase their revenue from service fees and additional product offerings to loyal customers.')
        st.caption('')
        st.caption('Therefore, I aim to create an optimal machine learning model using several algorithms such as KNN, SVM, Decision Tree, Random Forest, and Boosting, as well as performing hyperparameter tuning to maximize model performance. By having an effective machine learning classification system, banks can develop their business further by predicting potential customers who will leave the service.')
    
    with st.expander("Problem Statement"):
        st.caption('Create a predictive machine learning model using KNN, SVM, Decision Tree, Random Forest, and Boosting algorithms, then identify the best model for predicting customers who have the potential to leave bank services. This model helps banks identify customers at high risk of churning, enabling them to take further action to retain customers and prevent potential business losses.')

    with st.expander("Outline"):
         st.caption("1. Load data and check information about the data set.")
         st.caption("2. EDA on a dataset involving further data analysis to gain insight.")
         st.caption("3. Feature Engineering to obtain features and modeling targets.")
         st.caption("4. Defining Models using pipelines.")
         st.caption("5. Training the model.")
         st.caption("6. Evaluate the model consisting of Hyperparameter Tuning to get the best model with the best results.")
         st.caption("7. Saving the best model.")
         st.caption("8. Conclusion.")
         st.caption("9. Deployment.")
         st.caption("")

    with st.expander("Conclusion"):
        st.caption("Based on the dataset that we took about information about customer churn at a bank with a total of 10,000 data and a total of 14 columns. We have succeeded in creating a model that is used to predict whether a customer will churn (1) or a customer will not churn (0).")
        st.caption("From the test results using 5 different models, namely using KNN, SVM, Decision Tree, Random Forest and XGBoost. We find that the results of the XGBoost model are the best compared to other models, because XGBoost has the highest average cross-validation score and also has the lowest standard deviation, which shows that its performance is quite consistent in various parts of the data set. However, because there are indications that the model is overfitting and its performance is imbalanced in test and train, we carry out tuning to compare model performance.")
        st.caption("The XGBoost model successfully identified 398 true positive cases and 2013 true negative cases, but it also exhibited errors in classification, notably with 376 false positive and 213 false negative cases. On the other hand, the model with hyperparameter tuning improves true positive identification to 386 cases but introduces 385 false positive and 225 false negative cases. While the hyperparameter-tuned model prioritizes recognizing churned customers, it lacks balance in overall prediction accuracy. Therefore, for a balanced approach in predicting potential customer churn, the XGBoost model without hyperparameter tuning is preferred due to its better balance between true positive, true negative, false positive, and false negative rates.")
        st.caption("The advantages of the XGBoost model created are:")
        st.caption("- The relatively high recall rate (0.831 on test data) shows that the model is able to identify the majority of customers who have the potential to churn.")
        st.caption("The disadvantages of the XGBoost model created are:")
        st.caption("- Overfitting: There is a significant difference between model performance on test data and training data (0.831 vs 0.928), indicating overfitting. Models tend to memorize training data and are less able to generalize to new data.")
        st.caption("- High Variability: High standard deviation in recall values for test data (0.060) and training data (0.007) indicates large variability in model performance. This indicates that the model is sensitive to changes in the dataset.")
        st.caption("- High Classification Error: The significant number of False Positives (376) and False Negatives (213) indicates that the model tends to make errors in classifying customers, either as customers who have the potential to churn but do not, or vice versa. This can result in inaccurate decisions and negatively impact business strategy.")
        st.caption("With these results, there are several suggestions that can be made to improve goods arriving on time, such as:")
        st.caption("- **Use of Information for Customer Retention:** Banks can utilize information obtained from customer churn prediction models to design more effective customer retention strategies.")
        st.caption("- **Customer Segmentation:** Based on churn prediction results, banks can segment customers to identify customer groups with high and low risk of churn.")
        st.caption("- **Improved Customer Service and Experience:** Information about customer churn can provide banks with valuable insights into customer needs and preferences.")
        st.caption("- **Model Evaluation and Improvement:** Banks can continue to evaluate and improve their customer churn prediction models by taking into account feedback and new data.")
        st.caption("- **Integration with Wider Business Strategy:** Customer churn prediction models must be integrated with the bank's overall business strategy. This means ensuring that steps taken based on predicted results are aligned with business objectives and company values, and coordinated with broader customer retention initiatives.")

elif page == 'Exploration Data Analysis':
    eda.run()
else:
    prediction.run()