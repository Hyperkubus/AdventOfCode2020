import re

def preparePassport(entry):
    data = entry.split(' ')
    keys = {}
    for date in data:
        values = date.split(':')
        keys[values[0]] = values[1]
    return keys

def isValid(data):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = 0
    for key in data:
        if not isFieldValid(key, data[key]):
            return False
        if key in req_fields:
            fields += 1
    if fields == 7:
        return True
    return Falsea

def isFieldValid(key, value):
    if key == 'byr':
        value = int(value)
        if value < 1920 or value > 2002:
            return False
        return True
    if key == 'iyr':
        value = int(value)
        if value < 2010 or value > 2020:
            return False
        return True
    if key == 'eyr':
        value = int(value)
        if value < 2020 or value > 2030:
            return False
        return True
    if key == 'hgt':
        if value[-2:] == "cm":
            if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                return False
            return True
        elif value[-2:] == "in":
            if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                return False
            return True
        else:
            return False
    if key == 'hcl':
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)
        if not match:
            return False
        return True
    if key == 'ecl':
        if value not in ('amb','blu','brn','gry','grn','hzl','oth'):
            return False
        return True
    if key == 'pid':
        match = re.search(r'^(?:[0-9]{9})$', value)
        if not match:
            return False
        return True
    if key == 'cid':
        return True
    return False


def passportInfo(data):
    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    print("=== PASSPORT ===")
    for field in fields:
        if field in data.keys():
            print(field, ": ", data[field])
        else:
            print(field, ": MISSING!")

def debug():
    print("test byr")
    print(not isFieldValid('byr',1919))
    print(isFieldValid('byr', 1920))
    print(isFieldValid('byr', 2002))
    print(not isFieldValid('byr', 2003))

    print("test hgt cm")
    print(not isFieldValid('hgt', "149cm"))
    print( isFieldValid('hgt', "150cm"))
    print( isFieldValid('hgt', "193cm"))
    print(not isFieldValid('hgt', "194cm"))

    print("test hgt in")
    print(not isFieldValid('hgt', "58in"))
    print(isFieldValid('hgt', "59in"))
    print(isFieldValid('hgt', "76in"))
    print(not isFieldValid('hgt', "77in"))

    print("test hgt oth")
    print(not isFieldValid('hgt', "12"))
    print(not isFieldValid('hgt', "194mm"))

    print("test hcl")
    print(not isFieldValid('hcl', "123456"))
    print(isFieldValid('hcl', "#123456"))
    print(isFieldValid('hcl', "#ffffff"))
    print(isFieldValid('hcl', "#FFFFFF"))
    print(not isFieldValid('hcl', "#FFFFFG"))

    print("test ecl")
    print(not isFieldValid('ecl', ''))
    print(isFieldValid('ecl', 'amb'))
    print(isFieldValid('ecl', 'blu'))
    print(isFieldValid('ecl', 'brn'))
    print(isFieldValid('ecl', 'gry'))
    print(isFieldValid('ecl', 'grn'))
    print(isFieldValid('ecl', 'hzl'))
    print(isFieldValid('ecl', 'oth'))
    print(not isFieldValid('ecl', 'red'))

    print("test pid")
    print(not isFieldValid('pid', '00000000'))
    print(isFieldValid('pid', '000000000'))
    print(isFieldValid('pid', '999999999'))
    print(not isFieldValid('pid', '1000000000'))
    print(not isFieldValid('pid', 'a000000000'))
    print(not isFieldValid('pid', '000000000o'))


def main():
    input = "delta.txt"
    lines = open("../../input/"+input,"r").readlines()
    entry = ""
    valid = 0
    total = 0
    for line in lines:
        if line[:-1] == "":
            total += 1
            data = preparePassport(entry.strip())
            passportInfo(data)
            if isValid(data):
                valid += 1
            entry = ""
        else:
            entry += line[:-1] + " "
    print(valid,'/',total)
main()
#debug()

# < 172