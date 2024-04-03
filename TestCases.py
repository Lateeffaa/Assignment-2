def main():
    def show_ticket_prices():
        print("Ticket Prices:")
        print("1 - Adult Ticket: AED 50")
        print("2 - Child Ticket: Free (with national ID)")
        print("3 - Senior Ticket: Free (with national ID)")
        print("4 - Student Ticket: Free (with national ID)")
        print("5 - Group Ticket: 50% discount")

    def guest_actions():
        print("Welcome, Guest!")
        ticket_choice = input("Would you like to purchase a ticket? (yes/no): ").lower()
        if ticket_choice in ["yes", "y"]:
            print("Here are the available ticket options:")
            show_ticket_prices()
            purchase_tickets(visitor)
        elif ticket_choice in ["no", "n"]:
            print("You chose not to purchase a ticket.")
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    def employee_actions():
        print("Welcome, Management Employee!")
        event_choice = input(print("List of Exhibitions:"))
        print("1 - Film Screening: The Jungle Book", "\n2 - Ramadan at the Museum", "\n3 - Family Spring Camp",
              "\n4 - From Kalila wa Dimna to La Fontaine",
              "\n5 - Modern Art Exhibition", "\nWhich event would you like to monitor? (Enter number): ")
        print(f"You chose to monitor the event: {event_choice}")

    def display_menu(role):
        print(f"Welcome! Are you a {role}?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(f"You selected {role}.")
            if role == "Guest":
                guest_actions()
            elif role == "Management employee":
                employee_actions()
        elif choice == "2":
            print(f"You're not a {role}.")
        else:
            print("Invalid choice. Please enter 1 or 2.")
            display_menu(role)

    def purchase_tickets(visitor):
        total_price = 0

        try:
            num_of_tickets = int(input("\nHow many tickets? "))

            for _ in range(num_of_tickets):
                while True:
                    category_input = input("Enter ticket category (Adult, Child, Student, Teacher, Senior): ").upper()
                    try:
                        category = VisitorsClassification[category_input]
                        break
                    except KeyError:
                        print(f"Enter a valid ticket category.")

                ticket = TicketandPricing(1, category)
                visitor.add_ticket(ticket)
                total_price += ticket.calculatePrice()

            if num_of_tickets > 5:
                discount = total_price * 0.5  # 50% discount on  total price
                total_price -= discount  # discount

            print(f"Total price for {num_of_tickets} tickets will be: {total_price:.2f} AED")

        except ValueError:
            print("Enter a valid number for the number of tickets.")

        except KeyboardInterrupt:
            print("\nPurchase interrupted. Exiting...")

        except Exception as e:
            print(f"An error occurred: {e}")

    # Main menu
    print("Welcome to the Museum!")
    while True:
        print("1. Guest")
        print("2. Management employee")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            visitor = Visitor("Lateefa", "Bani Malek", 19, "Female", "0580000000", "UAE", "V123456", "lateefa@example.com")
            display_menu("Guest")
        elif choice == "2":
            display_menu("Management employee")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


try:
    main()
except Exception as e:
    print("An error occurred:", e)
