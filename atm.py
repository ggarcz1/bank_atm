import tkinter as tk
import hashlib
# due to time constraints and my thirst to conquer connecting the apps, 
# most of this is from ChatGPT.  
# will revisit later
PIN_LENGTH = 4

def button_click(number):
    current_pin = pin_var.get()
    pin_var.set(current_pin + str(number))

def clear_pin():
    pin_var.set("")

# send to bank for procesing/comparison
# make a new class for this, aka utilize the router here
def verify_pin(hashed_pin):
    # TO-DO     
    return bool

def brute_force_test():
    # TO-DO     
    return bool

def enter_pin():
    # for testing, delete for production
    entered_pin = pin_var.get()
    print(entered_pin)

    global PIN_LENGTH
    if len(entered_pin) is not PIN_LENGTH:
        # create error here
        a = 5

    # hash here
    sha256_hash = hashlib.sha256()
    sha256_hash.update(entered_pin.encode('utf-8'))
    hashed_pin = sha256_hash.hexdigest()
    print(hashed_pin)
    verify_pin(hashed_pin)

# Create the main window
root = tk.Tk()
root.title("PIN Pad")

# Variable to store the PIN
pin_var = tk.StringVar()

# Entry widget to display the PIN
pin_entry = tk.Entry(root, textvariable=pin_var, show='*')
pin_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define buttons for digits
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0'
]

# Add digit buttons to the grid
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda digit=button: button_click(digit)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# Button to clear the PIN
tk.Button(root, text="Clear", padx=20, pady=20, command=clear_pin).grid(row=row_val, column=col_val)

# Button to enter the PIN
# how to clear the pin after hitting enter?
tk.Button(root, text="Enter", padx=20, pady=20, command=enter_pin).grid(row=row_val, column=col_val+1)


# on enter, run 

# Run the Tkinter main loop
root.mainloop()
