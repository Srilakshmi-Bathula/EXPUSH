import statistics

user_list =[2,2.3,5,4,9] 

def calculate_statistics(numbers):
    if len(numbers) == 0:
        print("The list is empty. Cannot perform calculations.")
        return

    average = sum(numbers) / len(numbers)
    print(f"Average of the numbers: {average}")

    mean = statistics.mean(numbers)
    print(f"Mean of the numbers: {mean}")

    median = statistics.median(numbers)
    print(f"Median of the numbers: {median}")

    std_dev = statistics.stdev(numbers)
    print(f"Standard Deviation of the numbers: {std_dev}")

calculate_statistics(user_list)
