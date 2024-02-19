# Loan Apporval Predictor

<img width="641" alt="image" src="https://github.com/rajbondili/project4_Loan_approval_predictor/assets/142377615/b38fc08a-d1e5-41fd-9225-38273badf313">


# Overview

This project, Loan Approval Prediction Analysis using historical data to build a model that can predict whether a loan application is likely to be approved or rejected based on the machine learning algorithms.
The statistical techniques are used to identify patterns and relationships within the dataset alongwith the machine learning algorithms that will contribute to the loan approval decision.

# DataSource

The dataset was in the CSV file format.
| Column        	| Description   				      |
| ------------- 	| ------------- 				      |
| Loan          	| A unique id   				      |
| Gender           	| Male/female   				      |
| Married           | Yes/ No       				      |
| Dependents		| Applicant Dependents(1,2,3)	      |
| Education         | Graduate or not				      |
|Self_Employed		| yes/no						      |
|Applicant income 	| Applicant income				      |
|CoapplicantIncome  | Co-applicant income			      |
|LoanAmount			| Loan amount (in thousands)		  |
|Loan_Amount_Term	|Terms of loan (in months)		      |
|Credit_History		| Yes/No						      |
|Property_Area		|Rural/Urban/Semi-urban			      |
|Loan_Status		| Y- Yes, N-No 					      |


## 🧰 Libraries

In this project we outline the tools, language and libraries required to complete the project brief.
<br>

<img align="left" alt="Git" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" />
<img align="left" alt="GitHub" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" />
<img align="left" alt="Python" width="80x" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" />
<img align="left" alt="Pandas" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original-wordmark.svg" />
<img align="left" alt="Flask" width="80px" style="padding-right:12px;" img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original-wordmark.svg" />
<img align="left" alt="VSCode" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" />
<img align="left" alt="Jupyter" width="80px" style="padding-right:12px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" />

<br><br><br><br><br><br><br>


# Categorical Columns of Dataset
The analysis of the categorical columns of dataset are as follows:

    > Loan Approval Status: About 66.6% of applicants have been granted loan.
    > Sex: In the dataset the primary income consists of Men which is approximately three times than Women.
    > Martial Status: 66% of the population in the dataset is Married and they are more likely to be granted loans.
    > Dependents: Majority of the population have zero dependents and are also likely to accepted for loan.
    > Education: About 83% of the population is Graduate and graduates have higher propotion of loan approval.
    > Employment: 83% of population is not self employed.
    > Property Area: More applicants from Semi-urban and likely to be granted loans.
    > Credit history: Applicant with credit history are far more likely to be accepted.
    > Loan Amount Term: Majority of the loans taken are for 360 Months (30 years). 

<img width="531" alt="image" src=".\Images\Categorical_values.png">

# Machine Learning Model
The following are the machine learning model used to predict the loan appliaction whether it will be approved or rejected. All the models Accuracy and Classification Reports taken into consideration to use the best model to predict the loan application. So the RandomForestClassifier machine learning model has the highest accuracy of 87% with the average precision higher than 80% in predicting the application, this model is being used in the flask application as the back-end model to predict the applications.

1. Logistic regression
    ***********************************************************************
        Accuracy: 82%
        Classification Report: 
                            precision    recall  f1-score   support

                False           0.71      0.48      0.57        25
                True            0.85      0.93      0.89        76

                accuracy                           0.82        101
                macro avg       0.78      0.71      0.73       101
                weighted avg    0.81      0.82      0.81       101
    ************************************************************************

 2. Decision Tree
    ************************************************************************
        Accuracy: 73%
        Classification Report: 
                        precision    recall  f1-score   support

                False       0.47      0.56      0.51        25
                True        0.85      0.79      0.82        76

            accuracy                            0.73       101
            macro avg       0.66      0.67      0.66       101
            weighted avg    0.75      0.73      0.74       101
    *************************************************************************

 3. Support Vector Machine
    *************************************************************************
        Accuracy: 75%
        Classification Report: 
                        precision    recall  f1-score   support

            False           0.00      0.00      0.00        25
            True            0.75      1.00      0.86        76

        accuracy                                0.75       101
        macro avg           0.38      0.50      0.43       101
        weighted avg        0.57      0.75      0.65       101
    **************************************************************************

 4. K-Nearest Neighbors
    
    **************************************************************************
        Accuracy: 71%
        Classification Report: 
                        precision    recall  f1-score   support

            False           0.25      0.08      0.12        25
            True            0.75      0.92      0.83        76

        accuracy                                0.71       101
        macro avg           0.50      0.50      0.47       101
        weighted avg        0.63      0.71      0.65       101

    **************************************************************************

 5. RandomForestClassifier
    
    **************************************************************************
        Accuracy: 87%
        Classification Report: 
                        precision    recall  f1-score   support

                False       0.80      0.64      0.71        25
                True        0.89      0.95      0.92        76

            accuracy                            0.87       101
            macro avg       0.84      0.79      0.81       101
            weighted avg    0.87      0.87      0.87       101
    ***************************************************************************

# Random Forest Classifier

Random forest is a commonly-used machine learning algorithm which combines the output of multiple decision trees to reach a single result.

The below chart shows us the important fields on the which most of the decision made by the algorithm to reject or approve the loan application. The Figure 1 is generated by the random forest classifier algorithm whereas Figure 2 gives the same results when we find out the correlation between the fields to predict the loan application. The model best predicted according to the test data and actual data as per the confusion matrix shown in the Figure 3. Both the pecision and recall quantifies and overall accuracy of the model is above 80% as shown in Figure 4   <br />

<p align="left">
Figure 1: Important Features Random Forest Classifier (Machine Learning Model)<br clear="both" />
<img align="left" width="531" alt="image" src=".\Images\Feature_Importance_in_Random_Forest_Model.png"><br clear="both"/>
</p>

<p align="left">
Figure 2: Correlation of Dataset Fields<br clear="both" />
<img align="left" width="531" alt="image" src=".\Images\Correlation_Chart_Dataset_Fields.PNG"><br clear="both"/>
</p>

<p align="left">
Figure 3: Confusion Matrix Random Forest Classifier (Machine Learning Model)<br clear="both" />
<img align="left" width="531" alt="image" src=".\Images\Random_Forest_Confusion_Matrix.PNG"><br clear="both"/>
</p>

<p align="left">
Figure 4: Classification Report Random Forest Classifier (Machine Learning Model)<br clear="both" />
<img align="left" alt="image" src=".\Images\Random_Forest_Classification_Chart.PNG"><br clear="both"/>
</p>

# Conclusion
To conclude, Random Forest Classifier is giving the best accuracy greater than 80% on testing dataset. As per chart for important features figure 1 and the heatmap shown in the figure 2, the Applicant Income, Credit_History and Loan_Amount plays vital role in depicting approval and rejection of the loan application. However, we are lacking in the test data as our dataset is having success rate of loan approval for 66%. it doesnot consider various actual world field's like Co-Applicant Income, Dependants, type of area and property looking by the applicant. Apart from that, it does not include part of the income being spend on the other factors like food and accomodation, recreatinal activities, part of income going towards the dependents and investing etc. once these factors comes into consideration might be different algorithm need for this type of prediction.

# References
https://www.geeksforgeeks.org/<br clear="both" />
https://stackoverflow.com/<br clear="both" />
https://docs.github.com/<br clear="both" />
https://medium.com/<br clear="both" />
