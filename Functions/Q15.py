nums = [1, 2, 3, 4, "ram", 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nNumbers from the list:")
nums = list(filter(lambda x: type(x)==int, nums))
print(nums)