#main.py
# the import section
import webapp2
import os
import jinja2
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
        ships = get_all_internships()
        template_values = {
            'ships': ships, 
            'last updated': 'today',
        }
        self.response.write(welcometemplate.render(template_values))
    

        
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


class Internships(ndb.Model):
    #list here all the properties of the entity
    Title = ndb.StringProperty(required=True)
    Description = ndb.StringProperty(required=True)
    Link = ndb.StringProperty(required=True)
    
def get_all_internships():
    intern = Internships.query().fetch()
    print "intern"
    return intern 

        
# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage), 
     ('/internships', InternshipsPage), 
     ('/contact', ContactPage),
    ('/aboutpage', AboutPage),#this maps the root url to the Main Page Handler
], debug=True)
