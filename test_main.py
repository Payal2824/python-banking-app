import main


def test_create_account():
    main.accounts.clear()

    main.accounts["12345"] = {
        "name": "Payal",
        "pin": "1234",
        "balance": 0
    }

    assert "12345" in main.accounts
    assert main.accounts["12345"]["name"] == "Payal"
    assert main.accounts["12345"]["balance"] == 0
    
def test_deposit():
    main.accounts.clear()

    main.accounts["12345"] = {
        "name": "Payal",
        "pin": "1234",
        "balance": 1000
    }

    main.accounts["12345"]["balance"] += 500

    assert main.accounts["12345"]["balance"] == 1500
    
def test_withdraw():
    main.accounts.clear()

    main.accounts["12345"] = {
        "name": "Payal",
        "pin": "1234",
        "balance": 1000
    }

    main.accounts["12345"]["balance"] -= 300

    assert main.accounts["12345"]["balance"] == 700
    
def test_transfer():
    main.accounts.clear()

    main.accounts["12345"] = {
        "name": "Payal",
        "pin": "1234",
        "balance": 1000
    }

    main.accounts["67890"] = {
        "name": "Amit",
        "pin": "5678",
        "balance": 500
    }

    transfer_amount = 300

    main.accounts["12345"]["balance"] -= transfer_amount
    main.accounts["67890"]["balance"] += transfer_amount

    assert main.accounts["12345"]["balance"] == 700
    assert main.accounts["67890"]["balance"] == 800
    
def test_login():
    main.accounts.clear()

    main.accounts["12345"] = {
        "name": "Payal",
        "pin": "1234",
        "balance": 1000
    }

    assert main.accounts["12345"]["pin"] == "1234"
    assert "12345" in main.accounts