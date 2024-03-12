class PaymentStatus:
    Paymant_Status = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('cancelled', 'Cancelled'),
    )


class OrderStatus:
    Order_STATUS = (
        ('Pending', 'Pending'),
        ('Fullfilled', 'Fullfilled'),
        ('Cancelled', 'Cancelled'),
    )
