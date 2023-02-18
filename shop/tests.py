from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from decimal import Decimal
from django_countries import countries
from .models import Item, Order, OrderItem, Address, BillingAddress, Payment, Coupon

User = get_user_model()


class ItemModelTest(TestCase):

    CATEGORY_CHOICES = (
        ('S', 'Shirt'),
        ('SW', 'Sport wear'),
        ('OW', 'Outwear'),
    )

    LABEL_CHOICES = (
        ('P', 'primary'),
        ('S', 'secondary'),
        ('D', 'danger'),
    )

    def setUp(self):
        self.item = Item.objects.create(
            title='Test Item',
            price=10.0,
            discount_price=8.0,
            category='S',
            label='P',
            slug='test-item',
            description='This is a test item.',
            image='test_image.jpg'
        )

    def test_item_str_method(self):
        self.assertEqual(str(self.item), 'Test Item')

    def test_item_url_methods(self):
        self.assertEqual(self.item.get_url(), reverse(
            'shop:product', kwargs={'slug': 'test-item'}))
        self.assertEqual(self.item.get_add_to_cart_url(), reverse(
            'shop:add-to-cart', kwargs={'slug': 'test-item'}))
        self.assertEqual(self.item.get_remove_from_cart_url(), reverse(
            'shop:remove-from-cart', kwargs={'slug': 'test-item'}))

    def test_price_with_discount_property(self):
        self.assertEqual(self.item.price, 10.0)
        self.assertEqual(self.item.discount_price, 8.0)

    def test_item_category_and_label_choices(self):
        self.assertIn(('S', 'Shirt'), self.CATEGORY_CHOICES)
        self.assertIn(('SW', 'Sport wear'), self.CATEGORY_CHOICES)
        self.assertIn(('OW', 'Outwear'), self.CATEGORY_CHOICES)
        self.assertIn(('P', 'primary'), self.LABEL_CHOICES)
        self.assertIn(('S', 'secondary'), self.LABEL_CHOICES)
        self.assertIn(('D', 'danger'), self.LABEL_CHOICES)


class OrderModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

        self.item = Item.objects.create(
            title='Test Item',
            price=Decimal('10.00'),
            category='S',
            label='P',
            slug='test-item',
            description='Test Item description',
        )

        self.order_item = OrderItem.objects.create(
            user=self.user,
            item=self.item,
            quantity=2
        )

        self.order = Order.objects.create(
            user=self.user,
            ordered_date='2022-02-18',
        )

        self.order.items.add(self.order_item)

    def test_get_total(self):
        coupon = Coupon.objects.create(
            code='TESTCOUPON', amount=Decimal('5.00'))
        self.order.coupon = coupon
        self.order.save()

        expected_total = Decimal('15.00')
        self.assertEqual(self.order.get_total(), expected_total)


class OrderItemModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.item = Item.objects.create(
            title='Test Item', price='10.00', category='S', label='P', slug='test-item', description='Test Item Description', image='test.jpg')
        self.order_item = OrderItem.objects.create(
            user=self.user, item=self.item, quantity=2)

    def test_order_item_created(self):
        self.assertEqual(str(self.order_item), '2 of Test Item')

    def test_get_total_item_price(self):
        expected_total = Decimal('20.00')
        self.assertEqual(
            self.order_item.get_total_item_price(), expected_total)

    def test_get_total_discount_price(self):
        self.item.discount_price = 5.00
        self.item.save()
        expected_total = Decimal('10.00')
        self.assertEqual(
            self.order_item.get_total_discount_price(), expected_total)

    def test_get_amount_saved(self):
        self.item.discount_price = 5.00
        self.item.save()
        expected_saved = Decimal('10.00')
        self.assertEqual(self.order_item.get_amout_saved(), expected_saved)

    def test_get_final_price(self):
        self.item.discount_price = 5.00
        self.item.save()
        expected_price = Decimal('10.00')
        self.assertEqual(self.order_item.get_final_price(), expected_price)


class BillingAddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(
            username='testuser', password='testpass')

    def setUp(self):
        self.address = BillingAddress.objects.create(
            user=self.user,
            street_address='123 Main St',
            apartment_address='Apt 1',
            country='US',
            postcode='12345',
        )

    def test_str_representation(self):
        self.assertEqual(str(self.address), self.user.username)

    def test_fields(self):
        self.assertEqual(self.address.user, self.user)
        self.assertEqual(self.address.street_address, '123 Main St')
        self.assertEqual(self.address.apartment_address, 'Apt 1')
        self.assertEqual(self.address.country, 'US')
        self.assertEqual(self.address.postcode, '12345')

    def test_country_field_choices(self):
        self.assertEqual(len(self.address._meta.get_field(
            'country').choices), len(countries))


class AddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', password='testpass')
        cls.address = Address.objects.create(
            user=cls.user,
            street_address='123 Main St',
            apartment_address='Apt 4B',
            country='US',
            postcode='12345',
            address_type='S',
            default=True
        )

    def test_address_creation(self):
        self.assertEqual(self.address.user, self.user)
        self.assertEqual(self.address.street_address, '123 Main St')
        self.assertEqual(self.address.apartment_address, 'Apt 4B')
        self.assertEqual(self.address.country, 'US')
        self.assertEqual(self.address.postcode, '12345')
        self.assertEqual(self.address.address_type, 'S')
        self.assertTrue(self.address.default)


class PaymentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass')

        # Create a test payment
        cls.payment = Payment.objects.create(
            stripe_charge_id='ch_12345',
            user=cls.user,
            amount=10.50,
        )

    def test_payment_str(self):
        self.assertEqual(str(self.payment), self.user.username)

    def test_payment_has_timestamp(self):
        self.assertIsNotNone(self.payment.timestamp)
