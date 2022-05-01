from copyreg import pickle
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


    kitchen = data['meters']
    bathroom = data['bathroom']
    frontal = data['zip']
    bedroom = data['bedrooms']
    images = data['images']


    #Ejecutamos nuestro modelo para ver si se pasan todas las fotos
    try:
        print("Aqui entra")
        data = app.model.getScoreImages(images[0], images[1], images[2], images[3])
        print(data)
        output = app.decisionTree.predict(data)
        return redirect(url_for('results'), score = format(output)) #Si va fino
    except Exception as e:
        print(e)
        flash('Error al conectarse a la base de datos.')

@app.route('/info')
def results():
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