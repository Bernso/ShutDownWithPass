import os
from time import sleep

# To make sure we are in the correct directory
workingdir = os.getcwd()
os.chdir(workingdir)
def clear():
    os.system('cls')
clear()
tries_path = 'PasswordForShutdown/tries.txt'
if os.path.exists(tries_path): 
    tries_file = open(tries_path, 'r')
    tries = tries_file.read()
    if tries == '0':
        print("You do not have permission to run this file.")
        quit()
    tries_file.close()



def run_check(password):
    if len(password) < 10:
        clear()
        print("\n* Password must contain 10 characters")
        return False
        
    elif len(password) > 16:
        clear()
        print("\n* Password must contain less than 16 characters")
        return False
        
    elif password.lower() == password:
        clear()
        print("\n* Password must contain capital letters")
        return False
        
    elif password.upper() == password:
        clear()
        print("\n* Password must contain lowercase letters")
        return False
        
    elif password.isalpha():
        clear()
        print("\n* Password must contain integers")
        return False
    
    elif " " in password:
        clear()
        print("\n* No spaces allowed")
        return False
        
    else:
        return True


def shutdown():
    user_input = input("Would you like to shut down your computer? (y/n)\n")    
    if user_input.lower() == "n":
        print("\nOk")
        print("👋")
        quit()
    
    # Waits 10 seconds
    for i in range(1, 11):
        os.system('cls')
        print(f"Shutting down in {10-i}...")
        sleep(1)
    # Shuts down the computer
    try:
        print("👋")
        os.system("shutdown /s")
    except OSError as e:
        print(f"Error while shutting down:\n{e}")

def does_user_know_password(password):
    check_for_extra = open('PasswordForShutdown/tries.txt', 'r')
    tries = check_for_extra.read()
    number_tries = int(tries)
    if number_tries not in [1, 2, 3]:
        print("Resetting number of tries...")
        tries_to_change = open('PasswordForShutdown/tries.txt', 'w')
        tries_to_change.write('3')
    password_file = open('PasswordForShutdown/pass.txt', 'r')
    contents = password_file.read()
    password_file.close()
    check_for_extra.close()
    
        
    if password == contents:
        shutdown()
            
    else:
        number_tries = number_tries - 1
        change_tries = open('PasswordForShutdown/tries.txt', 'w')
        writeable_tries = str(number_tries)
        change_tries.write(writeable_tries)
        print(f"You got the pasword wrong. {number_tries} tries remaining")
        
    


def create_password():
    print("\nPlease create a password with the following rules: \n- Minimum 10 Characters \n- Maximum 16 Characters \n- Must have capitals and lowercase \n- Must contain integers \n- NO SPACES \n")
    password = input("Enter your password: \n")
    
    # If the password is returned false this will run
    if not run_check(password):
        print("Password does not meet the requirements")
        # Re-runs the code 
        create_password()
    
    # Only happens when the password is valid
    else:
        try:
            # Create the file if it hasn't been created before
            password_file = open(password_path, "w")
            # Write the password to the file
            password_file.write(password)
            # Close the password file to prevent data loss
            password_file.close()
            print("Password has been saved successfully.\n")
            shutdown()

        # Incase there is an error while saving the password; it will print out the error
        except Exception as e:
            print(f"An error occurred while saving the password:\n{e}")
        
    
    
# Creates a new folder to store the password for the shutdown (if it doesn't already exist)
pass_folder = "PasswordForShutdown"
if os.path.exists(pass_folder):
    print("'PasswordForShutdown' folder already exists")
else:
    print("Making 'PasswordForShutdown' folder...")
    os.makedirs(pass_folder)
    print("'PasswordForShutdown' folder created")




tries_path = 'PasswordForShutdown/tries.txt'
if not os.path.exists(tries_path):
    tries_file = open(tries_path, 'w')
    tries_file.write("3")
    tries_file.close()   
else:
    print("'tries' file already exists\n")

# Checks to see if a password has already been created
password_path = 'PasswordForShutdown/pass.txt'
if os.path.exists(password_path):
    # Checks if the previous password was valid
    previous_pass = open(password_path, 'r')
    contents = previous_pass.read()
    previous_pass.close()
    run_check(contents)
    
    if run_check(contents):
        print("Valid password found.")
        password_temp = input("Enter the password: ")
        does_user_know_password(password_temp)
    else:
        print("Previous file had an invalid password.")
        print("Removing invalid password...")
        # Deletes the invalid password
        os.remove(password_path)
        # Creates a new file for the to be new password
        new_file = open(password_path, 'w')
        new_file.close()
        print("Old password was removed.")
        # Creates a password
        create_password()
    
else:
    print("No password has been found\nCreating a new password...")
    create_password()



        