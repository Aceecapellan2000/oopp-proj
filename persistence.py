import shelve


class Points:
    def __init__(self, name, member_points, voucher_redemption, login_points, points_summary):
        self.name = name
        self.member_points = member_points
        self.login_points = login_points
        self.voucher_redemption = voucher_redemption
        self.points_summary = points_summary

    def get_articlepoints(self):
        self.member_points += 200

    def get_loginpoints(self):
        self.login_points += 150

    def points_summary(self):
        self.points_summary = self.login_points + self.member_points
        return self.points_summary

    def voucher(self):
        self.member_points -= 10

members = shelve.open('member')


def add_member(member):
    members[member.name] = member


def add_login_points(name):
    if name in members:
        m = members[name]
        m.login_points += 100
        members[name] = m


def add_member_points(name):
    if name in members:
        m = members[name]
        m.member_points += 200
        members[name] = m


def get_member(name):
    if name in members:
        return members.get(name)
    return None
