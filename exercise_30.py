def generate_room_tag(room_name,department,level="Ground_Floor"):
    tag_info=(f"Tag info---> Room:{room_name} | Dept: {department} | Level: {level}")
    return tag_info
first=generate_room_tag("Lobby","Public")
print(first)
second=generate_room_tag("Manager Ofiice","Management","Level 3")
print(second)