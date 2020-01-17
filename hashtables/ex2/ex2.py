#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        Ticket = {
            'source': self.source,
            'destination': self.destination
        }
        return str(Ticket)
    


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    print(hashtable)
    print(tickets)

    """
    YOUR CODE HERE
    """

    return route


tickets = [
  Ticket("PIT","ORD"),
  Ticket("XNA","CID"),
  Ticket("SFO","BHM"),
  Ticket("FLG","XNA"),
  Ticket("NONE", "LAX"),
  Ticket("LAX","SFO"),
  Ticket("CID","SLC"),
  Ticket("ORD","NONE"),
  Ticket("SLC","PIT"),
  Ticket("BHM","FLG")
]

reconstruct_trip(tickets,len(tickets))
