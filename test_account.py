from account import Account
import pytest

def test_init():
    j = Account("John")
    assert j.getname() == "John"
    assert j.getbalance() == 0


def test_deposit():
    f = account("Fred")
    f.deposit(100)
    assert f.getbalance() == 100


def test_withdraw():
    a = account("Alex")
    a.deposit(10000)
    a.withdraw(2567)
    assert a.getbalance() == 7433



