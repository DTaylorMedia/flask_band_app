from flask import Blueprint,render_template,request

my_view = Blueprint('my_view', __name__)

bands_list = []
class BandEntry(object):
	def __init__(self, song, album, artist, rating):
		self.song = song
		self.album = album
		self.artist = artist
		self.rating = rating

@my_view.route("/")
def index():
	return render_template("index.html")

@my_view.route("/helloworld")
def hello():
	return render_template("helloworld.html")

@my_view.route("/fav-bands", methods=['GET','POST'])
def fav_bands():
	if request.method == "POST":
		new_band = BandEntry(
			request.form["entry_song"],
			request.form["entry_album"],
			request.form["entry_artist"],
			int(request.form["entry_rating"])
		)
		bands_list.append(new_band)

	return render_template("favbands.html", bands = bands_list)