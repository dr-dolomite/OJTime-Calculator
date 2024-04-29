import os

def parse_time_input(input_str):
    hours, minutes = map(int, input_str.split())
    return hours + minutes / 60

def convert_decimal_to_time(decimal_hours):
    hours = int(decimal_hours)
    minutes = int((decimal_hours - hours) * 60)
    return f"{hours:02}:{minutes:02}"

def calculate_hours():
    morning_in = parse_time_input(input("Morning in (HH MM): "))
    morning_out = parse_time_input(input("Morning out (HH MM): "))
    afternoon_in = parse_time_input(input("Afternoon in (HH MM): "))
    afternoon_out = parse_time_input(input("Afternoon out (HH MM): "))

    total_hours = (morning_out - morning_in) + (afternoon_out - afternoon_in)
    return total_hours

def main():
    total_accumulated_hours = 0
    day_count = 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
        print(f"Day {day_count}")

        total_hours = calculate_hours()
        total_accumulated_hours += total_hours

        print(f"Total hours for that day: {total_hours:.2f} ({convert_decimal_to_time(total_hours)})")
        print(f"Total accumulated hours: {total_accumulated_hours:.2f} ({convert_decimal_to_time(total_accumulated_hours)})")

        choice = input("Press 1 to do another calculation, or any other key to exit: ")
        if choice != '1':
            break
        day_count += 1

if __name__ == "__main__":
    main()
