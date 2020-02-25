""" Module to direct through Twitter API """
import twitter

def read_list(lst:list):
    '''
    Returns list's element if found,
    otherwise returns error
    '''
    print('This is a list!')
    ind = int(input(f"Please choose list's element index from 0 to {len(lst) - 1} included: "))
    try:
        return lst[ind]
    except:
        return 'Wrong Index entered'


def read_dict(dct: dict):
    '''
    Returns dictionary key value if found,
    otherwise returns error
    '''
    print('This is a dictionary!')
    dict_keys = dct.keys()
    print(dict_keys)
    key = input('Please enter the desired key from above: ')
    try:
        return dct[key]
    except:
        return 'Wrong key entered'


if __name__ == '__main__':
    user = input("Please enter user's name: ")
    try:
        file = twitter.get_friends_locations('https://api.twitter.com/1.1/friends/list.json', user)
    except:
        print('Wrong user entered.')

    while True:
        if type(file) == dict:
            new_file = read_dict(file)
        elif type(file) == list:
            if len(file) > 1:
                new_file = read_list(file)
            else:
                print(file)
                break
        else:
            print(file)
            break
        file = new_file
