# Capstone: Video Game Recommender


## Problem Statement

When it comes to video games, there is just too many to choose from. Even the most dedicated gamers most likely have not played all the games out there, and even if somone has, everyone has a different taste in video games. I wanted to create an recommender system that suggests games based on content and genre for anyone who has ever finished a game and wanted to find another one similar to it. Not only will my recommender give you a list of games most similiar to the one you already enjoy, but it might also introduce you to video games you have never heard of.


## Project Directory

**app**
- templates
    - home.html
    - recommendations.html
    - search.html
- games_final.csv
- recommender.csv (link can be found in data folder)
- recommender_app.py

**code**
- 01_Data_Collection.ipynb
- 02_Cleaning_Part_I.ipynb
- 03_Cleaning_Part_II_and_EDA.ipynb
- 04_Recommender.ipynb

**data**
- api_descriptions.csv
- cleaned_games.csv
- games_basic.csv
- games_final.csv
- link_to_recommender.txt (file too large to load onto GitHub)
- ratings.csv
- ready_to_model.csv
- summary_genres.csv

**README.md**


## Executive Summary

I collected over 2,500 metascored PC games off of Metacritic's website starting from 2010 until 2020. The name of the games, their metascore and user score, release date, summary, genres, and the image of their game cover were scraped from Metacritic using BeautifulSoup. Video game descriptions, store URLs, and any missing data were supplemented with data collected from the RAWG API. 

Right off the bat, I noticed that a couple of the games showed up multiple times in the data. This was due to the fact that they were episodic games, so each episode was getting scored as they came out and then again after the entire game was released. In addition, for some games, only a few of the episodes had a metascore while the full game did not. I was able to drop the individual episodes when I did have data on the full game, but had to combine the ones where I did not. I also had to drop games that were not longer playable or purchasable as the game servers have since been shut down. As for missing values, over half of the games did not have a rating because ratings are considered optional for PC games whereas they are mandatory for console manufacturers according to the ESRB. 

When it came to building the recommender on summary and description, I chose the longer of the two. Games that had a missing summary was imputed with the description and vice versa. As for the genre, I extracted only the unique genres from each game since Metacritic had a tendency to group two genres together into one in addition to included this two separate genres as well. The genres and summary/description were both tokenized and only the summary/description lemmatized with the stop words removed. After the text was clean, I used a CountVectorizer on the genres and a TFIDFVectorizer on the summary/description before combining the matrices and calculating the pairwise distance to create the recommender.


## Conclusion & Next Steps

Although the recommender gives back pretty good results, there is still a lot of work to be done. A limitation to the recommender is that it can only recommend games of similar genres for one of a kind games. For example, the recommendations for Overcooked!, a cooking games, were other similution games but none of which had anything to do with cooking. This is because Overcooked! happened to be the only cooking game in the data, so unable to find other cooking games, the recommender instead returns a list of games of the same genre. However for games with very popular genres, such as action and adventure, it returns a pretty accurate list of recommendations. For next steps, I would like to increase the number of games in my data adding all the games released prior to 2010 and well as making sure I have a more inclusive and even distribution of games to minimize the limitation. I would also like to include a filter function to my app to filter the results by various attributes.