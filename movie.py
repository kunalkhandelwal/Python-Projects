# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:20:34 2021

@author: kkhan
"""

import imdb
hr = imdb.IMDb()
movie_name= input("Please enter the name of the Movie: ")
movies = hr.search_movie((str()))
index =movies[0].getID()
movie = hr.get_movie(index)
title= movie['title']
year= movie['year']
cast= movie['cast']
list_of_cast = " ,".join(map(str,cast))
print("Title of the Movie:\n",title)
print("Year of Release of the Movie:\n",year)
print("Full Cast of the Movie:\n",list_of_cast)