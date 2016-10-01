import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "Toys coming to life", "wiki.toystory.link", "youtube.toystory")

##print (toy_story.title)

avatar = media.Movie("Blue Cats", "Europe invades America", "wiki.avatar", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

##print (avatar.trailer_youtube_url)
##avatar.show_trailer()

deadmau5 = media.Movie("mouse head", "sometimes good music", "info.DM", "https://www.youtube.com/watch?v=6rZtfgtDT1w")
##print deadmau5.title

##deadmau5.show_trailer()

movies = [toy_story, avatar, deadmau5]
##fresh_tomatoes.open_movies_page(movies)

##print media.Movie.RATINGS)

##print (media.Movie.__dict__)
print (media.Movie.__doc__)
print (media.Movie.__module__)
print (media.Movie.__bases__)
print (media.Movie.__name__)
