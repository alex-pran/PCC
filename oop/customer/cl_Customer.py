

class Customer:
    def __init__(self,name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        print('Calculating cost')
        self.membership_type = new_membership

    def read_customer():
        print('Reading customer from DB')

customer = [Customer('Caleb', 'Gold'),
            Customer('Brad', 'Bronze')]

print(cutomer[1].membership_type)
customer[1].update_membership('Gold')
print(customer[1].membership_type)

Customer.read_customer()


# c = Customer("Caleb", 'Gold')
# print(c.name, c.membership_type)
#
# c2 = Customer("Brad", "Bronze")
# print(c2.name, c2.membership_type)

