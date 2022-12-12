import os

# Makes the token an environment variable for security reasons

#Create secret key for WTF-forms
class Config(object):
	
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'development-key'
  
  
 

