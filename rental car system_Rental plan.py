
class RentalPlan:
    def __init__(self, plan_id, plan_name, duration, rate):
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.duration = duration  # Duration in days
        self.rate = rate  # Rate per day
    
    def get_plan_details(self):
        return {
            "Plan ID": self.plan_id,
            "Plan Name": self.plan_name,
            "Duration": self.duration,
            "Rate": self.rate
        }
    
    def is_valid_plan(self):
        if self.duration <= 0 or self.rate <= 0:
            return False
        return True
    
    def calculate_discounted_rate(self, discount_percentage):
        if 0 < discount_percentage <= 100:
            return self.rate * (1 - discount_percentage / 100)
        else:
            raise ValueError("Invalid discount percentage. Must be between 0 and 100.")
        

rental_plan = RentalPlan(1, "Weekend Plan", 2, 50.0)
# Display details
print(rental_plan.get_plan_details())
