from flask import Flask, render_template, url_for, request, jsonify
import googlemaps
from datetime import datetime

import static
import config
from utils import Process

app = Flask(__name__)
app.config.from_object('config')

# Set an instance of Google Maps
gmaps = googlemaps.Client(key=config.MAPS_API_KEY)


@app.route('/')
@app.route('/index/')
def index():
    
    dictionary = {'lat': 46.3458880, 'lng': 2.432046}

    return render_template('index.html', lat=dictionary['lat'], lng=dictionary['lng'], zoom=5, marker=0)

@app.route('/mapview')
def mapview():
    
    # Geocoding an address
    geocode_result = gmaps.geocode('Aéroport de Paris-Charles de Gaulle')
    coordinates = geocode_result[0]['geometry']['location']
    return render_template('index.html', lat=coordinates['lat'], lng=coordinates['lng'], zoom=12, marker=1)

@app.route('/chatProcess', methods= ['POST'])
def chatProcess():

    userQuestion = request.form['userQuestion']                                # We define 2 variables. The first is directly related to the values of the forms in HTML, and the second is the the text to display in the browser.
    output = userQuestion

    if userQuestion:
        
        # We process the question in the parser
        # We stock it in a variable
        question_parsed = Process.parser(userQuestion)
        print(question_parsed)

        # We call the Google Maps API with the result of the parser
        # We stock the answer in a variable
        adress = Process.google_maps_API(question_parsed)['adress']
        coordinates = Process.google_maps_API(question_parsed)['coordinates']

        print('Here is the adress :', adress)
        print('Here are the coordinates :', coordinates)

        # We call the Wiki API with the adress returned by Google Maps
        # We stock the answer in a variable
        summary = Process.wikipedia_API(adress)['summary']
        url = Process.wikipedia_API(adress)['url']

        print("Here is the summary :", summary)
        print("Here is the url :", url)

        # We return all the results in a JSON file to display correctly with ajax in the template
        
        return jsonify({'output': output})                                     # The return jsonify( {‘output’:output} ) will return output as a json data

    else:
        return jsonify({'error' : 'Missing data!'})                            # If there is no data required in the JSON returned by the AJAX part, we return a JSON who says data missing



if __name__ == "__main__":
    app.run()
