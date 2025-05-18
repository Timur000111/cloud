def get_numbers():
    user_input = input("Введите числа через запятую: ")
    numbers_list = []
    for number in user_input.split(','):
        cleaned_number = number.strip()
        numbers_list.append(int(cleaned_number))
    return numbers_list

def filter_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

def merge_sort(input_array):
    if len(input_array) <= 1:
        return input_array
    
    middle_index = len(input_array) // 2
    left_half = merge_sort(input_array[:middle_index])
    right_half = merge_sort(input_array[middle_index:])
    
    return merge_sorted_halves(left_half, right_half)

def merge_sorted_halves(left_half, right_half):
    merged_result = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged_result.append(left_half[left_index])
            left_index += 1
        else:
            merged_result.append(right_half[right_index])
            right_index += 1
    
    while left_index < len(left_half):
        merged_result.append(left_half[left_index])
        left_index += 1
        
    while right_index < len(right_half):
        merged_result.append(right_half[right_index])
        right_index += 1
    
    return merged_result

def main():
    original_numbers = get_numbers()
    even_numbers = filter_even_numbers(original_numbers)
    sorted_numbers = merge_sort(original_numbers.copy())
    
    print(f"Четные числа: {even_numbers}")
    print(f"Максимальное число: {max(original_numbers)}")
    print(f"Минимальное число: {min(original_numbers)}")
    print(f"Отсортированный список: {sorted_numbers}")

if __name__ == "__main__":
    main()