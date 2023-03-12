import os
from threading import Thread
from flask import Flask, render_template, request
import openai

app = Flask('discord bot')
my_secret = os.environ['OPNAI']
# Set up OpenAI API credentials
openai.api_key = my_secret

# Define function to generate song recommendations based on book name
def generate_song_recommendations(xp):
  pp = 'Could you please make me a list of songs which match the vibe of the book "'+xp+'"?'
  
  xx = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
          {"role": "system", "content": "You are someone who recommends songs."},
          {"role": "user", "content": pp},
      ]
  )
  
  #print(xx["choices"][0]["message"]["content"])
  
  edt = xx["choices"][0]["message"]["content"]
  
  cc = ""
  
  for i in edt:
      if i == ":":
          cc = ""
      elif i == "(":
          break
      else:
          cc += i
  xt = []
  g = cc.split('\n')
  for i in g:
    if i == '':
      pass
    else:
      xt.append(i)
#  hh = [xt[:10],xt[10:]]

  
  return g 

# Define Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommendations", methods=["POST"])
def recommendations():
    book_name = request.form["book_name"]
    reco = generate_song_recommendations(book_name)
    return render_template("reco2.html", reco=reco)

def start_server():
  app.run(host='0.0.0.0',port=8080)


t = Thread(target=start_server)
t.start()
