from dice import Dice, DiceBag

def rolling_message():
    print('!!! Rolling Dice !!!')

def error_message():
    print('Unrecognized input. You can terminate the program with Ctrl+C.')

def line_break():
    print('-'*20)

def input_command():
    return str.lower(input('Choose operation: Roll, Max, Min, Show or New?')).strip()

def input_mode():
    return str.lower(input('Breakdown result by dice size [y/n]?')).strip()

def main():
    try:
        user_input = input('Enter a dice size or multiple sizes seperated by spaces:')
        user_dice = DiceBag(*user_input.split())
    except ValueError:
        print('Dice sizes must be integers seperated by spaces.')
        return
    user_command = input_command()
    if user_command not in ['show','new']:
        user_mode = input_mode()
    while user_command != 'new':
        if user_command == 'show':
            line_break()
            print(user_dice)
        elif user_mode == 'n':
            if user_command == 'roll':
                line_break()
                rolling_message()
                print(f"Roll result: {user_dice()}")
            elif user_command == 'max':
                line_break()
                rolling_message()
                print(f"Largest rolled value: {user_dice.max()}")
            elif user_command == 'min':
                line_break()
                rolling_message()
                print(f"Smallest rolled value: {user_dice.max()}")
            else:
                error_message()
        elif user_mode == 'y':
            if user_command == 'roll':
                line_break()
                rolling_message()
                print(f"Roll result by size: {user_dice(detailed=True)}")
            elif user_command == 'max':
                line_break()
                rolling_message()
                print(f"Largest value by size: {user_dice.sub_max()}")
            elif user_command == 'min':
                line_break()
                rolling_message()
                print(f"Smallest value by size: {user_dice.sub_max()}")
            else:
                error_message()
        else:
            error_message()
        line_break()
        user_command = input_command()
        if user_command not in ['show','new']:
            user_mode = input_mode()


if __name__=='__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            break
