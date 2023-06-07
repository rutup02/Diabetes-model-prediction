import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import traceback
import pandas as pd

from model import x
from my_sql import mysqldata


#create the flask app
app = Flask(__name__)

#load the pickle model
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def Home():
    return  render_template("demo.html")

@app.route("/website")
def website():
    # output = request.form.to_dict()
    # prg = output["prg"]
    # output = request.form.to_dict()
    # glc = output["glc"]
    # output = request.form.to_dict()
    # bp = output["bp"]
    # output = request.form.to_dict()
    # st = output["st"]
    # output = request.form.to_dict()
    # inl = output["inl"]
    # output = request.form.to_dict()
    # bmi = output["bmi"]
    # output = request.form.to_dict()
    # dpf = output["dpf"]
    # output = request.form.to_dict()
    # age = output["age"]




    return render_template("website.html")

# @app.route("/result")
# def result():
#     return  render_template("result.html")

@app.route("/predict", methods = ['GET','POST'])

def predict():
    if request.method == 'POST':
        print("predicted function call")
        prg =request.form.get('prg')
        print(prg)
        glc = request.form.get('glc')
        print(glc)
        bp = request.form.get('bp')
        print(bp)
        st = request.form.get('st')
        print(st)
        inl = request.form.get('inl')
        print(inl)
        bmi = request.form.get('bmi')
        print(bmi)
        dpf = request.form.get('dpf')
        print(dpf)
        age = request.form.get('age')
        print(age)

    # query_df = pd.DataFrame(json_)
    # prediction = model.predict(query_df)
    # return jsonify({"Prediction":list(prediction)})
    float_features = [prg,glc,bp,st,inl,bmi,dpf,age]

    print(float_features)
    for i in range(0,len(float_features)):
        float_features[i] = float(float_features[i])
    print('modified list is: '+str(float_features))
    features = [np.array(float_features)]
    prediction = model.predict(features)
    print(prediction)

    mysqldata(prg, glc,bp,st,inl, bmi, dpf, age, prediction[0])

    # output = '{0:.{1}f}'.format(prediction[0],[1],2)

    # if output>str[0]:
    # return render_template("demo.html", prediction_text = "prediction is: ", pred='Your diabetes prediction is '+ str(prediction))
    if int(prediction) == 0:
        return render_template("website.html", prediction_text = "prediction is: ", pred='Your report is Negative! You do not have diabetes '+ str(prediction))
    if int(prediction) == 1:
        return render_template("website.html", prediction_text = "prediction is: ", pred='Your report is Positive! You have diabetes '+ str(prediction))
    # if output > str[1]:
    #     return render_template("website.html", prediction_text="prediction is: ", pred='You have diabetes because prediction is {}'.format(output))


if __name__ == "__main__":
    app.run(debug = True)





