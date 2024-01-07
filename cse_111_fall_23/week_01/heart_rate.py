# 01 Checkpoint: Review Python

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
user_age = int(input("Please enter your age: "))
range_ = 220 - user_age
range_65 = range_ * .65 
range_85 = range_ * .85 

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {range_65:.0f} and {range_85:.0f}")