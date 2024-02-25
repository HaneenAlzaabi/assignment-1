from datetime import datetime


class Passenger:
    def __init__(self, passengerID, name, contactNumber):
        self.passengerID = passengerID
        self.name = name
        self.contactNumber = contactNumber

    def updateInfo(self, newContactNumber):
        self.contactNumber = newContactNumber


class Flight:
    def __init__(self, flightNumber, destination, departureDateTime, gateNumber, boardingTime, terminalNumber,
                 seatNumber):
        self.flightNumber = flightNumber
        self.destination = destination
        self.departureDateTime = departureDateTime
        self.gateNumber = gateNumber
        self.boardingTime = boardingTime
        self.terminalNumber = terminalNumber
        self.seatNumber = seatNumber

    def getDetails(self):
        departure_date = self.departureDateTime.strftime('%Y-%m-%d')
        departure_time = self.departureDateTime.strftime('%H:%M')

        return f"Flight {self.flightNumber} to {self.destination} departs on {departure_date} at {departure_time} from Gate {self.gateNumber}"

    def checkAvailability(self):
        # Checking seat availability
        return True


class Booking:
    def __init__(self, bookingID, passenger, flight):
        self.bookingID = bookingID
        self.passenger = passenger
        self.flight = flight

    def generateBoardingPass(self):
        # Generating a boarding pass
        return BoardingPass(self.bookingID, self.passenger, self.flight)


class BoardingPass:
    def __init__(self, passID, passenger, flight):
        self.passID = passID
        self.passenger = passenger
        self.flight = flight

    def displayBoardingInfo(self):
        return f"Boarding Pass ID: {self.passID}\n" \
               f"Passenger: {self.passenger.name}\n" \
               f"{self.flight.getDetails()}\n" \
               f"Boarding Time: {self.flight.boardingTime}\n" \
               f"Terminal Number: {self.flight.terminalNumber}\n" \
               f"Seat Number: {self.flight.seatNumber}"


# Create instances
passenger1 = Passenger("P001", "Amr Sallam", "123-456-7890")
flight1 = Flight("F001", "UAE", datetime(2023, 3, 3, 12, 30), "G02", "12:00", "Terminal 1", "First Class - 08A")

# Make a booking
booking1 = Booking("B001", passenger1, flight1)

# Generate BoardingPass
boarding_pass1 = booking1.generateBoardingPass()

# Display BoardingPass details
print(boarding_pass1.displayBoardingInfo())
