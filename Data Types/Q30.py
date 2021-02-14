d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def key_present(k):
    if k in d:
        print ("Key already exists.")
    else:
        print ("Key doesnot exist.")
            
check_key = int(input("Enter the key for checking: "))
key_present(check_key)