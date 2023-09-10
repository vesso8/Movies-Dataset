import pandas as pd


movies_data = {
    'id': ['1', '2', '3', '4', '5', '6'],
    'title': ['First Movie', 'Second Movie', 'Third Movie', 'Fourth Movie',
    'Second Movie', 'First Movie'],
    'release_date': ['2000-01-01', '1999-01-01', '2001-01-01', '2000-01-01', '1998-01-01', '1999-01-01'],
    'genres': [
        '[{"id": 18, "name": "Drama"}]',
        '[{"id": 35, "name": "Comedy"}, {"id": 22, "name": "Action"}]',
        '[{"id": 62, "name": "Adventure"}, {"id": 77, "name": "Romance"}]',
        '[{"id": 55, "name": "Action"}]',
        '[{"id": 17, "name": "Comedy"}]',
        '[{"id": 41, "name": "Comedy"}]',
    ]
    }

ratings_data = {
    'movieId': ['1', '2', '3', '4', '5', '6'],
    'rating': [4.0, 5.0, 3.5, 4.0, 3.5, 4.0]
    }

metadata_df = pd.DataFrame(movies_data)
ratings_df = pd.DataFrame(ratings_data)

metadata_df.to_csv('movies_example.csv', index=False)
ratings_df.to_csv('ratings_example.csv', index=False)