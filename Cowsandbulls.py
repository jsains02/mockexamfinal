import random

def convert(number):
    n = str(number)
    return [int(d) for d in str(n)]

def check_bulls(guess_covert,number_convert):
    result = 0
    for i in range(4):
        for j in range(4):
            if i == j:
                pass
            else:
                if guess_covert[i] == number_convert[j]:
                    result +=1
    return result

def check_cows(guess_covert,number_convert):
    result = 0
    for i in range(4):
        if guess_covert[i] == number_convert[i]:
            result += 1
    return result

def generate():
    return random.randint(999,9999)

def main():
    cow = 0
    number = generate()
    while cow != 4:
        print('welcome to the cows and bulls game!')
        print('Enter a number', end='')
        number_convert = convert(number)
        print(number_convert)
        guess = int(input())
        guess_covert = convert(guess)
        cow = check_cows(guess_covert,number_convert)
        bull = check_bulls(guess_covert,number_convert)
        print ('cow :',cow,' bull: ',bull)

if __name__ == "__main__":
    main()



