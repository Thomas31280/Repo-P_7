import googlemaps
import wikipedia

import config


# Set an instance of Google Maps
gmaps = googlemaps.Client(key=config.MAPS_API_KEY)
wikipedia.set_lang("fr")

class Process:

    @classmethod
    def parser(cls, userquestion):

        words_to_ignore = ["Salut", "GrandPy", "!", "Est-ce", "que", "tu", "connais", "l'adresse", "?"]
        output_value = ''

        for word in userquestion.split():

            if word in words_to_ignore:
                pass
            else:
                output_value += (word + ' ')
        
        return output_value
        

    @classmethod
    def google_maps_API(cls, question_parsed):
        
        try:
            # Geocoding the parsed adress
            geocode_result = gmaps.geocode(question_parsed)
            response = {"coordinates": geocode_result[0]['geometry']['location'], 
                        "adress": geocode_result[0]['formatted_address']}

            return response
        
        except:
            # In case of failure
            return "ERROR : This adress couldn't been find..."
    

    @classmethod
    def wikipedia_API(cls, adress):

        first_part_of_the_adress = ''
        
        # We only extract the first part of the adress, wich one we want to send to wikipedia API. 
        # This fisrt part is before the first comma...
        try:
            for letter in adress:
                if letter != ',':
                    # We don't want the digits, it would disturb the Wiki API...
                    if not letter.isdigit():
                        first_part_of_the_adress += letter
                else:
                    break

            summary = wikipedia.summary(first_part_of_the_adress)                            # We get the summary...
            page = wikipedia.page(first_part_of_the_adress)                                  # ... then stock the page in a variable...
            url_to_the_page = page.url                                                       # ... to finally get the url of this wiki's api object.
            
            response = {"summary": summary, "url": url_to_the_page}
            
            return response
        
        except:

            return "ERROR : We couldn't find more informations on wikipedia for this adress..."