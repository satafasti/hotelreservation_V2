# def update_room_type(room_types, type_id, new_description=None, new_max_guests=None):
#     rt = next((r for r in room_types if r.type_id == type_id), None)
#     if rt:
#         if new_description: rt.description = new_description
#         if new_max_guests: rt.max_guests = new_max_guests
#         print(f"Zimmertyp {type_id} aktualisiert: {rt.description}, max Gäste: {rt.max_guests}")
#     else:
#         print("Zimmertyp nicht gefunden.")
