"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    letter_sequence = ['A', 'B', 'C', 'D']
    for num in range(number):
        yield letter_sequence[num % 4]


letters = generate_seat_letters(4)
print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    seat_letters = generate_seat_letters(number)
    seat_row = 1

    for _ in range(number):
        if seat_row == 13:
            seat_row += 1
        seat_letter = next(seat_letters)
        yield f'{seat_row}{seat_letter}'

        if seat_letter == 'D':
            seat_row += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    passenger_seat = {}
    seats = generate_seats(len(passengers))

    for passenger in passengers:
        passenger_seat[passenger] = next(seats)
    return passenger_seat


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        code = seat + flight_id
        zeros = 12 - len(code)
        yield code + '0' * zeros
