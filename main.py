# the import section
import webapp2
import jinja2
import os
from models import User
from quiz import quiz 

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)




# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    start_template = the_jinja_env.get_template('templates/index.html')  # path to index.html
    self.response.write(start_template.render()) # render index.html
  def post(self):
    username=self.request.get('username')
    password=self.request.get('password')     
    user=User(username=username)
    user.put()
 
    start_template = the_jinja_env.get_template('templates/index.html')
    self.response.write(start_template.render())    

class GameHandler(webapp2.RequestHandler):
  def get(self):
	game_template = the_jinja_env.get_template('templates/game-start.html') # path to game-start.html
	self.response.write(game_template.render()) # render game-start.html
  def post(self):
  	answer = self.request.get("questionForm")

class LoginHandler(webapp2.RequestHandler):
  def get(self):
    login_template = the_jinja_env.get_template('templates/login.html') # path to login.html
    self.response.write(login_template.render()) # render login.html

class InstructionsHandler(webapp2.RequestHandler):
  def get(self):
	inst_template = the_jinja_env.get_template('templates/instructions.html') 
	self.response.write(inst_template.render()) 



class ScoreHandler(webapp2.RequestHandler):
   def get(self):
    score_template = the_jinja_env.get_template('templates/scoreboard.html')
    self.response.write(score_template.render())
        
class SignupHandler(webapp2.RequestHandler):
  def get(self):
    sign_template = the_jinja_env.get_template('templates/signup.html')
    self.response.write(sign_template.render())
    

# the app configuration section	
app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/game', GameHandler),
  ('/score', ScoreHandler),
  ('/signup',SignupHandler),
  ('/login', LoginHandler),
  ('/instructions', InstructionsHandler)
  ], debug=True)






