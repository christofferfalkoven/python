'''
Identifiers:
\d any number
\D anyything but a number
\s space
\S anything but space
\w any character
\W anything but a character
. any character, except for a newline
\b the whitespace around words
\. a period

Modifiers:
{1,3} We're expecting 1-3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of a string
^ Match the beginning of a string
| Match either or
[] Range or "variance"
{x} expecting "x" amount

White Space Characters
\n new line
\s space
\t tab
\e escape
\f form feed
\r return
'''
from datetime import *
import re


exampleString = '''Jessica is 15 years old, and Daniel is 27 years old. 
Edward is 97, and his grandfather, Oscar, is 102.'''
ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)
print(ages)
print(names)
ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1
print(ageDict)

exampleString2 = '''Read on port: \\?\hid#vid_1a79&pid_7410&mi_00#7&2b31b1d0&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}<STX>4R|1706|^^^Glucose|6.2|mmol/L^P||F/M0/T1||201811090310<CR><ETB>B8<CR><LF>'''
# mmol = re.findall(r'\d{1,3}\.\d{1}', exampleString2)
# print(mmol)
print("----------")
# print(mmol)

#
# f = (open("bmi.txt", "r"))

with open('bmi.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

# print(data)

mmol = re.findall(r'(?<=Glucose\|)\d{1,2}\.\d{1}', data)
dates = re.findall(r'(?<=\|\|)\d{12}', data)


blood_sugar_dict = {}
x = 0
for date in dates:
    blood_sugar_dict[date] = mmol[x]
    x+=1
print(blood_sugar_dict)

print(len(blood_sugar_dict))

