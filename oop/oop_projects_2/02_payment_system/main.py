from payment import CardPayment, CashPayment, OnlinePayment

payments = [
    CardPayment(250),
    CashPayment(100),
    OnlinePayment(500),
]

for payment in payments:
    payment.pay()
