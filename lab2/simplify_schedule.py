def simplify_schedule(schedule):
    if not schedule:
        return []

    sorted_schedule = sorted(schedule, key = lambda x: x[0])
    simplified_schedule = [sorted_schedule[0]]
    for interval in sorted_schedule[1:]:
        if interval[0] <= simplified_schedule[-1][1]:
            simplified_schedule[-1] = (simplified_schedule[-1][0], max(simplified_schedule[-1][1], interval[1]))
        else:
            simplified_schedule.append(interval)
    return simplified_schedule




input_schedule = [(0, 1), (1, 2), (3, 4), (10, 11), (5, 6)]
result = simplify_schedule(input_schedule)
print(result)


def calculate_working_hours(result):
    hour_list = []
    hours = 9
    minutes = 0
    for i in range(len(result)):
        first, second = result[i]
        for j in range(first):
            minutes += 30
            if minutes == 60:
                minutes = 0
                hours += 1
        first_hour = f"{hours:02} : {minutes:02}"
        hours, minutes = 9, 0
        for k in range(second):
            minutes+=30
            if minutes==60:
                minutes=0
                hours+=1

        second_hour = f"{hours:02} : {minutes:02}"
        hours, minutes = 9, 0
        time_tuple = (first_hour, second_hour)
        hour_list.append(time_tuple)
    return hour_list

print(calculate_working_hours(result))