def imdbabove5_5(movie):
    imdb = movie.get('imdb')
    if imdb>5.5:
        return True 
    else:
        return False 
movie = {
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
}
print(imdbabove5_5(movie))