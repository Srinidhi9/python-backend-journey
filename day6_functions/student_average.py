def calculate_average(marks):
    return sum(marks) / len(marks)


marks = []

for i in range(3):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

average = calculate_average(marks)

print("Average:", average)