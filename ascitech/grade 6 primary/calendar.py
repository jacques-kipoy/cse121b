import pywhatkit , calendar

day = int(input("enter the day as a number "))
month = int(input("enter the month as a number "))
year = int(input("enter the year "))
#print(calendar.prcal(year))
print( ) #blank space
#print(calendar.month(year, month))





# Replace the phone numbers and message with your own
phone_numbers = ['+243824775135', '+243840575592']
message = 'Hello from Python!'

# Send the message to the phone numbers at 9:30 AM
pywhatkit.sendwhatmsg_to_group('Group Name', phone_numbers, 9, 30, message)

