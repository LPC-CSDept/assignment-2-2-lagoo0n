def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    celcius = int(input("Enter the temperature in celcius: "))
    fahrenheit = (9/5)*celcius + 32
    print(f'fahrenheit: {fahrenheit}')
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
