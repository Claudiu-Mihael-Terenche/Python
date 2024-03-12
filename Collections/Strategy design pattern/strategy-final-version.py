from dataclasses import dataclass, field
import string
import random
from typing import List, Callable


def generate_id(length: int = 8) -> str:
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class SupportTicket:
    id: str = field(init=False, default_factory=generate_id)
    customer: str
    issue: str


SupportTickets = List[SupportTicket]

Ordering = Callable[[SupportTickets], SupportTickets]


def fifo_ordering(list1: SupportTickets) -> SupportTickets:
    return list1.copy()


def filo_ordering(list1: SupportTickets) -> SupportTickets:
    list_copy = list1.copy()
    list_copy.reverse()
    return list_copy


def random_ordering(list1: SupportTickets) -> SupportTickets:
    list_copy = list1.copy()
    random.shuffle(list_copy)
    return list_copy


def blackhole_ordering(_: SupportTickets) -> SupportTickets:
    return []


def process_ticket(ticket: SupportTicket):
    print('==================================')
    print(f'Processing ticket id: {ticket.id}')
    print(f'Customer: {ticket.customer}')
    print(f'Issue: {ticket.issue}')
    print('==================================')


class CustomerSupport:

    def __init__(self):
        self.tickets: SupportTickets = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, ordering: Ordering):
        # create the ordered list
        ticket_list = ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print('There are no tickets to process. Well done!')
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            process_ticket(ticket)


def main() -> None:
    # create the application
    app = CustomerSupport()

    # register a few tickets
    app.create_ticket('Ralph the Raccoon', 'Cannot open the garbage bin! What is the password?')
    app.create_ticket('Brad the Bear',
                      'This sandwich has mustard. Do you have some without mustard, by any chance?')
    app.create_ticket(
        'Sonny the Skunk', 'I need a new deodorant')

    # process the tickets (random_ordering, fifo_ordering, filo_ordering)
    app.process_tickets(random_ordering)


if __name__ == '__main__':
    main()
