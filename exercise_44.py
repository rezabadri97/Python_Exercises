import clr
try :
    clr.AddReference('RevitAPIUI')
    data_r={"Selection" : "Select elemnts by mouse click" , "TaskDialog" : "Display popup messages to the user"}
    for key, value in data_r.items():
        print(f"The {key} is used to {value}")
except Exception as e:
    print(f"An error occurred while loading RevitAPIUI:{e}")