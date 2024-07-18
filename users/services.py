import stripe
from forex_python.converter import CurrencyRates

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """Создание Stripe продукта."""

    product_name = (
        f"{instance.paid_course}" if instance.paid_course else f"{instance.paid_lesson}"
    )
    product = stripe.Product.create(name=f"{product_name}")
    return product


def convert_rub_to_usd(amount):
    """Конвертирование из рублей в доллары."""

    try:
        c = CurrencyRates()
        rate = c.get_rate("USD", "RUB")
    except:
        rate = 80
    return round(amount / rate, 2)


def create_stripe_price(amount, product):
    """Создание цены продукты в Stripe."""

    return stripe.Price.create(
        currency="usd",
        unit_amount=int(convert_rub_to_usd(amount) * 100),
        product=product.get("id"),
    )


def create_stripe_session(price):
    """Создание сессии в Stripe"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


def retrieve_sessions_statuses(session_id):
    """Получение статусов сессий в Stripe."""
    info = stripe.checkout.Session.retrieve(session_id)
    return info.get("payment_status")
