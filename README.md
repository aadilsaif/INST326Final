# INST326Final



# Movie Recommender

## Description
Have you ever found yourself spending more time searching for a movie than actually watching one? It can be frustrating to sift through countless reviews and recommendations without finding something that truly matches your taste. That's where the Movie Recommender comes in.

The Movie Recommender is a project aimed at providing customized movie recommendations based on your watch history. By leveraging the popular social media app Letterboxd, this project offers tailored suggestions that align with your preferences.

In addition to personalized recommendations, the Movie Recommender also provides brief statistics and visualizations to help you better understand the types of movies that interest you. By analyzing your watch history and extracting relevant data, this project offers insights into your movie preferences.

## Features

### Movie Class
The Movie Class is a crucial component of the Movie Recommender. It stores all the necessary data types that a movie should have. By utilizing the movie's unique ID provided by the recommender process, the Movie Class accesses The Movie Database (TMDB) API to retrieve comprehensive information about the movie. This information forms the foundation for generating personalized recommendations.

### Web Scraper for Recommendations
Creating a custom recommendation algorithm can be complex, so the Movie Recommender incorporates an existing website's algorithm to generate recommendations. By utilizing the Selenium library, the project interacts with the website, inputting relevant information and scraping the recommendations that result from the algorithm. This approach ensures that the Movie Recommender provides reliable and diverse movie suggestions.

### Data Plots
To enhance the user experience and provide a better understanding of movie preferences, the Movie Recommender utilizes the Matplotlib library. This powerful tool enables the creation of visualizations and data plots based on the recommended movies. These visual representations allow users to explore patterns, genres, and other insightful information about their recommended movies.


### Usage
1. Set up your Letterboxd account and ensure you have a watch history.
2. Run the Movie Recommender script:
   ```
   python main.py [username]
   ```
3. Wait for the Movie Recommender to generate personalized recommendations and display data plots.
4. Explore the recommendations and enjoy watching your next movie!

