from flask import Flask, render_template, url_for, request, jsonify
from flask_googlemaps import GoogleMaps, Map

import static
import config

app = Flask(__name__)
app.config.from_object('config')

# Set key as config
app.config["GoogleMaps_Key"] = config.MAPS_API_KEY

# Initialize the extension
GoogleMaps(app)


@app.route('/')
@app.route('/index/')
def index():

    return render_template('index.html')


@app.route('/mapview')
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('exemple.html', mymap=mymap, sndmap=sndmap)


@app.route('/chatProcess', methods= ['POST'])
def chatProcess():

    userQuestion = request.form['userQuestion']                                # We define 2 variables. The first is directly related to the values of the forms in HTML, and the second is the the text to display in the browser.
    output = userQuestion

    if userQuestion:
        return jsonify({'output': output})                                     # The return jsonify( {‘output’:output} ) will return output as a json data

    else:
        return jsonify({'error' : 'Missing data!'})                            # If there is no data required in the JSON returned by the AJAX part, we return a JSON who says data missing



if __name__ == "__main__":
    app.run()
