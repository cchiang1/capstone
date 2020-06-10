# Imports
import pandas as pd
import numpy as np 
import regex as re
from flask import Flask, Response, request, render_template

# Read in data
games = pd.read_csv('games_final.csv')
recommender = pd.read_csv('recommender.csv', index_col=0)

# Initialize Flask app
app = Flask('videoGameRecommender')

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Search page
@app.route('/search')
def search():
    user_input = request.args['game_name']

    # List of games with the input in its name
    similar_names = games[games['name'].str.contains(user_input, flags=re.IGNORECASE)].reset_index()
    games_list = [similar_names['name'][i] for i in range(similar_names.shape[0])]

    return render_template('search.html', games_list=games_list)

# Recommendations page
@app.route('/recommendations')
def most_similar():
    selected_game = request.args['game_name']

    # Transpose dataframe for easier selection
    games_t = games.set_index('name').T

    # Top 10 most similar games
    recommendations = recommender[selected_game].sort_values()[1:11]
    names = list(recommendations.index)
    recs_df = games_t[names]

    return render_template('recommendations.html', games=recs_df, names_list = names, selected_game=selected_game)

# Run app when python script is called
if __name__ == '__main__':
    app.run(debug=True)

# Take the result of user input and make it an arg in search/<game>
# Use game name as parameter maybe and also uriginal user input 

