class Process:
    def __init__(self, p_id, process_name, start_time, priority):
        self.p_id = p_id
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"{self.p_id} {self.process_name} {self.start_time} {self.priority}"

def sort_processes(processes, sort_param):
    if sort_param == 1:
        return sorted(processes, key=lambda x: x.p_id)
    elif sort_param == 2:
        return sorted(processes, key=lambda x: x.start_time)
    elif sort_param == 3:
        return sorted(processes, key=lambda x: x.priority)

def print_flight_table(processes):
    for process in processes:
        print(process)

if __name__ == "__main__":
    processes = [
        Process("P1", " VSCode ", 100, " MID "),
        Process("P23", " Eclipse ", 234, " MID "),
        Process("P93", " Chrome ", 189, " High "),
        Process("P42", " JDK ", 9, " High "),
        Process("P9", " CMD ", 7, " High "),
        Process("P87", " NotePad ", 23, " Low 1"),
    ]

    while True:
        print("\nOptions:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 4:
            break

        if choice in [1, 2, 3]:
            sorted_processes = sort_processes(processes, choice)
            print("\nFlight Table:")
            print_flight_table(sorted_processes)
        else:
            print("Invalid choice. Please select a valid option.")
