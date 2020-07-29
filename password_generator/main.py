from generator import Password


passwords = Password()
print("-------------------Welcome To The Password Generator!!!-------------------")
pw_num = int(input("How many passwords do you want? "))
list_pw_num = [i for i in range(pw_num)]  # Turns the int value from pw_num to list of individual numbers
equal_pw_length = input(
    "Do you want all your password of equal length?y/n").lower()
if equal_pw_length == "y":
    pw_length = int(input("Enter length of password: "))
    for digit in list_pw_num:
        print(passwords.ps_gen(pw_length))
else:
    for digit in list_pw_num:
        pw_length = int(input("Enter length of password: "))
        print(passwords.ps_gen(pw_length))
print("-------------------Thanks For Using The Password Generator!!!-------------------")
