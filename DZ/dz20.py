import re

user_number = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'

number_phone = r'\+*\d{1}\s*\(?\d{3}\)?\s*\d{3}[\s-]*\d{2}[\s-]*\d{2}'

print(re.findall(number_phone, user_number))