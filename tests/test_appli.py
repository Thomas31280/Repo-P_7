from flask_testing import LiveServerTestCase
from selenium import webdriver

from .. import app

class TestViews(LiveServerTestCase):

    def create_app(self):

        app.config.from_object("tests.config")
        return app


    def setUp(self):
        
        self.driver = webdriver.Firefox()


    def tearDown(self):
        
        self.driver.quit()


    def test_display_main_page():

        self.driver.get(self.get_server_url())
        assert self.driver.current_url == "http://127.0.0.1:5000/"
