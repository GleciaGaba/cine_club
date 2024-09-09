import os

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")
print(DATA_FILE)


class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        pass

    def _write_movies(self):
        pass


if __name__ == '__main__':
    m = Movie("harry potter")
    print(m)
