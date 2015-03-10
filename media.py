#calls standard python library to open up webbrowser and render HTML file
import webbrowser 

#class of movie with its constructors to create a place in memory
class Movie():
 
    #function - to inital information from the object(s) that will created on
    #entertainment center that is in an array
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #webbrowser functionality and rendering
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
