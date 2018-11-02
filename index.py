# -*- coding: utf-8 -*-

#importing libraries
from sklearn.externals import joblib
import inputScript

#load the pickle file
classifier = joblib.load('final_models/rf_final.pkl')

#input url
print("enter url")
url = input()

print("If output = [-1] -> Safe Website")
print("If output = [1] -> Phishing Website")

#checking and predicting
checkprediction = inputScript.main(url)
prediction = classifier.predict(checkprediction)

print(prediction)


