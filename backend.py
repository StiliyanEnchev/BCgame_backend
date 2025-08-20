import random

rules = """
Hello and welcome to this mini game of Bulls and Cows!

Rules:
- There is a 4-digit safe code to crack in the range of 1-9.
- Only digits are allowed, no repetitions.
- You have as many attempts as you like.
- After each guess, you'll see:
    • Bulls: numbers guessed correctly in the correct place
    • Cows: numbers guessed correctly but in the wrong place
Good luck!
    """

print(rules)

nums = random.sample(range(1, 9), 4)
nums_str = ''.join(str(n) for n in nums)
result = '____'
B = 0
K = 0

while B != 4:
    B = 0
    K = 0
    users_input = input('Provide the number: ')
    if not users_input.isnumeric() or len(users_input) != 4:
        print('Your number can be four digits only. Please try again.');
    elif len(set(users_input)) != 4:
        print('Please enter four different digits as each number can be used only once.');
    elif "0" in users_input:
        print('Please enter a number in the range 1-9.');
    else:
        for i in range(len(nums_str)):
            if nums_str[i] == users_input[i]:
                B += 1
            elif nums_str[i] in users_input:
                K += 1

        print(f"You have K:{K} and B:{B}")

print('Congratulations! You won')

