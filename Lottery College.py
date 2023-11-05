import random  # Imports the 'random' module

winning_numbers = []  # Initialise a list to store all the winning numbers (stays consistent)
bonus_number = random.randint(1, 59)  # Picks a random number between 1 and 59 (inclusive) for the bonus number

# Generates 6 numbers in the range of 1 and 59 (inclusive) and checks if it has been used before for the winning numbers and adds it to the list
for i in range(6):
    while True:
        n = random.randint(1, 59) 
        if n not in winning_numbers and n is not bonus_number:
            winning_numbers.append(n)
            break

winning_numbers = sorted(winning_numbers)  # Sort the winning numbers from smallest to largest and prints them in a readable format
print("Lottery Numbers Are:", str(winning_numbers)[1:-1])
print("Bonus Number Is:", str(bonus_number))

# Dictionary of the winning conditions' counter
winnings = {
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '5b': 0,
    '6': 0
}

# Generates 1 million tickets to simulate probability for each winning condition
for i in range(1_000_000):
    # Generate one ticket
    ticket_numbers = []
    for j in range(6):
        while True:
            n = random.randint(1, 59)
            if n not in ticket_numbers:  # Store random numbers that hasn't been stored prior in the list until the for loop has looped 6 times
                ticket_numbers.append(n)
                break
    dups = []
    for n in ticket_numbers:
        if n in winning_numbers:  # Store the numbers that matched between the ticket numbers and the winning numbers into the dups list
            dups.append(n)
    bonus_match = False  # Initialise the bonus match boolean variable
    dupsLength = len(dups)  # dupsLength is the amount of matches
    if dupsLength == 5:
        for n in ticket_numbers:
            if n is bonus_number:
                bonus_match = True  # If there is a number that matches with the bonus number and has 5 matches from the winning numbers, set bonus match to true
                break
    if dupsLength >= 2:
        key = str(dupsLength)  # If there are two or more matches, use the dupsLength to assign to the correct key in the winnings dictionary
        if bonus_match:
            key = '5b'  # if bonus match is true, set the key to 5b
        winnings[key] += 1  # Add one to the value of the specificied winning condition

print('Winnings:')
for key in winnings:
    print('\t' + key + ':', winnings[key])  # print the winnings of all the 1,000,000 tickets


results = []  # Store the ticket number to caclulate the average later on
for k in range(10):  # Will exit out of the loop once 10 tickets have 6 matches
    ticket_num = 1  # Start with ticket #1
    while True:
        dups = []  # Stores the matching numbers
        ticket_numbers = [] # Stores the ticket numbers
        for j in range(6):  # Loops 6 times to get 6 numbers of the guessed numbers between 1 and 59
            while True:
                n = random.randint(1, 59)
                if n not in ticket_numbers:  # If the guess is already guessed, pick a new number
                    ticket_numbers.append(n)  # If it is, store the guess to the ticket numbers list
                    if n in winning_numbers:
                        dups.append(n)  # If the ticket number is one of the winning numbers, add that to the dups list
                    break
        dupsLength = len(dups)
        if dupsLength == 6:  # If there are 6 matches, break out of the while loop
            break
        ticket_num += 1  # Increment the ticket number by one if the winning condition is not met

    print('Got 6 at ticket #' + str(ticket_num))  # Print the ticket number and append it to the results list
    results.append(ticket_num)

average = 0
for num in results:
    average += num
average /= len(results)  # Calculates the average using all the values stored in the results list by adding them all up and dividing by the amount of numbers, in this case, 10

print('Average number for winning:', average)  # Prints out the average of the ticket numbers to show the probability of having 6 matching numbers
