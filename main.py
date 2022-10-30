class User:
    history = []
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.from_des = from_des
        self.to = to
        self.departure = departure
        self.seat = ["Empty" for i in range(20)]

class ShohagBusCompany:
    total_bus = 5
    total_bus_lst = []

    def install(self):
        bus_no = int(input("Enter Bus No : "))
        flag = 1
        for w in self.total_bus_lst:
            if bus_no == w['coach']:
                print("BUS already installed")
                flag = 0
                break
        if flag:
            bus_driver = input("Enter Bus Driver Name : ")
            bus_arrival = input("Enter Bus Arrival Time : ")
            bus_departure = input("Enter Bus Departure Time : ")
            bus_from = input("Enter Bus Start From : ")
            bus_to = input("Enter Bus To Destination : ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival,bus_departure, bus_from, bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print("\nBus successfully installed")

class Counter(ShohagBusCompany):
    user_lst = []
    def reservation(self):
        bus_no = int(input("Enter Bus No : "))
        for w in self.total_bus_lst:
            if bus_no == w['coach']:
                passenger = input("Enter YOur name : ")
                seat_no = int(input("Enter seat No : "))
                if seat_no > 20:
                    print("Seats only 20")
                elif w['seat'][seat_no] != "Empty":
                    print("Seat Already Booked")
                else:
                    w['seat'][seat_no-1] = passenger
            else:
                print("No bus available")

    def show(self):
        bus_no = int(input("Enter bus number : "))
        for w in self.total_bus_lst:
            if w['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus number : {bus_no} \t\tDriver : {w['driver']}")
                print(f"Arrival : {w['arrival']} \t\t\tDeparture Time : {w['departure']} \nFrom : \t{w['from_des']} \t\t\tTo : \t{w['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a += 1
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a += 1
                    print()
                print('*'*50)
            else:
                print("No bus available")
                break

    def get_users(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter your username : ")
        password = input("Enter your password : ")
        self.new_user = User(name, password)
        self.user_lst.append(vars(self.new_user))
        print("Account Created Successfully\n")

    def available_buses(self):
        if len(self.total_bus_lst) == 0:
            print("No Buses available\n")
        else:
            print('*'*50)
            for bus in self.total_bus_lst:
                print()
                print(f"{' '*10} {'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(f"Bus number : {bus['coach']} \tDriver : {bus['driver']}")
                print(
                    f"Arrival : {bus['arrival']} \tDeparture Time : {bus['departure']} \nFrom : \t{bus['from_des']} \t\tTo : \t{bus['to']}")
                print()
            print('*'*50)
