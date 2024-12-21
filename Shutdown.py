def shutdown():
    shut=input("Are all apps closed")
    if shut == "Yes" or shut == "yes":
        print("Your program can be shutdowned")
    else:
        print("Sorry")
print(shutdown())