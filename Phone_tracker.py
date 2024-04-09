import phonenumbers
from phonenumbers import geocoder

#prompt the user to enter phone number
phone_number_input=input("Enter the Phone Number:")
parsed_number=phonenumbers.parse(phone_number_input,"US")

#Get country and region information
print(phonenumbers.region_code_for_number(parsed_number))
print(geocoder.description_for_number(parsed_number,"en"))