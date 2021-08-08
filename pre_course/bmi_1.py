def ask_for_float_input(input_name):
    count = 0
    while True:
        try:
            message = "What's your {} (m)? " if not count else "The {} was invalid. Please enter a new one. "
            value = float(input(message.format(input_name)))
            break
        except ValueError:
            count += 1
            continue
    return value


def ask_personal_information():
    name = input("What's your name? ")
    age = input("What's your age? ")
    while not age.isdigit():
        age = input("The age was invalid. Please enter a new one. ")

    height = ask_for_float_input('height')
    weight = ask_for_float_input('weight')

    return name, age, height, weight


name, age, height, weight = ask_personal_information()
print(f"Person #1 - Name: {name}, Age: {age}, BMI: ???")

name, age, height, weight = ask_personal_information()
print(f"Person #2 - Name: {name}, Age: {age}, BMI: ???")
