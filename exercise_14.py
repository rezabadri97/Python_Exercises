def estimate_concrete(length,width,thickness):
    concrete_volume=length*width*thickness
    if concrete_volume>10:
        return f"volume: {concrete_volume} | High Volume"
    else:
        return f"volume: {concrete_volume} | Standard Volume"
volume=estimate_concrete(5,5,.5)
print(volume)