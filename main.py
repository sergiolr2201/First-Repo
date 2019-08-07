#main.py
# the import section
import webapp2

# the handler section
class HomePage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
    
        
class InternshipsPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        
        
class ContactPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'


class AboutPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'

        
# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage),  ('/internships', InternshipsPage), ('/contact', InternshipsPage),
    ('/aboutpage', AboutPage)#this maps the root url to the Main Page Handler
], debug=True)