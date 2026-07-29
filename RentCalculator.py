# Input from the user

room_rent = int(input("Enter total room/flat rent: "))
total_students = int(input("Enter the number of students: "))
food_order = int(input("Enter the food order amount: "))
electric_uses = int(input("Enter the total electricity units used: "))
electric_per_unit_charge = int(input("Enter the electricity charge per unit: "))

# Calculate electricity bill
total_charge_electric = electric_uses * electric_per_unit_charge

# Calculate total spending
total_spend_amount = room_rent + food_order + total_charge_electric

# Calculate each student's share
individual_student = total_spend_amount / total_students

# Output
print("\n------ BILL SUMMARY ------")
print("Room Rent:", room_rent)
print("Food Order:", food_order)
print("Electricity Bill:", total_charge_electric)
print("Total Spend Amount:", total_spend_amount)
print("Each Student Pays:", individual_student)