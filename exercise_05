# Format: "STATUS:TaskName:DurationInDays"
schedule_data = ["URGENT:Foundations:20", "Normal:Walls:15", "URGENT:Structural_Columns:10", "Normal:Windows:5", "URGENT:Roofing:8"]
urgent_tasks = []
total_days = 0
for item in schedule_data:
    new_data=item.split(":")
    duration=int(new_data[2])
    status=new_data[0]
    task_name=new_data[1]
    if status== "URGENT":
        urgent_tasks.append(task_name)
    total_days+=duration
print(f"Urgent Tasks: {urgent_tasks}")
print(f"Total Duration: {total_days} Days")
if total_days>40:
    print("Project Delay Risk: High")
else:
    print("Schedule is Optimized")