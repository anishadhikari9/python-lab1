# Constants
CLEANING_RATE = 60
CAVITY_FILLING_RATE = 200
X_RAY_RATE = 100
TAX_RATE = 0.15

# Function to calculate the bill
def calculate_bill(name, cleaning_performed, cavity_filling_performed, x_ray_performed):
    # Calculate subtotal
    subtotal = 0
    if cleaning_performed == 'y':
        subtotal += CLEANING_RATE
    if cavity_filling_performed == 'y':
        subtotal += CAVITY_FILLING_RATE
    if x_ray_performed == 'y':
        subtotal += X_RAY_RATE
    
    # Calculate tax
    tax = subtotal * TAX_RATE
    
    # Calculate total
    total = subtotal + tax
    
    # Apply discount if applicable
    if total > 300:
        total *= 0.9
    elif total > 200:
        total *= 0.95
    
    # Print receipt
    print("Melanie Dental Clinic")
    print("----------------------")
    print("Receipt for patient name: {}".format(name))
    print("Subtotal: ${:.2f}".format(subtotal))
    print("Tax: ${:.2f}".format(tax))
    print("Total: ${:.2f}".format(total))

# Get inputs from user
name = input("Enter patient's name: ")
cleaning_performed = input("Was cleaning performed? (y/n): ")
cavity_filling_performed = input("Was cavity-filling performed? (y/n): ")
x_ray_performed = input("Was X-Ray performed? (y/n): ")

# Calculate bill and print receipt
calculate_bill(name, cleaning_performed, cavity_filling_performed, x_ray_performed)
