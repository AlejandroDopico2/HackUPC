from copyreg import pickle
from curses import meta
from email.mime import image
from flask import (
    Flask,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    send_from_directory
)
import os
from flask_cors import CORS
from numpy import imag
from psycopg2 import paramstyle
from model import *
import pickle
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
app.debug = True
CORS(app)
app.secret_key = 'somesecretkeythatonlyishouldknow'
app.model = ScoreImage() #Aquí ponemos una instancia de nuestro modelo
app.decisionTree= pickle.load(open('model.pkl', 'rb'))


@app.route("/results", methods=['POST'])
def upload():
    # data = request.form.to_dict()
    # data = dict(request.form)
    data = request.get_json()


    meters = data['meters']
    bathroom = data['bathroom']
    zipCode = data['zip']
    bedroom = data['bedrooms']
    image1 = data["image1"]
    image2 = data["image2"]
    image3 = data["image3"]
    image4 = data["image4"]

    #Ejecutamos nuestro modelo para ver si se pasan todas las fotos
    try:
        scores = app.model.getScoreImages([image1, image2, image3, image4])
        parameters = [bedroom, bathroom, meters, zipCode]
        # decisionTreeInput = scores 
        # np.append(decisionTreeInput, bedroom)
        # np.append(decisionTreeInput, bathroom)
        # np.append(decisionTreeInput, meters)
        # np.append(decisionTreeInput, zipCode)

        decisionTreeInput = np.array(scores + parameters)

        print(decisionTreeInput)

        output = app.decisionTree.predict(decisionTreeInput.reshape(1, -1))
        print(output) # Hasta aqui va bien
        
        # return redirect(url_for('results')) #Si va fino
        return str(output[0])
    except Exception as e:
        print(e)
        return "error: " + e
        flash('Error al conectarse a la base de datos.')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route("/")
def root():
    return render_template('index.html')
    # return redirect(url_for('index.html'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/about_us")
def aboutUs():
    return render_template('about_us.html')

@app.route('/results')
def results():
    return render_template('results.html')