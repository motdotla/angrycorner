import pystache
import os
from angrycorner import app

def load_template(template_path, view_params):
  """ Load and parse the template """
  
  project_path  = os.path.join(os.path.dirname(__file__), os.pardir)
  template_path = project_path + '/templates/' + template_path
  
  file_handle   = open(template_path)
  body_html     = file_handle.read()
  file_handle.close()
  
  return pystache.render(body_html, view_params)

def layout(view_params):
  """ Handle the site layout template """
  
  # Defaults
  output_html = load_template('common/layout.html', view_params)
  
  return output_html

