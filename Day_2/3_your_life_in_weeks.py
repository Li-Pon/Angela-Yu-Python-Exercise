age = int(input("What is your current age? "))
left_time = 60-age

left_day = left_time * 365
left_week = left_time * 52
left_month = left_time * 12

print(
    f"You have {left_day} days, {left_week} weeks and {left_month} months left")
