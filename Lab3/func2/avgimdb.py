def avg(movies):
    totalscore = 0
    count = 0
    for movie in movies:
        imdb = movie.get('imdb')
        totalscore+=imdb 
        count+=1 
    avg = totalscore/count 
    return avg 
movies = [
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
}
]
print(avg(movies))