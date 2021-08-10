import googlemaps
import wikipedia

import config


# Set an instance of Google Maps...
gmaps = googlemaps.Client(key=config.MAPS_API_KEY)
wikipedia.set_lang("fr")

url_value_for_test = None


class Process:

    @classmethod
    def parser(cls, userquestion):

        words_to_ignore = config.STOP_WORD
        output_value = ''

        for word in userquestion.split():

            if word.lower() in words_to_ignore:

                pass
            else:
                output_value += (word.lower() + ' ')

        return output_value.rstrip()                                           # We remove the space at the end of the string

    @classmethod
    def google_maps_API(cls, question_parsed):

        try:
            # Geocoding the parsed adress
            geocode_result = gmaps.geocode(question_parsed)

            response = {"maps_api_call": 'Ok', "coordinates": geocode_result[0]['geometry']['location'],
                        "address": geocode_result[0]['formatted_address']}

            return response

        except:
            # In case of failure
            response = {"maps_api_call": 'Failure'}
            return response

    @classmethod
    def wikipedia_API(cls, adress):

        first_part_of_the_adress = ''

        # We only extract the first part of the address, wich one we want to send to wikipedia API.
        # This fisrt part is before the first comma...
        try:
            for letter in adress:
                if letter != ',':
                    # We don't want the digits, it would disturb the Wiki API.
                    if not letter.isdigit():
                        first_part_of_the_adress += letter
                else:
                    break

            summary = wikipedia.summary(first_part_of_the_adress)                            # We get the summary...
            page = wikipedia.page(first_part_of_the_adress)                                  # ... then stock the page in a variable...

            if url_value_for_test is None:
                url_to_the_page = page.url                                                   # ... to finally get the url of this wiki's api object.
            else:
                url_to_the_page = url_value_for_test

            response = {"wiki_api_call": 'Ok', "summary": summary,
                        "url": url_to_the_page}

            return response

        except:
            # In case of failure
            response = {'wiki_api_call': 'Failure'}
            return response
