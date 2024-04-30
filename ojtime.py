import os

def parse_time_input(input_str):
    hours, minutes = map(int, input_str.split())
    return hours + minutes / 60

def convert_decimal_to_time(decimal_hours):
    hours = int(decimal_hours)
    minutes = int((decimal_hours - hours) * 60)
    return f"{hours} Hours and {minutes} Minutes"

def calculate_hours():
    morning_in = parse_time_input(input("Morning in (HH MM): "))
    morning_out = parse_time_input(input("Morning out (HH MM): "))
    afternoon_in = parse_time_input(input("Afternoon in (HH MM): "))
    afternoon_out = parse_time_input(input("Afternoon out (HH MM): "))

    if afternoon_out < afternoon_in:
        afternoon_out += 24  # Add a day's worth of hours

    total_hours = (morning_out - morning_in) + (afternoon_out - afternoon_in)
    return total_hours

def save_to_file(day_count, total_hours, total_accumulated_hours):
    with open("work_hours.txt", "a") as file:
        file.write(f"Day {day_count}: Total hours: {total_hours:.2f} Accumulated hours: {total_accumulated_hours:.2f}\n")

def load_from_file():
    try:
        with open("work_hours.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                parts = last_line.split(":")
                day_count = int(parts[0].split()[1])
                total_accumulated_hours = float(parts[-1])
            else:
                day_count = 1
                total_accumulated_hours = 0
            return day_count, total_accumulated_hours
    except FileNotFoundError:
        return 1, 0


def main():
    while True:
        choice = input("Press 1 to start a new calculation, 2 to load from file, or any other key to exit: ")
        
        if choice == '1':
            day_count = 1
            total_accumulated_hours = 0
        elif choice == '2':
            day_count, total_accumulated_hours = load_from_file()
            day_count += 1
        else:
            break

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            print(f"Day {day_count}")

            total_hours = calculate_hours()
            total_accumulated_hours += total_hours

            print(f"Total hours for that day: {total_hours:.2f} ({convert_decimal_to_time(total_hours)})")
            print(f"Total accumulated hours: {total_accumulated_hours:.2f} ({convert_decimal_to_time(total_accumulated_hours)})")

            save_to_file(day_count, total_hours, total_accumulated_hours)

            choice = input("Press 1 to do another calculation, or any other key to exit: ")
            if choice != '1':
                break
            day_count += 1

if __name__ == "__main__":
    main()
