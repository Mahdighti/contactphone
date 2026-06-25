class Phone():
    def __init__(self, name,phone,email):
        self.name  = name
        self.phone = phone
        self.email = email
    def search(self):
        return f"{self.name} | {self.phone} | {self.email}"
    def display(self):
        return f"{self.name} | {self.phone} | {self.email}"