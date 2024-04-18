def is_valid_input(input_str):
    valid_chars = {'a', 't', 'g', 'c'}
    return all(char in valid_chars for char in input_str)

def input_string():
    while True:
        user_input = input("Enter a valid ADN string (formed exclusively from 'a', 't', 'g', or 'c'): ")
        if is_valid_input(user_input):
            return user_input
        else:
            print("Invalid input. Please enter a valid ADN string.")

def input_sequence():
    while True:
        user_input = input("Enter a valid ADN sequence (formed exclusively from 'a', 't', 'g', or 'c'): ")
        if is_valid_input(user_input):
            return user_input
        else:
            print("Invalid input. Please enter a valid ADN sequence.")

def proportion(string, sequence):
    count = string.count(sequence)
    total_length = len(string)
    if total_length == 0:
        return 0
    else:
        return count / total_length * 100

adn_string = input_string()
adn_sequence = input_sequence()
prop = proportion(adn_string, adn_sequence)
print(f"There is {prop:.2f}% of \"{adn_sequence}\" in your string.")




