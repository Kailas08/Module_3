calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    string1 = string.upper()
    string2 = string.lower()
    return (len(string), string1, string2)
def is_contains(str_, lst_):
    count_calls()
    lst1 = [i.upper() for i in lst_ ]
    if str_.upper() in lst1:
        return True
    else:
        return False

print(string_info('Piramida'))
print(string_info('Saturn'))
print(string_info('Telphon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)