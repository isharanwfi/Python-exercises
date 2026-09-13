def remove_uneven(numbers):
  
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def main():
 
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
   
    cut_down_list = remove_uneven(test_list)
    print(f"Original list: {test_list}")
    print(f"Cut-down list: {cut_down_list}")

if __name__ == "__main__":
    main()
