class Node(object):

    def __init__(self, movieID: str):
        """

        :param movieID: movieID of the movie the node corresponds to
        """
        self.movieID = movieID
        self.oet = {}
        self.iet = {}

    def getMovieID(self) -> str:
        """

        :return: movieID of the movie that corresponds to the Node
        """
        return self.movieID
