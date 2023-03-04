from brownie import SimpleStorage, accounts, config


def read_contract():
    # get the recent transaction address
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
