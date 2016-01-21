import media
import webbrowser
import fresh_tomatoes

# Created instances of the movie for gabbarSingh , Nannaku Prematho,
# Bengal Tiger, nenu sailaja, express raja, soggade chinni nayana, dictator,
# bruce lee the fighter, size zero with Title, Story line, Poster Image,
# and Trailer Link
gabbarSinghSardar = media.Movie("Sardar Gabbar Singh", " The story of a Cop",
                                "http://www.hdwallpapers.in/walls/pawan_kalyan_sardaar_gabbar_singh-HD.jpg",
                                "https://www.youtube.com/watch?v=jiJtB8zjtMU")

nannakuPremato = media.Movie("Nannaku Prematho", "A revenge story of a son",
                             "http://www.belvoireagle.com/wp-content/uploads/2015/12/nannaku-prematho-new-poster-relased.jpg",
                             "https://www.youtube.com/watch?v=RwB6aOkmEgc")

bengalTiger = media.Movie("Bengal Tiger", "The story of a lucky guy"
                          " big", "http://www.apnewsforum.com/wp-content/gallery/ravi-teja-bengal-tiger-movie-posters/Ravi-Teja-Bengal-Tiger-Movie-First-Look-Wallpapers-8.jpg",
                          "https://www.youtube.com/watch?v=GCvipxfEnJY")

nenuSailaja = media.Movie("Nenu Sailaja", " A Love Story",
                          "http://rifflenow.com/wp-content/uploads/2015/12/Nenu-Sailaja-001.jpg",
                          "https://www.youtube.com/watch?v=i916BRRHoTg")

expressRaja = media.Movie("Express Raja", "A Love Story",
                          "http://data1.ibtimes.co.in/cache-img-423-0-photo/en/full/33128/1451455378_express-raja-upcoming-telugu-movie-written-directed-by-merlapeka-gandhi-produced-under-banner.jpg",
                          "https://www.youtube.com/watch?v=YDpRur0T9iQ")

soggade = media.Movie("Soggade Chinni Nayana", "A Romantic Comedy",
                      "http://www.cinekushi.com/wp-content/uploads/2015/12/scn-audio.jpg",
                      "https://www.youtube.com/watch?v=Or40avO08mE")

dictator = media.Movie("Dictator", "A typical Balayya movie",
                       "http://cdn.chitramala.in/wp-content/uploads/2015/10/NBK-Dictator-Teaser.jpg",
                       "https://www.youtube.com/watch?v=zTMVMdCseRM")

brueLee = media.Movie("Brue Lee The Fighter", "A Fighters love story",
                      "http://www.idlebrain.com/images5/posters-brucelee3.jpg",
                      "https://www.youtube.com/watch?v=JdSSm6waqgc")

sizeZero = media.Movie("Size Zero", "A fat girls story",
                       "http://www.cochintalkies.com/movie-gallery/poster-l/size-zero-movie-poster-7854.jpg",
                       "https://www.youtube.com/watch?v=RJyCHwQrECY")
# All the movie instances are added to a list, here movies is the list
# of all movies
movies = [gabbarSinghSardar, nannakuPremato, bengalTiger, nenuSailaja,
          expressRaja, soggade, dictator, brueLee, sizeZero]
# open_movies_page() method in fresh_tomatoes module will take the list of
# movies that are created and generates a webpage will all the movie info
# that is provided like title, poster image, youtube url
fresh_tomatoes.open_movies_page(movies)
