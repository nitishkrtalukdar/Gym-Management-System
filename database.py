class Database:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def get_members(self):
        return self.members