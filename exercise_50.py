def approve_rooms(pending,approved):
    while pending:
        current_room=pending.pop()
        print(f"{current_room}")
        approved.append(current_room)
pending_rooms = ['Lobby', 'Office 101', 'Restroom A']
approved_rooms = []
approve_rooms(pending_rooms[:],approved_rooms)
print(pending_rooms)
print(approved_rooms)