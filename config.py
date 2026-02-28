import csv
import io
from collections import Counter
from sqlalchemy import func
from .models import Booking


def booking_summary(db):
    bookings = Booking.query.filter(Booking.status != "cancelled").all()
    total_bookings = len(bookings)
    total_revenue = round(sum(b.total_amount for b in bookings), 2)
    cancelled = Booking.query.filter_by(status="cancelled").count()
    counter = Counter(b.room.category.name for b in bookings if b.room and b.room.category)
    top_category = counter.most_common(1)[0][0] if counter else "—"
    return {
        "total_bookings": total_bookings,
        "total_revenue": total_revenue,
        "cancelled": cancelled,
        "top_category": top_category,
    }


def bookings_csv(bookings):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Гость", "Email", "Номер", "Заезд", "Выезд", "Сумма", "Статус", "Оплата"])
    for b in bookings:
        writer.writerow([b.id, b.guest_name, b.guest_email, b.room.number, b.check_in, b.check_out, b.total_amount, b.status, b.payment_method])
    return output.getvalue().encode("utf-8-sig")
