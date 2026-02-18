def create_lable(element_id,prefix="BIM-"):
    result=prefix+str(element_id)
    return result
E_I_01=5050
E_I_02=7070
final_result=create_lable(E_I_01)
print(f"Lable: {final_result}")
final_result=create_lable(E_I_02,"Revit-")
print(f"Lable: {final_result}")