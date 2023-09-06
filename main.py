pay_of-worker:
hours_to_work =8
rate_per_hour =5
if(hours_to_work <=8)
    pay="hours_worked" * rate_per_hour
    normal_pay= hours_to_work * rate_per_hour
else(over_time_pay):
    over_time_rate =6#ghc
    over_time_hours =4
    over_time_pay = hours_to_work - over_time_hour
    total_pay =normal_pay + over_time_pay
    return
     usage
    day= (input(prompt a user to input the number of days worked))
if( days<=14)
    print(total_pay)


















