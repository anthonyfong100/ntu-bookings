def is_valid_court_num(court_number: int) -> bool:
    # valid court numbers are 1...6
    return 1 <= court_number <= 6


def is_valid_time(start_time: int) -> bool:
    # valid start time are 8...21 , 24 hour clock
    return 8 <= start_time <= 21
