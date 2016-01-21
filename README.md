# Movie Trailers website
Movie trailers website generation project will generate a static html file
that will display a list of movies and the users can view trailers from
the website.

## Getting Started
Download the python modules into your local machine.
It contains 4 files:
* entertainment_movies.py
* media.py
* fresh_tomatoes.py
* README.md

**Note:** Make sure all the files are in the same directory

entertainment_movie.py is your main file. Run/Build the file.
You will see a static webpage that gets opened in the browser
where you can see the movies information. When you click on any
of the movies, trailer of that movie will be played

## Prerequisites for running 
* Python should be installed
* Any web browser(Chrome or firefox)

##Code details
*  **media.py**  contains the Movie class that holds movie properties
like title, storyline, poster url, trailer url
*  **entertainment_movie.py** is the main module that creates a couple
of instances of the Movie class and creates a list out of these movies
*  **fresh_tomatoes.py** is the module that takes the list of movies 
created by ```entertainment_movie.py``` and creates a static webpage with these
movies.

##Testing : Done 
