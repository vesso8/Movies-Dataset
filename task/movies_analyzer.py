import pandas as pd
import logging
import json

# Create a logger
logging.basicConfig(filename="../movie_dataset.log", level=logging.INFO)


class MovieAnalyzer:
    def __init__(self, metadata_path, ratings_path):
        self.metadata_path = metadata_path
        self.ratings_path = ratings_path
        self.load_datasets()

    # Load the movies metadata and ratings datasets
    def load_datasets(self):
        try:
            self.metadata = pd.read_csv(self.metadata_path, low_memory=False)
            self.ratings = pd.read_csv(self.ratings_path)
            logging.info("Datasets loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading datasets: {str(e)}")
            raise

    # Get the unique movies in the dataset
    def unique_movies_count(self):
        unique_movies = self.metadata["title"].nunique()
        return unique_movies

    # Get the average rating of all movies
    def average_rating(self):
        average_rating = self.ratings["rating"].mean()
        return average_rating

    # Return the top 5 highest rated movies
    def top_rated_movies(self, n=5):
        self.metadata["id"] = self.metadata["id"].astype(str)
        self.ratings["movieId"] = self.ratings["movieId"].astype(str)

        # Merge based on 'id' in metadata and 'movieId' in ratings
        merged_data = self.metadata.merge(
            self.ratings, left_on="id", right_on="movieId", how="inner"
        )
        top_rated_movies = (
            merged_data.groupby("title")["rating"]
            .mean()
            .sort_values(ascending=False)
            .head(n)
        )

        # Convert the result to a DataFrame
        top_rated_movies_df = top_rated_movies.reset_index()
        return top_rated_movies_df

    # Return the number of movies released each year
    def movies_per_year(self):
        # Extract the year from the 'release_year' column
        self.metadata["release_date"] = pd.to_datetime(
            self.metadata["release_date"], errors="coerce"
        )
        self.metadata["Year"] = (
            self.metadata["release_date"].dt.year.fillna(0).astype(int)
        )  # Replace NaN with 0, then convert to int

        # Count movies per year and create a DataFrame
        movies_per_year = self.metadata["Year"].value_counts().reset_index()
        movies_per_year.columns = ["Year", "Count"]
        return movies_per_year

    # Return the number of movies in each genre
    def movies_per_genre(self):
        # Extract and count genre names
        genre_counts = self.metadata["genres"].apply(
            lambda x: [genre["name"] for genre in json.loads(x.replace("'", '"'))]
        )
        genre_counts = genre_counts.explode().value_counts().reset_index()
        genre_counts.columns = ["Genre", "Count"]
        return genre_counts

    # Save the dataset to a JSON file
    def save_to_json(self, output_path):
        try:
            self.metadata.to_json(output_path, orient="records", lines=True)
            logging.info(f"Dataset saved to {output_path}.")
        except Exception as e:
            logging.error(f"Error saving dataset to JSON: {str(e)}")
            raise


if __name__ == "__main__":
    metadata_path = "../datasets/movies_metadata.csv"
    ratings_path = "../datasets/ratings.csv"
    output_json_path = "../movies_dataset.json"

    movie_analyzer = MovieAnalyzer(metadata_path, ratings_path)

    print(f"Number of unique movies: {movie_analyzer.unique_movies_count()}")
    print(f"Average rating of all movies: {movie_analyzer.average_rating():.2f}")
    print("Top 5 highest rated movies:")
    print(movie_analyzer.top_rated_movies())
    print("Number of movies released each year:")
    print(movie_analyzer.movies_per_year())
    print("Number of movies in each genre:")
    print(movie_analyzer.movies_per_genre())

    movie_analyzer.save_to_json(output_json_path)
