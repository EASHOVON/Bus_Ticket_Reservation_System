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
    def reservaton(self):
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
