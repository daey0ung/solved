GP_list = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
GP_sum=0.0
grade_sum = 0.0
for i in range(20):
    a = list(input().split())
    if a[2] != 'P':
        grade_sum += float(a[1])
        GP_sum += float(a[1]) * GP_list[a[2]]

print(GP_sum/grade_sum)