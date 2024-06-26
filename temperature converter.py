def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def convert(choice: int) -> None:

    match choice:
        case 1:
            celsius: float = float(input('Enter the value of celsius : '))
            print(f'{celsius}C in fahrenheit is : {celsius_to_fahrenheit(celsius):.2f}C')
        case 2:
            fahrenheit: float = float(input('Enter the value of fahrenheit : '))
            print(f'{fahrenheit}F in celsius is : {fahrenheit_to_celsius(fahrenheit):.2f}F')
        case 3:
            exit(0)
        case _:
            print('Entered invalid value')


def main() -> None:

    print('!!!TEMPERATURE CONVERTER!!!')

    while True:
        print('1. Celsius to Fahrenheit.')
        print('2. Fahrenheit to Celsius.')
        print('3. quit')

        choice: int = int(input('Enter your choice : '))
        convert(choice)


if __name__ == '__main__':
    main()

