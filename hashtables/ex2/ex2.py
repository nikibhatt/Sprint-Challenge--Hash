#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    cache = {}
    route = [None] * length
    for i in range(length):
        if tickets[i].source not in cache:
            cache[tickets[i].source] = tickets[i].destination

    route[0] = cache['NONE']
    for i in range(1, length):
        route[i] = cache[route[i-1]]

    return route


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")
#
# tickets = [ticket_1, ticket_2, ticket_3]
#
# #expected = ["PDX", "DCA", "NONE"]
# result = reconstruct_trip(tickets, 3)
# print(result)
