from flask import Flask, render_template, request, redirect
import requests
import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure, reset_output

app = Flask(__name__)

@app.route('/') # http://127.0.0.1:33507/index
def index():
    return render_template('user_inputs2.html')
    
    
@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
