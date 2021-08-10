$(document).ready(function() {                                                             // We use $ in jQuery to select an element. En jQuery, on appelle une méthode sur un objet ( ou un ensemble d'objets). Les étapes sont simple pour utiliser une méthode jQuery.   1) On sélectionne un élément convertit en un objet jQuery avec $().   2) On met un point.   3) On met le nom de la méthode.   4) On met des parenthèses, vides ou contenant des paramètres.   This line in particular tell to the browser to run the fonctions after the document that is HTML is fully loaded.
    $('form').on('submit', function(event) {                                               // Si on reprend les étapes citées ci-dessus, on doit donc avoir : $("element").méthode("paramètres")    C'est exactement le cas ici !!!! On sélectionne l'élément HTML form que l'on convertit en objet jQuery, puis on utilise la méthode .on dessus ( un event listener donc ), et on place les paramètres requis dans les parenthèses.

        $.ajax({                                                                           // Here we define the AJAX part...
            data : {                                                                       // ... Inside the AJAX, we put in a dictionnary ( we can consider it as a JSON object ) the fields values of #firstName and #lastName...
            userQuestion : $('#userQuestion').val()
            },
            type : 'POST',                                                                 // ... Then we define the request method ( POST here, who means 'send the data to the server' )...
            url : '/chatProcess'                                                           // ... And obvioulsy we define the server route for the flask post method that will perform the tasks on the JSON data.
        })
        .done(function(data) {                                                             // At the end of the process on the JSON data send to the flask method...
         console.log(data)
            if(data.question == 'Ok'){
                if (data.maps_api_call == 'Ok'){
                    if(data.wiki_api_call == 'Ok'){
                        $('#output_question').text(data.outputQuestion).show();                                          // ... show the result in the HTML object with the ID "output"
                        $('#address').text('Bien sûr mon poussin ! La voici : ' + data.address).show();
                        $('#summary').text("Laisse moi te présenter l'endroit : " + data.summary).show();
                        $('#url').text('Si tu souhaites en savoir plus, clique ici !').attr("href", data.url).show();


                        displayMap.call(this, data.coordinates['lat'], data.coordinates['lng'])
                    }
                    else{
                        $('#output_question').text(data.outputQuestion).show();
                        $('#address').text('Bien sûr mon poussin ! La voici : ' + data.address).show();
                        $('#summary').text("Par contre, pour le coups, je ne peux pas t'en dire plus sur cet endroit, je n'ai rien trouvé...").show();
                        $('#url').text('').show();
                        
                        displayMap.call(this, data.coordinates['lat'], data.coordinates['lng'])
                    }
                }
                else{
                    $('#output_question').text(data.outputQuestion).show();
                    $('#address').text('Alors là mon poussin, tu me pose une colle !').show();
                    $('#summary').text('').show();
                    $('#url').text('').show();
                
                    // We don't display the map in that case.
                    $('#map').text('').show();
                }
            }

            else{
                $('#output_question').text('ERROR : Missing data !').show();
                $('#address').text('').show();
                $('#summary').text('').show();
                $('#url').text('').show();

                // Again, we don't display the map in that case.
                $('#map').text('').show();
            }

        });
     event.preventDefault();
     });
});


// Initialize and add the map
function displayMap( lat, lng) {

    // The location
    const location = { lat: lat, lng: lng };
    // The map, centered at location
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: location,
    });
    // The marker, positioned at location
    const marker = new google.maps.Marker({
        position: location,
        map: map
    });
}
