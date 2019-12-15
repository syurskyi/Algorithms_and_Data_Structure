import json
import operator
from json import JSONEncoder
from dataclasses import dataclass, field
from typing import Dict


def api(handler):
    def decorate(*args, **kwargs):
        instance = args[0]
        url = args[1]
        try:
            payload = json.loads(args[2])
        except IndexError:
            payload = None
        return json.dumps(handler(instance, url, payload), cls=UserEncoder)
    return decorate


@dataclass
class User:
    name: str
    owes: Dict = field(default_factory=dict)
    owed_by: Dict = field(default_factory=dict)
    balance: float = 0.0

    def owe(self, borrower, amount):
        lender = self

        lender.balance += amount
        borrower.balance -= amount

        User._handle_debt(lender.owes, lender.owed_by, borrower, amount)
        User._handle_debt(borrower.owed_by, borrower.owes, lender, amount)

    @staticmethod
    def _handle_debt(_from, _to, to_user, amount):
        debt = _from.pop(to_user.name, 0)
        debt -= amount
        if debt != 0:
            debt_obj = [_to, _from][debt > 0]
            debt_obj[to_user.name] = abs(-debt)

class UserEncoder(JSONEncoder):
    def default(self, obj: User):
        try:
            return {
                "name": obj.name,
                "owes": obj.owes,
                "owed_by": obj.owed_by,
                "balance": obj.balance
            }
        except AttributeError:
            return super().default(obj)


class RestAPI:
    def __init__(self, database=None):
        self.users = []
        for user_dict in database["users"]:
            self.users.append(User(**user_dict))

    @api
    def get(self, url, payload=None):
        return {
            "/users": self._get_users
        }.get(url)(payload)

    @api
    def post(self, url, payload=None):
        return {
            "/add": self._add_user,
            "/iou": self._add_iou
        }.get(url)(payload)

    def _add_user(self, payload):
        new_user = User(name=payload["user"])
        self.users.append(new_user)
        return new_user

    def _get_users(self, payload=None):
        users = self.users
        if payload is None:
            return {"users": users}
        return {"users": list(self._get_user_by_name(username) for username in payload["users"])}

    def _get_user_by_name(self, name):
        return list(filter(lambda u: u.name == name, self.users))[0]

    def _add_iou(self, payload):
        lender = self._get_user_by_name(payload["lender"])
        borrower = self._get_user_by_name(payload["borrower"])
        lender.owe(borrower, payload["amount"])
        return {"users": sorted([lender, borrower], key=lambda x: x.name)}
