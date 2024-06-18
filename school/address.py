
class Address:
    def __init__(self, area, city, state, pincode):
        self.area = area
        self.city = city
        self.state = state
        self.pincode = pincode
    
    def __str__(self):
        return f"{self.area} {self.city} {self.state} {self.pincode}"