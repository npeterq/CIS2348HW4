"Peter Nguyen"
"6/27/2021"
"CIS2348"
"1860823"
"12.7 CIS 2348 LAB: Fat-burning heart rate"


def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    heart_rate = 220 - age
    heart_rate *= 0.7
    return heart_rate

if __name__ == "__main__":
    try:  # try block of statements
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print("Fat burning rate for a ", age, " year-old:", end="")
        print(rate, "bpm")
    except ValueError as e:
        print(e)
        print('Could not calculate heart rate info.\n')