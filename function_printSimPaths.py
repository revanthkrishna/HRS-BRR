# def similar paths for a path
from Path import Path


def printSimPaths(p: Path):
    """

    :param p: The path for which similar paths are to be found out and displayed
    :return: Prints all similar paths for path p, including itself, along with similarity measure
    """

    # startnode of the path p
    startNode = p.startNode

    # this is the dict that contains the similar paths
    # keys are paths are values are similarity measures
    resultSet = {}

    # pointer is a var that is used to point a node
    # initialization(pointer) = startnode of path p
    pointer = startNode

    # add all similar paths wrt oet of the startnode to resultset
    for i in pointer.oet.values():
        for j in i:
            resultSet[j] = 1

    # add all similar paths wrt iet of the startnode to resultset
    for i in pointer.iet.values():
        for j in i:
            if j in resultSet:
                resultSet[j] += 1
            else:
                resultSet[j] = 1

    # outcome is a flag used to help with the loops
    outcome = False
    # this nested loop and the if stmt after the nested loop, sets the pointer to the next node in the path
    # if pointer currently points to the last node of the path, pointer is set to None
    for i in pointer.oet.keys():
        for j in pointer.oet[i]:
            if j == p:
                outcome = True
                pointer = i
                break
        if outcome == True:
            break
    if outcome == False:
        pointer = None

    # this while loop traverses the path node wise
    # currently pointer points to second Node of the path p
    while pointer != None:

        # add all similar paths wrt oet of the current node pointed by pointer to resultset
        for i in pointer.oet.values():
            for j in i:
                if j in resultSet:
                    resultSet[j] += 1
                else:
                    resultSet[j] = 1

        # add all similar paths wrt iet of the current node pointed by pointer to resultset
        for i in pointer.iet.values():
            for j in i:
                if j in resultSet:
                    resultSet[j] += 1
                else:
                    resultSet[j] = 1

        # outcome is a flag used to help with the loops
        outcome = False
        # this nested loop and the if stmt after the nested loop, sets the pointer to the next node in the path
        # if pointer currently points to the last node of the path, pointer is set to None
        for i in pointer.oet.keys():
            for j in pointer.oet[i]:
                if j == p:
                    outcome = True
                    pointer = i
                    break
            if outcome == True:
                break
        if outcome == False:
            pointer = None

    # this loop prints the resultset that contains the set of similar paths wrt to oet
    for i in resultSet:
        print(i.getPathID(), ':', resultSet[i])
