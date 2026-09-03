class ParkingSlot:
    def __init__(self,slot_number):
        self.slot_number=slot_number
        self.status="VACANT"
    def occupied(self):
        self.status="OCCUPIED"
        print(f"Slot {self.slot_number} marked as OCCUPIED.")

    def mark_vacant(self):
        self.status = "VACANT"
        print(f"Slot {self.slot_number} marked as VACANT.")

    def display_status(self):
        print(f"Slot {self.slot_number} is {self.status}.")

s1=ParkingSlot("A1")
s2=ParkingSlot("B2")

s1.occupied()
s2.mark_vacant()

s1.mark_vacant()
s1.display_status()