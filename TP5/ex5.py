import string
import random
def create_list(n):
    l = []
    for _ in range(n):
        l.append(''.join(random.choices(string.ascii_letters + string.digits, k=5)))
    return l

def display_vowel_strings(liste_chaines):
    vowels = 'aeiouAEIOU'
    print("Strings starting with a vowel:")
    for s in liste_chaines:
        if s[0] in vowels:
            print(s)
def count_a_occurrences(liste_chaines):
    print("Occurrences of 'a' in each string:")
    for s in liste_chaines:
        print(f"{s}: {s.count('a')}")

def create_sub_lists(liste_chaines):
    numbers = [s for s in liste_chaines if s.isdigit()]
    alphanumeric = [s for s in liste_chaines if s.isalnum() and not s.isalpha() and not s.isdigit()]
    string = [s for s in liste_chaines if s.isalpha()]
    return numbers, alphanumeric, string

n = random.randint(5, 20)
print(f"Generating {n} random strings.")
liste_chaines = create_list(n)
print("Generated List:", liste_chaines)
display_vowel_strings(liste_chaines)
count_a_occurrences(liste_chaines)
numbers, alphanumeric, string = create_sub_lists(liste_chaines)
print("Sub-list - Numbers:", numbers)
print("Sub-list - Alphanumeric:", alphanumeric)
print("Sub-list - Strings (only letters):", string)
