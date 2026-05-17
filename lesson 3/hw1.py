present =int(input("Eneter the number of days present:"))
absent =int(input("Eneter the number of days absent:"))
health = str(input("Enter true(if unwell) or false(in not unwell):"))
num=present+absent


if (present / num) * 100 >= 75 and health == "false":
    print("Student eligible to sit in exam")
elif (present / num) * 100 >= 75 and health == "true":
    print("Student eligible to sit in exam (unwell)")
elif (present / num) * 100 < 75 and health == "false":
    print("Student not eligible to sit in exam")
elif (present / num) * 100 < 75 and health == "true":
    print("Student is eligible to sit in exam (unwell)")


