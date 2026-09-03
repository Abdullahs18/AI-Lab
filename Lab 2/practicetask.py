class ParkingSlot:
    def __init__(self, slot_number, status="VACANT"):
        self.slot_number = slot_number
        self.status = status

    def mark_occupied(self):
        self.status = "OCCUPIED"

    def mark_vacant(self):
        self.status = "VACANT"

    def display_status(self):
        print(f"Slot {self.slot_number}: {self.status}")


# Creating multiple parking slots
slot_101 = ParkingSlot(101, "VACANT")
slot_102 = ParkingSlot(102, "OCCUPIED")
slot_103 = ParkingSlot(103, "VACANT")
slot_104 = ParkingSlot(104, "VACANT")

# Updating slot states
slot_101.mark_occupied()
slot_103.mark_occupied()
slot_104.mark_vacant()

# Displaying current status of each slot
for slot in [slot_101, slot_102, slot_103, slot_104]:
    slot.display_status()
