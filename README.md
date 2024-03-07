# Customer Churn Prediction Analysis
## Introduction
Customer churn is an important issue for the business world, especially in industries such as banking where retaining customers is critical for sustainable growth. With advances in data science, there is an opportunity to investigate this phenomenon in more depth. 

This project seeks to investigate the underlying factors that contribute to customer churn. By leveraging machine learning techniques and algorithms such as KNN, SVM, Decision Tree, Random Forest, and Boosting, as well as careful hyperparameter tuning, the goal is to develop an optimal model capable of predicting customer churn. The main metrics used are Recall and ROC-AUC, with a focus on minimizing the number of cases where the model fails to identify potential churning customers.Through these efforts, banks can gain valuable insights into customer behavior and anticipate potential churn, allowing banks to design proactive strategies aimed at customer retention.

The dataset comprises various attributes related to bank customers, including unique row numbers, customer IDs, surnames, credit scores, geography, gender, age, tenure, bank balances, number of products used, credit card ownership, active membership status, estimated salaries, and an exit flag indicating whether the customer closed their account (1 for closure, 0 for retention).

## Main feature
This project offers several critical analysis and prediction features, including:

- **Feature Importance Analysis:** Identify the most influential factors contributing to customer churn using techniques like correlation analysis and feature importance scores.
- **Model Comparison:** Evaluate and compare the performance of machine learning algorithms (e.g., KNN, SVM, Decision Tree, Random Forest) to predict customer churn.
- **Customer Segmentation:** Segment customers based on demographics and behavior to analyze churn patterns and differences.

## Methodology
The project methodology is divided into several main stages:

1. **Exploratory Data Analysis (EDA):** This stage involves data visualization and statistical analysis to understand the distribution, trends, and relationships between variables in the dataset.
2. **Feature Engineering:** This process involves selecting, transforming, and creating new features to improve the predictive capabilities of the model.
3. **Machine Learning Model Training:** Using XGBoost as the main model to predict customer churn. This model was chosen because of its ability to handle linear prediction problems compared to other model (KNN, SVM, Decision Tree, and Random Forest)

## Results
The developed model successfully predicts customer churn with a good degree of accuracy, as indicated by the evaluation metrics used (Focused on Recall and ROC-AUC metrics). These results demonstrate the effectiveness of the approach used in analyzing and predicting churn in the context of customer churn.

## File Descriptions

- Bank_Customer_Churn.csv: Raw data used for analysis.
- Customer_Churn_Modelling.ipynb: Main notebook containing the analysis and modeling process.
- Customer_Churn_Inference.ipynb: Additional notebook focusing on further model insights.
- url.txt: Text file containing dataset and deployment links.
- Deployment folder: containing scripts for deployment creation.

## References

Dataset     : <a href="https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling"> Bank Customer Churn</a>.  
Deployment  : <a href="https://huggingface.co/spaces/OgiHadicahyo/Churn_Modelling"> Hugging Face</a>. 