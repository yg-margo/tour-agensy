import pytest
from django.core.exceptions import ValidationError
from tours.models import Tour, Reservation, Review

@pytest.mark.django_db
def test_tour_creation():
    tour = Tour.objects.create(
        name="Test Tour",
        agency="Test Agency",
        description="This is a test tour.",
        period="2023-10-01 to 2023-10-10",
        payment_conditions="Full payment required."
    )
    assert tour.name == "Test Tour"
    assert str(tour) == "Test Tour"

@pytest.mark.django_db
def test_reservation_creation(user):
    tour = Tour.objects.create(
        name="Test Tour",
        agency="Test Agency",
        description="This is a test tour.",
        period="2023-10-01 to 2023-10-10",
        payment_conditions="Full payment required."
    )
    reservation = Reservation.objects.create(
        user=user,
        tour=tour,
        status="pending"
    )
    assert reservation.tour.name == "Test Tour"
    assert reservation.status == "pending"

@pytest.mark.django_db
def test_review_creation(user):
    tour = Tour.objects.create(
        name="Test Tour",
        agency="Test Agency",
        description="This is a test tour.",
        period="2023-10-01 to 2023-10-10",
        payment_conditions="Full payment required."
    )
    review = Review.objects.create(
        user=user,
        tour=tour,
        rating=8,
        comment="Great tour!"
    )
    assert review.rating == 8
    assert review.comment == "Great tour!"
