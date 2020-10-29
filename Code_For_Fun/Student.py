r_no, name, s1, s2, s3, s4, total, avg = ([] for i in range(8))
n = int(input("Enter the number of students: "))
for _ in range(n):
    reg_no = input()
    s_name = input()
    sub_1 = int(input())
    sub_2 = int(input())
    sub_3 = int(input())
    sub_4 = int(input())
    sum = sub_1 + sub_2 + sub_3 + sub_4
    average = sum/4
    r_no.append(reg_no)
    name.append(s_name)
    s1.append(sub_1)
    s2.append(sub_2)
    s3.append(sub_3)
    s4.append(sub_4)
    total.append(sum)
    avg.append(average)
for i in range(n):
    print(r_no[i])
    print(name[i])
    print(total[i])
    print(avg[i])
if sub_1 and sub_2 and sub_3 and sub_4 >= 50:
    print("Result : Pass")
else:
    print("Result : Fail")