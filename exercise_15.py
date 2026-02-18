def calculate_beam_weight(length,beam_type):
    if beam_type=="IPE180":
        unit_weight=18.8
    elif beam_type=="IPE200":
            unit_weight=22.4
    else:
            unit_weight=0
    total_weight=length*unit_weight
    return round(total_weight,2)
length=6
beam_type="IPE200"
final_result=calculate_beam_weight(length,beam_type)
print(f"Beam: {beam_type} | Length: {length} | Total Weight: {final_result} ")