try:
    numofitems = int(input("Enter the number of items:"))
    total_price = 200 * numofitems
    avg_price = numofitems/total_price
    print("Avg Price : ", avg_price)
except ZeroDivisionError: # One try can have more than 1 except block.
    print("You cannot enter 0 as number of items.")
finally:
    print("I am in a finally block, i always execute.")

print("End of code.")