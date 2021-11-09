from flask import Flask, request, render_template
import pickle

file1 = open('bodyfatmode.pk1', 'rb')
rf = pickle.load(file1)
file1.clos()


app = Flask(__name__)

# route is used to get from one template to another template
# '/' is just the home page
@app.route('/', methods = ['GET','POST']) # web programming standards protocols
def predict():
    if request.method == 'POST':
        my_dict = request.form

        density = float(my_dict['density'])
        abdomen = float(my_dict['abdomen'])
        chest = float(my_dict['chest'])
        weight = float(my_dict['weight'])
        hip = float(my_dict['hip'])

        input_features = [[density, abdomen, chest, weight, hip]]
        prediction = rf.predict(input_features)[0].round(2)

        string = 'Percentage of Body Fat Estimated is :' +str(prediction)+'%'

        return render_template('show.html', string = string)
    return render_template('home.html')