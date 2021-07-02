# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Load the Random Forest CLassifier model
#filename =
classifier = pickle.load(open('lgbm_model.plk', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":

        # Gender Male or Female
        
        # Gender Male or Female`
        Gender=request.form['Gender']
        if (Gender=='Male'):
            Gender=0
        else:
            Gender=1
            
        
        # Age
        Age=int(request.form['Age'])
        
        # Region_code
        Region_Code=int(request.form['Region_Code'])
        
        ## Occupation
        Occupation = request.form["Occupation"]
        if (Occupation=='Salaried'):
            Occupation=0
        elif(Occupation=='Self_Employed'):
            Occupation=1
            
        elif(Occupation=='Other'):
            Occupation=2
        else:
            Occupation=3
        
        ##Channel_code
        
        Channel_Code=int(request.form['Channel_Code'])
        
        ##Vintage
        
        Vintage=int(request.form['Vintage'])
        
        ## Credit_product
        
        Credit_Product=request.form['Credit_Product']
        if (Credit_Product=='Yes'):
            Credit_Product=2
        elif(Credit_Product=='No'):
            Credit_Product=1
        else:
            Credit_Product=0
        
        ## Average_account_balance 
        
        Avg_Account_Balance=int(request.form['Avg_Account_Balance'])
        
        ## Is active
        
        Is_Active=request.form['Is_Active']
        if (Is_Active=='Yes'):
            Is_Active=1
        else:
            Is_Active=0

        
        my_prediction=classifier.predict([[
            Gender,
            Age,
            Region_Code,
            Occupation,
            Channel_Code,
            Vintage,
            Credit_Product,
            Avg_Account_Balance,
            Is_Active
        ]])

        
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)