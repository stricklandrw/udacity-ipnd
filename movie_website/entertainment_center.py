import fresh_tomatoes
import media

'''Use of media class:
movie_name = media.Movie("name",
                       "desc",
                       "poster_image",
                       "trailer_link")
'''

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hunger_games = media.Movie("Hunger Games",
                           "A post-apocalyptic yearly reality show with only one winner",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

serenity = media.Movie("Serenity",
                       "A space-based Western with a rag-tag crew and their mysterious passengers",
                       "http://www.media2.hw-static.com/wp-content/uploads/serenity-movie-poster_2445487-288x392.jpeg",
                       "https://www.youtube.com/watch?v=AAL6qVciZMA")

avengers = media.Movie("Marvel - The Avengers ",
                       "Superheroes unite to save the world",
                       "https://vignette.wikia.nocookie.net/marvelheroes/images/9/98/Avengers-movie-poster-1.jpg/revision/latest?cb=20170713041606",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

real_steel = media.Movie("Real Steel",
                       "Rock-em, Sock-em robots",
                       "https://vignette.wikia.nocookie.net/disney/images/5/5c/Real_Steel_Poster_03.jpg/revision/latest?cb=20150423214524",
                       "https://www.youtube.com/watch?v=SwfmV3nn6QA")

harry_potter = media.Movie("Harry Potter and the Philosopher's Stone",
                       "A young boy learns he is a wizard",
                       "http://harrypotterfanzone.com/wp-content/2015/07/sorcerers-stone-one-sheet.jpg",
                       "https://www.youtube.com/watch?v=VyHV0BRtdxo")

capt_america = media.Movie("Captain America: The First Avenger",
                       "A rejected draftee becomes a super soldier",
                       "http://www.impawards.com/2011/posters/captain_america_the_first_avenger_ver6.jpg",
                       "https://www.youtube.com/watch?v=-J3HfllvXWE")

baseketball = media.Movie("BASEketball",
                       "A parody on the state of professional sports",
                       "http://www.impawards.com/1998/posters/baseketball_xlg.jpg",
                       "https://www.youtube.com/watch?v=GHQrDlhnl_I")

'''Define list of movies to use as inputs to fresh_tomatoes.py'''
movies = [toy_story, avatar, hunger_games, serenity, avengers, real_steel, harry_potter, capt_america, baseketball]

'''Call function open_movies_page from fresh_tomatoes.py using the list of movies '''
fresh_tomatoes.open_movies_page(movies)
