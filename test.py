import random

MAX_LINES = 4
MAX_BET = 100
MIN_BET = 1

ROWS = 4
COLS = 4

symbol_count = {"A":2, "B":4, "C":6,"D":8,"E":10,"F":12}

symbol_value = {"A":6, "B":5, "C":4,"D":3,"E":2,"F":1}


def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        
    return winnings,winning_lines
            

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(column) -1:
                print(column[row],end = " | ")
            else:
                print(column[row],end = "")

        print()


def deposit():
    while True:
        amount = input("What would u like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. ")
        else:
            print("Please enter a valid number ")

    return amount  


def get_num_of_lines():
    while True:
        num_of_lines = input("How many lines would you like to print (1-" + str(MAX_LINES) +")? ")
        if num_of_lines.isdigit():
            num_of_lines = int(num_of_lines)
            if 1 <= num_of_lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be greater than 0. ")
        else:
            print("Please enter a valid number ")

    return num_of_lines


def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
        else:
            print("Please enter a valid number ")

    return bet


def spin(balance):
    num_of_lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*num_of_lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {num_of_lines} lines. Total bet is equal to ${total_bet}")
    slot = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slot)
    winnings,winning_lines = check_winnings(slot,num_of_lines,bet,symbol_value)
    print(f"You won ${winnings}." )
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == "q" or "Q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
