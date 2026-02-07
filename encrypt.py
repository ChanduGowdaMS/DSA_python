class InstagramAccount:
    account_name = ""

    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self._private_reels:
                print("Reel: ", reel)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print("reel:", reel)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            print("Access Denied! Incorrect password")
            return None

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Incorrect old password. Password not updated")

obj=InstagramAccount("chandu", 1234)
obj.add_private_reel("Bikes")
obj.add_private_reel("dances")
obj.display_private_reels("asd")
obj.add_archived_reel("karate")
obj.add_archived_reel("cars")
obj.display_archived_reels(1234)
obj.set_password(1234, 5678)