from unittest import TestCase
import pandas as pd
import os
from task.movies_analyzer import MovieAnalyzer

class TestMovieAnalyzer(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.movies_data_path = 'resources/movies_example.csv'
        cls.ratings_data_path = 'resources/ratings_example.csv'

        cls.movie_analyzer = MovieAnalyzer(cls.movies_data_path, cls.ratings_data_path)

    def test_unique_movies_count(self):
        result = self.movie_analyzer.unique_movies_count()
        self.assertEqual(result, 4)

    def test_average_rating(self):
        result = self.movie_analyzer.average_rating()
        self.assertAlmostEqual(result, 4.0)

    def test_top_rated_movies(self):
        top_rated = self.movie_analyzer.top_rated_movies(n=2)
        self.assertEqual(len(top_rated), 2)

    def test_movies_per_year(self):
        result = self.movie_analyzer.movies_per_year()
        expected_result = pd.DataFrame({
            'Year': [2000, 1999, 2001, 1998],
            'Count': [2, 2, 1, 1]
        })
        expected_result['Year'] = expected_result['Year'].astype('int32')
        pd.testing.assert_frame_equal(result, expected_result)

    def test_movies_per_genre(self):
        result = self.movie_analyzer.movies_per_genre()

        expected_result = pd.DataFrame({
            'Genre': ['Comedy', 'Action', 'Drama', 'Adventure', 'Romance'],
            'Count': [3, 2, 1, 1, 1]
        })
        pd.testing.assert_frame_equal(result, expected_result)

    def test_save_to_json(self):
        output_json_path = 'resources/example_output.json'
        self.movie_analyzer.save_results_to_json(output_json_path)

        self.assertTrue(os.path.exists(output_json_path))




