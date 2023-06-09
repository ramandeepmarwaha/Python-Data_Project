import csv
import faker
from faker import Faker

fake = Faker()
data = []
input_number = input("Please input number of rows that are required to be created?\n")

i=0
while i < int(float((input_number))) :
    data.append([fake.name(),fake.address(), fake.email(),fake.credit_card_number(),fake.date_of_birth(),fake.phone_number()])
    i += 1
    
   
#print(data)
header = ['Name', 'Address', 'EmailID', 'Credit Card Nuymber', 'Date Of birth', 'Phone number']

file_n = input("Please name the csv file \n")


filename = file_n+".csv"

with open(filename, 'w',newline='' ) as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print(f"data saved to {filename} succefully")