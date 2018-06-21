import webbrowser

class Movie():
    '''This class provides a way to store movie-related information.'''

    '''Set static variable of movie ratings to be used later'''
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''
        Args:
            movie_title: string of the movie's title
            movie_storyline: string detailing plotline summary of movie
            poster_image: string of URL of the movie's poster image
            trailer_youtube: string of URL of the movie's trailer - official if available
        Behavior:
            sets initial required variables in class
        Returns:
            variables set for use in other functions
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''
        Args:
            none
        Behavior:
            uses webbrowser class to open a URL set in class initialization
        Returns:
            new browser window with URL of trailer_youtube_url
        '''
        webbrowser.open(self.trailer_youtube_url)
