// 

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