# the import section
import webapp2
import jinja2
import os
from webapp2_extras import sessions
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



def getCurrentUser(self):
  #will return None if user does not exist
  return self.session.get('user')

def login(self, id):
  self.session['user'] = id

def logout(self):
  self.session['user'] = None

def isLoggedIn(self):
  if self.session['user'] is not None:
    return True
  else:
    return False

# the handler section
class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

class KevinHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    welcome_template = the_jinja_env.get_template('main.html')
    self.response.write(welcome_template.render())

class SignupHandler(BaseHandler):
  def get(self):  # for a get request
    welcome_template = the_jinja_env.get_template('signup.html')
    self.response.write(welcome_template.render())

  def post(self):
    signup_template = the_jinja_env.get_template('signup.html')
    username = self.request.get('username')
    email = self.request.get('email')
    password = self.request.get('password')

    user = User(username = username, email = email, password = password)
    user_id = user.put()
    login(self, username)
    variable_dict = {"username": username}
    self.response.write(signup_template.render(variable_dict))

class AccountHandler(BaseHandler):
  def get(self):  # for a get request
    acct_template = the_jinja_env.get_template('account.html')
    user = getCurrentUser(self)
    if user is not None:
      user_info = User.query().filter(User.username == getCurrentUser(self)).fetch()
      variable_dict = {"username": user_info[0].username, "email": user_info[0].email}
      self.response.write(acct_template.render(variable_dict))
    else:
      #send user back to home/login if they're not signed in
      self.redirect('/')

class LogoutHandler(BaseHandler):
  def get(self):  # for a get request
    logout_template = the_jinja_env.get_template('logout.html')
    user = getCurrentUser(self)
    if user is not None:
      logout(self)
      self.response.write(logout_template.render())
    else:
      self.redirect('/')

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'your-super-secret-key',
}


# the app configuration section	
app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/game', GameHandler),
  ('/login', LoginHandler),
  ('/instructions', InstructionsHandler),
  ('/kevin', KevinHandler),
  ('/signup', SignupHandler),
  ('/account', AccountHandler),
  ('/logout', LogoutHandler),
  ], debug=True, config=config)



#############################










