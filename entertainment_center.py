#importing the file to render the webpage(tomatoes.py) and page that handles all creations of objects created.
import fresh_tomatoes
import media


#6 movies, as objects taking all information that will be passed through class Movie
toy_story = media.Movie("Toy Story",
                        "A story about bot and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")


avatar = media.Movie("Avatar",
                     "It deals with blue aliens",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=_i2RCBa3l-g")
                     


fightclub = media.Movie("Fight Club",
                        "Its about Soap",
                        "http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                        "http://www.youtube.com/watch?v=J8FRBYOFu2w")


wallE = media.Movie("Wall-E",
                    "About a robot that dreamed big!",
                    "http://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                    "http://www.youtube.com/watch?v=ZisWjdjs-gM")

pulpfiction = media.Movie("Pulp Fiction",
                          "Day in LA like Elmore Leonard would write",
                          "http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                          "www.youtube.com/watch?v=wZBfmBvvotE")


bigredone = media.Movie("Big Red One",
                        "WWII movie",
                        "http://upload.wikimedia.org/wikipedia/en/6/60/Big_red_one_post.jpg",
                        "http://www.youtube.com/watch?v=Z7jwYpAM6RU")


#python data structure of type array 
movies = [toy_story,avatar, fightclub, wallE, pulpfiction, bigredone]                      
                        

#call to tomatoes.py to render the page. 
fresh_tomatoes.open_movies_page(movies)
