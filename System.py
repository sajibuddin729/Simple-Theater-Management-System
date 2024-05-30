import datetime
class Star_Cin:
    hall_list = []
    def entry_hall(self, hall_obj):
        self.hall_list.append(hall_obj)
        
class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cin().entry_hall(self)
        
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [['O' for _ in range(self._cols)] for _ in range(self._rows)]
        
    def book_seats(self, id, seat_list):
        if id not in self._seats:
            print("Invalid show ID")
            return
        for row, col in seat_list:
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                print("Invalid seat")
                return
            elif self._seats[id][row - 1][col - 1] == 'X':
                print(" Seat already booked, onno ta try koren .")
                return
            else:
                self._seats[id][row - 1][col - 1] = 'X'
        print(" booked successfully , chill koren .")
        
    def view_show_list(self):
        print("Shows running  Hall", self._hall_no)
        for show in self._show_list:
            print("ID:", show[0], "| Movie:", show[1], "| Time:", show[2])
            
    def view_available_seats(self, id):
        if id not in self._seats:
            print("show ID golo vul dicoo , Invalid ")
            return
        print("Availabl seats  show ID", id, " Hall", self._hall_no)
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[id][i][j] == 'O':
                    print("Row: ", i + 1, "---> Col: ", j + 1)


if __name__ == "__main__":
    hall_no = "1"
    rows = 7
    cols = 6
    hall1 = Hall(rows, cols, hall_no)
    hall1.entry_show("1", "Avenger", "12:00 PM")
    hall1.entry_show("2", "SpiderMan", "3:00 PM")
    hall1.entry_show("3", "Batman", "6:00 PM")
    hall1.entry_show("4", "sajibuddin", "10:00 AM")
    while True:
        print("\n1. View All Show Today\n2. View Available Seat\n3. Book Ticket\n4. Exit form here")
        choice = input("choice de 1 teke 4 er modde : ")
        if choice == '1':
            today = datetime.date.today()
            print("Today Date:", today)
            hall1.view_show_list()
        elif choice == '2':
            id = input("E show ID dis: ")
            hall1.view_available_seats(id)
        elif choice == '3':
            id = input("E show ID dis: ")
            seats = int(input("Enter koita  seat you lagbe : "))
            seat_list = []
            for _ in range(seats):
                row = int(input("E row no de : "))
                col = int(input("E column no de : "))
                seat_list.append((row, col))
            hall1.book_seats(id, seat_list)
        elif choice == '4':
            break
        else:
            print("Invalid choice")
