import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("--------------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("--------------------")

user1 = UserInfo()
user2 = UserInfo()

user1.set_info("kim", "010-1234-1111")
user2.set_info("park", "010-9876-5555")

user1.print_info()
user2.print_info()
