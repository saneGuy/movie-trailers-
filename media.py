import webbrowser  # webbrowser package is to open websites


class Movie():

    """ Movie class hold attributes like title, storyline, poster_image_url,
    trailer_youtube_url and a method show_trailer() """

    # __init__() is the constructor for the Movie class that takes the function
    # arguments and assign them to the instance variables title, storyline,
    # poster_image_url, trailer_youtube_url
    def __init__(self, movie_title, movie_storyline, poster, trailer_youtube,
                 movie_actor, movie_director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_youtube
        self.actor = movie_actor
        self.director = movie_director

    # show_trailer method opens the youtube url stored in trailer_youtube_url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
