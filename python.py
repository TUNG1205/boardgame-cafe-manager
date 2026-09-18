
class Customer:
    """Represents a customer visiting the board game cafe."""

    def __init__(self, customer_id: str, name: str, membership_type: str, phone: str, budget: float, loyalty_points: int):
        self.customer_id = customer_id
        self.membership_type = membership_type
        self.name = name
        self.phone = phone
        self.budget = budget
        self.loyalty_points = loyalty_points
    def __str__(self) -> str:
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Membership: {self.membership_type}, Phone: {self.phone}, Budget: ${self.budget:.2f}, Loyalty Points: {self.loyalty_points}"

class Offering:
    """Represents the offerings available at the board game cafe."""
    def __init__(self, offering_id: str, name: str, price: float, category: str, subcategory: str, is_available: bool):
        self.offering_id = offering_id
        self.name = name
        self.price = price
        self.category = category
        self.subcategory = subcategory
        self.is_available = is_available
    def __str__(self) -> str:
        availability = "Available" if self.is_available else "Not Available"
        return f"Offering ID: {self.offering_id}, Name: {self.name}, Price: ${self.price:.2f}, Category: {self.category}, Subcategory: {self.subcategory}, Availability: {availability}"
class BoardGame(Offering):
    """Represents a board game available for rent at the cafe."""
    def __init__(self, offering_id: str, name: str, price: float, category: str, subcategory: str, min_players: int, max_players: int, complexity: float, is_available: bool):
        super().__init__(offering_id, name, price, category, subcategory, is_available)
        self.min_players = min_players
        self.max_players = max_players
        self.complexity = complexity
    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Min Players: {self.min_players}, Max Players: {self.max_players}, Complexity: {self.complexity}"
class Consumable(Offering):
    """Represents a consumable item available for purchase at the cafe."""
    def __init__(self, offering_id: str, name: str, price: float, category: str, subcategory: str, is_available: bool, prep_time: int, spice_level: str = None):
        super().__init__(offering_id, name, price, category, subcategory, is_available)
        self.prep_time = prep_time
        self.spice_level = spice_level
    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Prep Time: {self.prep_time} minutes"
# --- Quick Cafe Scenario Test ---
if __name__ == "__main__":
    # 1. Customer walks into the cafe
    guest = Customer(customer_id="CUST-402", name="Alex Mercer", membership_type="Regular", phone="0412-345-678", budget=50.00, loyalty_points=100)
    print(guest)
    offering1 = BoardGame(offering_id="BG-101", name="Catan", price=15.00, category="Board Game", subcategory="Strategy", is_available=True, min_players=3, max_players=4, complexity=2.5)
    offering2 = Consumable(offering_id="CS-201", name="Latte", price=4.50, category="Beverage", subcategory="Coffee", is_available=True, prep_time=5)
    print(offering1)
    print(offering2)
