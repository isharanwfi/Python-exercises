def sum_of_list(numbers):
  
    total = 0
    for num in numbers:
        total += num
    return total

def main():

    test_list = [5, 12, 7, 21, 4]
    
   
    total_sum = sum_of_list(test_list)
    print(f"The test list is: {test_list}")
    print(f"The sum of all numbers in the list is: {total_sum}")

if __name__ == "__main__":
    main()
