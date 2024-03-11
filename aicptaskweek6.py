class WildlifePark:
    def __init__(self):
        self.one_day_prices = {
            "Adult": 20.00,
            "Child": 12.00,
            "Senior": 16.00,
            "Family": 60.00,
            "Group": 15.00
        }

        self.two_day_prices = {
            "Adult": 30.00,
            "Child": 18.00,
            "Senior": 24.00,
            "Family": 90.00,
            "Group": 22.50
        }

        self.extra_attraction_prices = {
            "Lion Feeding": 2.50,
            "Penguin Feeding": 2.00,
            "Evening Barbecue": 5.00
        }

        self.available_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        self.bookings = {}
        self.booking_counter = 1

    def display_ticket_options(self):
        print("Ticket Options for One-Day Tickets:")
        self._display_ticket_prices(self.one_day_prices)

        print("\nTicket Options for Two-Day Tickets:")
        self._display_ticket_prices(self.two_day_prices)

        print("\nExtra Attractions:")
        for attraction, price in self.extra_attraction_prices.items():
            print(f"{attraction}: ${price:.2f}")

        print("\nAvailable Days for Booking:")
        print(", ".join(self.available_days))

    def _display_ticket_prices(self, prices):
        for ticket_type, price in prices.items():
            print(f"{ticket_type}: ${price:.2f}")

    def process_booking(self, day, ticket_type, num_tickets, attraction_list=None):
        total_cost = 0

        if ticket_type not in self.one_day_prices and ticket_type not in self.two_day_prices:
            print("Invalid ticket type.")
            return

        if day not in self.available_days:
            print("Invalid booking day.")
            return

        if ticket_type in self.one_day_prices:
            total_cost += self.one_day_prices[ticket_type]
        else:
            total_cost += self.two_day_prices[ticket_type]

        total_cost *= num_tickets

        if attraction_list:
            for attraction in attraction_list:
                if attraction in self.extra_attraction_prices:
                    total_cost += self.extra_attraction_prices[attraction] * num_tickets
                else:
                    print(f"Invalid attraction: {attraction}")

        booking_number = self.booking_counter
        self.booking_counter += 1
        self.bookings[booking_number] = {"Day": day, "Ticket Type": ticket_type, "Num Tickets": num_tickets, "Total Cost": total_cost}

        print(f"Booking details:")
        print(f"Booking Number: {booking_number}")
        print(f"Day: {day}")
        print(f"Ticket Type: {ticket_type}")
        print(f"Number of Tickets: {num_tickets}")
        print(f"Total Cost: ${total_cost:.2f}")

    def check_best_value(self, num_tickets, ticket_type):
        if ticket_type == "Group" and num_tickets >= 6:
            return True
        elif ticket_type == "Family" and num_tickets >= 3:
            return True
        else:
            return False


def main():
    park = WildlifePark()

    # Task 1: Display ticket options, attractions, and available days
    park.display_ticket_options()

    # Task 2: Process a booking
    day = input("\nEnter booking day: ")
    ticket_type = input("Enter ticket type: ")
    num_tickets = int(input("Enter number of tickets: "))
    attractions = input("Enter attractions (comma-separated): ").split(",") if input("Are there any attractions? (y/n): ").lower() == 'y' else None

    park.process_booking(day, ticket_type, num_tickets, attractions)

    # Task 3: Check best value
    if not park.check_best_value(num_tickets, ticket_type):
        print("Consider alternative booking options for better value.")


if __name__ == "__main__":
    main()
