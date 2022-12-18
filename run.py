from dice import Dice, DiceBag

def rolling_message():
    print('!!!Rolling your Dice!!!')

def error_message():
    print('Unrecognized input. You can terminate the program with Ctrl+C.')

def line_break():
    print('-'*10)

def main():
    user_input = input('Enter a list of dice sizes seperated by spaces:')
    user_dice = DiceBag(*user_input.split())
    user_command = str.lower(input('Roll, Max, Min, or New?'))
    user_mode = str.lower(input('Breakdown by dice size [y/n]?'))
    while user_command != 'new':
        if user_mode == 'n':
            if user_command == 'roll':
                rolling_message()
                print(f"Roll result: {user_dice()}")
            elif user_command == 'max':
                rolling_message()
                print(f"Largest rolled value: {user_dice.max()}")
            elif user_command == 'min':
                rolling_message()
                print(f"Smallest rolled value: {user_dice.max()}")
            else:
                error_message()
        elif user_mode == 'y':
            if user_command == 'roll':
                rolling_message()
                print(f"Roll result: {user_dice(detailed=True)}")
            elif user_command == 'max':
                rolling_message()
                print(f"Largest value by size: {user_dice.sub_max()}")
            elif user_command == 'min':
                rolling_message()
                print(f"Smallest value by size: {user_dice.sub_max()}")
            else:
                error_message()
        else:
            error_message()
        line_break()
        user_command = str.lower(input('Roll, Max, Min, or New?'))
        user_mode = str.lower(input('Breakdown by dice size [y/n]?'))


if __name__=='__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            break
