#main.py
# the import section
import webapp2
import jinja2
import os
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class HomePage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        welcometemplate = JINJA_ENVIRONMENT.get_template('Template/FCD_Home.html')
        self.response.write(welcometemplate.render())
    
        
class InternshipsPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        welcometemplate = JINJA_ENVIRONMENT.get_template('Template/FCD_Internships.html')
        self.response.write(welcometemplate.render())
    

        
class ContactPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        welcometemplate = JINJA_ENVIRONMENT.get_template('Template/FCD_Contact.html')
        self.response.write(welcometemplate.render())


class AboutPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        welcometemplate = JINJA_ENVIRONMENT.get_template('Template/FCD_About_page.html')
        self.response.write(welcometemplate.render())

        
# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage),  ('/internships', InternshipsPage), ('/contact', ContactPage),
    ('/aboutpage', AboutPage),#this maps the root url to the Main Page Handler
], debug=True)