import os
from threading import Thread
from flask import Flask, render_template, request, redirect
import openai

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.cache_handler import MemoryCacheHandler

cid = os.environ['cid']
csecret = os.environ['csecret']
cache_handler = MemoryCacheHandler()
app = Flask('discord bot')
my_secret = os.environ['OPNAI']
# Set up OpenAI API credentials
openai.api_key = my_secret


# Define function to generate song recommendations based on book name
def generate_song_recommendations(xp, c):
  if c == 0:
    pp = 'Could you please make me a list of 10 songs which match the vibe of the book "' + xp + '"?'
  else:
    pp = 'Could you please make me a list of 10 hindi songs which match the vibe of the book "' + xp + '"?'
  xx = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                    messages=[
                                      {
                                        "role":
                                        "system",
                                        "content":
                                        "You are someone who recommends songs."
                                      },
                                      {
                                        "role": "user",
                                        "content": pp
                                      },
                                    ])

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


  hh = [xt[:10],xt[10:]]

  print(g)
  return g


def recoclean2(r):
  cg = []
  for i in r:
    if i == '':
      pass
    else:
      cg.append(i)

  if len(cg) > 9:
    cg = cg[:-1]
  else:
    cg = cg
  return cg


def recoclean1(r):
  cg = []
  for i in r:
    if i == '':
      pass
    else:
      cg.append(i)
  return cg


'''  if len(cg) > 9:
    cg = cg[:-1]
  else: 
    cg = cg'''


def recoorg2(xt):
  song_names = []
  artist_names = []

  for song in xt:
    if xt == '':
      pass
    # split each item into song name and artist name
    split_song = song.split(" - ")
    #    print(split_song)
    song_name = split_song[0].split(". ")[1]
    print(split_song)
    artist_name = split_song[1]

    # append to respective lists
    song_names.append(song_name.strip('"'))
    artist_names.append(artist_name)
  return [song_names, artist_names]


def recoorg(xt):
  song_names = []
  artist_names = []

  for song in xt:
    if xt == '':
      pass
    # split each item into song name and artist name
    split_song = song.split(" by ")
 #   print(split_song)
    song_name = split_song[0].split(". ")[1]
    artist_name = split_song[1]

    # append to respective lists
    song_names.append(song_name.strip('"'))
    artist_names.append(artist_name)
  return [song_names, artist_names]


def dec(xt):
  for l in xt:
    if " by " in l:
      return recoorg(xt)
    else:
      return recoorg2(xt)


def get_spotify_url(song_names, artist_names):
  cc = []
  #Authentication - without user
  client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=csecret, cache_handler=cache_handler)
  sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

  for i in range(len(song_names)):

    try:  # Precise Search
      #        print("artist:"+artist_names[i]+" track:"+song_names[i])
      results = sp.search(q="artist:" + artist_names[i] + " track:" +
                          song_names[i],
                          type='track')
      #        print (results['tracks']['items'][0]['external_urls']['spotify'])
      #        url = results['tracks']['items'][0]['external_urls']['spotify']
      sid = results['tracks']['items'][0]['id']
      cc.append(sid)
    except:  # Fuzzy Search
      #        print("artist:"+artist_names[i]+" track:"+song_names[i])
      results = sp.search(q=song_names[i], type='track')
      #        print (results['tracks']['items'][0]['external_urls']['spotify'])
      #        url = results['tracks']['items'][0]['external_urls']['spotify']
      sid = results['tracks']['items'][0]['id']
      cc.append(sid)
  return cc


# Define Flask routes
@app.route("/")
def index():
  return render_template("index.html")


@app.route("/recommendations", methods=["POST"])
def recommendations():
  book_name = request.form["book_name"]
  if book_name:

    reco = generate_song_recommendations(book_name, 0)
    gf = dec(recoclean2(reco))
    gt = get_spotify_url(gf[0], gf[1])
    print(gt)
    return render_template("recospot.html", reco=gt)
  else:
    return redirect("https://song.pustak.me", code=302)


@app.route("/recohindi", methods=["POST"])
def recohindi():
  book_name = request.form["book_name"]
  if book_name:

    reco = generate_song_recommendations(book_name, 1)
    gf = dec(recoclean2(reco))
    print(gf)
    gt = get_spotify_url(gf[0], gf[1])
    print(gt)
    return render_template("recospot.html", reco=gt)
  else:
    return redirect("https://song.pustak.me", code=302)

    # Show the spinner while we generate the song recommendations


#    return """
  '''      <html>
            <head>
                <title>Loading...</title>
            </head>
            <body>
                <div id="loading-spinner">
                    <i class="fa fa-spinner fa-spin"></i> Generating song recommendations...
                </div>
                <script src="/static/js/main.js"></script>
            </body>
        </html>
    """
'''
'''@app.route("/recommendations", methods=["POST"])
def recommendations():
    book_name = request.form["book_name"]
    reco = generate_song_recommendations(book_name)
    recoorg(recoclean1(reco))
    return render_template("reco2.html", reco=reco)'''


def start_server():
  app.run(host='0.0.0.0', port=8080)


t = Thread(target=start_server)
t.start()
