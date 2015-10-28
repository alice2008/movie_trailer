
import media
avatar = media.Movie("avatar", "a man survive on an alien planet", "not url")
print avatar.story_line
print avatar.__module__, media.Movie.__name__
print dir(avatar)
print avatar.__doc__, media.Movie.__doc__