#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    trips = {}
    route = []

    if len(tickets) == 0:
        return None

    for t in tickets:
        trips[t.source] = t.destination

    airport = trips["NONE"]
    i = 0

    while i < length:
        route.append(airport)
        i += 1
        airport = trips[airport]

    return route
