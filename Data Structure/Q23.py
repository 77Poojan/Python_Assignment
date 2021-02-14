def islistempty(lst):
    if len(lst) != 0:
        print('List is not empty')
    else:
        print('List is empty')

sample_list = input('Enter string to add into list, if you do not want to add any elements just enter : ').split()
islistempty(sample_list)