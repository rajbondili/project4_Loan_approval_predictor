# save this as app.py
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        credit = request.form['credit'] 
        if (credit == "Yes"):
          credit = float(1)       
        else:
          credit = float(0)
        area = request.form['area']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])

        # gender
        if (gender == "Male"):
            Gender_Male = True
        else:
            Gender_Male = False
        
        # married
        if(married=="Yes"):
            Married_yes = True
        else:
            Married_yes= False

        # dependents
        if(dependents=="1"):
            Dependents = 1          
        elif(dependents == "2"):         
            Dependents = 2       
        elif(dependents=="3+"):          
            Dependents = 3
        else:
            Dependents = 0

        # education
        if (education=="Not Graduate"):
            Not_graduate = True
        else:
            Not_graduate = False

        # employed
        if (employed == "Yes"):
            employed_yes = True
        else:
            employed_yes = False        
     
        # property area
        if(area=="Semiurban"):
            semiurban = True
            urban= False
            rural = False
        elif(area=="Urban"):
            semiurban = False
            urban= True
            rural = False
        else:
            semiurban= False
            urban= False
            rural = True

        ## Assign values to model feature names for prediction.
        ApplicantIncome = ApplicantIncome      
        CoapplicantIncome = CoapplicantIncome
        LoanAmount = LoanAmount
        Credit_History = credit
        Loan_Amount_Term = Loan_Amount_Term
        Self_Employed_Yes = employed_yes
        Property_Area_Semiurban = semiurban
        Property_Area_Urban = urban  
        Property_Area_Rural = rural       
        
        prediction = model.predict([[
							Dependents,
							ApplicantIncome,
							CoapplicantIncome,
							LoanAmount,
							Loan_Amount_Term,
							Credit_History,
							Gender_Male,
							Married_yes,
							Not_graduate,
							Self_Employed_Yes,
							Property_Area_Semiurban,
							Property_Area_Urban,
							Property_Area_Rural
						  ]])

        if(prediction[0]==True):
            prediction="Yes"
            
        else:
            prediction="No"
            
        return render_template("results.html", prediction_text=prediction)       
        
    else:
      return render_template("prediction.html")

    

if __name__ == "__main__":
    app.run(debug=True)