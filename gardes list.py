# START
grades: list[int] = []
garde: int = int(input("enter a garde: "))
while garde != -999:
    grades.append(garde)
    garde: int = int(input("enter a garde: "))
else:
    print(f"{garde} is not valid")

if len(grades) > 0:
    print(max(grades))
    print(min(grades))
    print((sum(grades)) / (len(grades)))
# END