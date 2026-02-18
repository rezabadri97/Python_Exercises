def is_safe_height(height):
    if 2.5<=height<=5:
        return True
    else:
        return False
H1=6.5
H2=2.1
H3=3.2
result=is_safe_height(H1)
print(f"Is Safe Height: {result}")
result=is_safe_height(H2)
print(f"Is Safe Height: {result}")
result=is_safe_height(H3)
print(f"Is Safe Height: {result}")