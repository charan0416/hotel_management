from Manager import *

class OperationsManager:
    def __init__(self):
        self.manager = Manager()

    def print_menu(self):
        print("Program Options: ")
        options = [
            '1) add guest',
            '2) list guest',
            '3) available rooms',
            '4) remove guest',
            '5) price of room ',
            '6)please select the food from the menu '
        ]
        print('\n'.join(options))
        return self.get_choice(len(options))

    def get_choice(self, num_options):
        msg = f"Enter your choice from 1 to {num_options} \n"
        return input_is_valid(msg, 1, num_options)



    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.manager.add_guest()
            elif choice == 2:
                self.manager.list_guests()
            elif choice == 3:
                self.manager.check_rooms()
            elif choice == 4:
                self.manager.remove_guest()
            elif choice == 5:
                self.manager.price()
            elif choice == 6 :
                self.manager.food()
            else:
                print("Exiting the program.")
                break

ob = OperationsManager()
ob.run()