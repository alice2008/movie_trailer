
class Movie():
	"""Movie's doc string."""

	def __init__(self, title, story_line, poster_image_url):
		self.title = title
		self.story_line = story_line
		self.poster_image_url = poster_image_url

	def __showTrailer(self):
		print self.poster_image_url
