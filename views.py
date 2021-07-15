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

devices_data = {} # dict to store data of devices
devices_location = {} # dict to store coordinates of devices

@app.route('/')
@app.route('/index/')
def index():

    return render_template('index.html')


@app.route('/mapview', methods=['GET', 'POST'])
def mapview():
    # json_data = request.get_json(silent=True)
    # get json request

    json_data = { # for testing
        'user' : {
            'x' : 37.50611,
            'y' : 127.0616346
        },
        'devices' : [
            {
                'id' : '0001',
                'x' : 37.5077121,
                'y' : 127.0624397,
                'data' : 'something'
            }
        ]
    }

    user_location = (json_data['user']['x'], json_data['user']['y'])
    # json example : { 'user' : { 'x' : '300' , 'y' : '300' } }
    # get user_location from json & store as turple (x, y)

    devices_data[str(json_data['devices'][0]['id'])] = (
        json_data['devices'][0]['data']
    )

    devices_location[str(json_data['devices'][0]['id'])] = (
        json_data['devices'][0]['x'], 
        json_data['devices'][0]['y']
    )
    # json example : { 'devices' : { 'id' : '0001', x' : '500', 'y' : '500' }, { ... } }
    # get device_location from json & store turple (x, y) in dictionary with device id as key
    # use for statements or something to get more locations from more devices

    circle = { # draw circle on map (user_location as center)
        'stroke_color': '#0000FF',
        'stroke_opacity': .5,
        'stroke_weight': 5,
        # line(stroke) style
        'fill_color': '#FFFFFF', 
        'fill_opacity': .2,
        # fill style
        'center': { # set circle to user_location
            'lat': user_location[0],
            'lng': user_location[1]
        }, 
        'radius': 500 # circle size (50 meters)
    }

    map = Map(
        identifier = "map", varname = "map",
        # set identifier, varname
        lat = user_location[0], lng = user_location[1], 
        # set map base to user_location
        zoom = 15, # set zoomlevel
        markers = [
            {
                'lat': devices_location['0001'][0],
                'lng': devices_location['0001'][1],
                'infobox': devices_data['0001']
            }
        ], 
        # set markers to location of devices
        circles = [circle] # pass circles
    )

    return render_template('exemple.html', map=map) # render template


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
