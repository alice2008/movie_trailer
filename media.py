
import webbrowser
class Movie():
	"""Movie baisc class."""

	def __init__(self, title, story_line, poster_image_url, trailer_url):
		self.title = title
		self.story_line = story_line
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_url

	def showTrailer(self):
		webbrowser.open(self.trailer_url)
