from Node import Node


class Path(object):

    def __init__(self, startNode: Node, pathID: str):
        """

        :param startNode: Node object that is the startnode of the path
        :param pathID: pathID of the path
        """
        self.startNode = startNode
        self.pathID = pathID

    def getPathID(self) -> str:
        """

        :return: pathID of the path
        """
        return self.pathID
