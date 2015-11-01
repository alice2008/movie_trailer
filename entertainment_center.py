from fresh_tomatoes import open_movies_page
from media import Movie
def main():
	forrest_gump = Movie('Forrest Gump', 'Depicts a life of a man',
		'https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg',
		'https://www.youtube.com/watch?v=uPIEn0M8su0')

	avatar = Movie('Avatar', 'A man tries to save the planet Pandora',
		'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
		'https://www.youtube.com/watch?v=5PSNL1qE6VY')

	shawshank = Movie('The Shawshank Redemption', 'A innocent banker tries to escape from prison',
		'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg',
		'www.youtube.com/watch?v=6hB3S9bIaco')

	three_idiots = Movie('3 Idiots', 'Two friends are looking for a long-lost friend',
		'https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg',
		'www.youtube.com/watch?v=xvszmNXdM4w')

	movie_list = [forrest_gump, avatar, shawshank, three_idiots]
	open_movies_page(movie_list)


if __name__ == '__main__':
	main()