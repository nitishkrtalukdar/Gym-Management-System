class GymLogic:
    def __init__(self):
        self.plan_prices = {
            "Zumba": 500,
            "Cardio": 500,
            "Weightlifting": 1000,
            "All of Them": 1500,
        }
        self.members = []

    def get_plans(self):
        return list(self.plan_prices.keys())

    def calculate_price(self, plan):
        return self.plan_prices.get(plan, 0)

    def add_member(self, name, phone, gender, plan):
        price = self.calculate_price(plan)
        self.members.append((name, phone, gender, plan, price))

    def get_members(self):
        return self.members