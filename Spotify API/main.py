from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

# Songs scraping from the BillBoard.
choice = input("Which year you would like to travel to? (YYYY-MM-DD) : ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{choice}")
response.raise_for_status()

soup = BeautifulSoup(markup=response.text, from_encoding="UTF-8", features="html.parser")
songs_link = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

songs_name = []
for song in songs_link:
    songs_name.append(song.text)


# Setting up Spotify API, creating a playlist.
clientId = "9684b8d7aea84c498563837bb9e672cb"
clientSecret = "22f5149a43e841fb81435822c255aa20"
scope = "playlist-modify-private"

# Spotify OAuth2 for adding songs in the newly created playlist.
spotipyObj = SpotifyOAuth(client_id=clientId, client_secret=clientSecret, redirect_uri="https://example.com/eshaanplaylist/", scope=scope)
token = spotipyObj.get_cached_token()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/eshaanplaylist/",
        client_id=clientId,
        client_secret=clientSecret,
        show_dialog=True,
        cache_path=".cache"
    )
)

userID = sp.current_user()['id']
year = choice.split('-')[0]

# Pretty Print.
pp = pprint.PrettyPrinter()

songs_uri = []
for song in songs_name:
    result = sp.search(f"track:{song} year:{year}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        songs_uri.append(uri)
    except:
        print(f"The song, {song}, does not exist in spotify")

pp.pprint(songs_uri)

# Creating and adding songs in the playlist.
playlist = sp.user_playlist_create(user=userID, name=f"{choice} Billboard top 100.", public=False)
playlistId = playlist['id']
sp.playlist_add_items(playlist_id=playlistId, items=songs_uri)
