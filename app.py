import numpy as np
import pickle
from flask import Flask,request, jsonify, render_template
app= Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    value=request.form
    int_features =[int(x) for x in value.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    output=round(prediction[0][0],2)
    return render_template('index.html', prediction_text='Predicted Expenditure of Customer is ${}'.format(output))
if __name__=="__main__":
    app.run(debug=True)
