class MockChannel:
    def __init__(self, name, server, limit=None, topic=None, key=None):
        self.topic = topic
        self.limit = limit
        self.key = key
        self.usermodes = {}
        self.users = []
        self.modes = []
        self.name = name
        self.server = server

        self.joins = []
        self.parts = []
        self.msgs = []

    def join(self, user, key=None):
        self.joins.append({'user': user.nick, 'key': key})
        self.users.append(user)

    def part(self, user, msg=None):
        self.parts.append({'user': user.nick, 'msg': msg})
        self.users.remove(user)

    def msg(self, source, message):
        self.msgs.append({'source': source.nick, 'message': message})
