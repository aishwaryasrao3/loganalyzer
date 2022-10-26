import re

def find_pattern_and_count(name):
    file = open('log.txt')
    data = file.read()
    file.close()

    listdata = data.split()
    new_list = []
    for i in listdata:
        j = re.sub(r"[^a-zA-Z0-9 ]", "", i)
        new_list.append(j)
    matches = [item for item in new_list if name in item]
    mylist = list(dict.fromkeys(matches))
    print(mylist)
    for i in mylist:
        count = new_list.count(i)
        print("count of "+i)
        print(count)

def find_users():
    list_of_users = []
    with open('log.txt') as fd:

        for line in fd:
            # assuming that each time a session is killed a file is released from a user for count of locked files
            match = re.search(r'Killing session for user (\S+)', line)

            if match:
                user = match.group(1)
                list_of_users.append(user)

        userlist = list(dict.fromkeys(list_of_users))
        for i in userlist:
            print(i + " " + str(list_of_users.count(i)))

if __name__ == '__main__':

    print("users and locked file count")
    find_users()
    print('--------')
    print('list of warnings and count')
    find_pattern_and_count('Warning')
    print('-------')
    print('list of errors and count')
    find_pattern_and_count('Error')
