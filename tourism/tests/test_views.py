import pytest
from django.urls import reverse
from tours.models import Tour, Reservation, Review

@pytest.mark.django_db
def test_tour_list_view(client):
    Tour.objects.create(
        name="Test Tour",
        agency="Test Agency",
        description="This is a test tour.",
        period="2023-10-01 to 2023-10-10",
        payment_conditions="Full payment required."
    )
    url = reverse('tour-list')
    response = client.get(url)
    assert response.status_code == 200
    assert "Test Tour" in str(response.content)

@pytest.mark.django_db
def test_tour_detail_view(client):
    tour = Tour.objects.create(
        name="Test Tour",
        agency="Test Agency",
        description="This is a test tour.",
        period="2023-10-01 to 2023-10-10",
        payment_conditions="Full payment required."
    )
    url = reverse('tour-detail', args=[tour.id])
    response = client.get(url)
    assert response.status_code == 200
    assert "Test Tour" in str(response.content)

@pytest.mark.django_db
def test_reservation_create_view(client, user):
    tour = Tour.objects.create(
        name="Test Tour",
        agency="Test Agency",
        description="This is a test tour.",
        period="2023-10-01 to 2023-10-10",
        payment_conditions="Full payment required."
    )
    client.force_login(user)
    url = reverse('reservation-create', args=[tour.id])
    response = client.post(url, {'status': 'pending'})
    assert response.status_code == 302  # Redirect after successful reservation
    assert Reservation.objects.filter(user=user, tour=tour).exists()

@pytest.mark.django_db
def test_review_create_view(client, user):
    tour = Tour.objects.create(
        name="Test Tour",
        agency="Test Agency",
        description="This is a test tour.",
        period="2023-10-01 to 2023-10-10",
        payment_conditions="Full payment required."
    )
    client.force_login(user)
    url = reverse('review-create', args=[tour.id])
    response = client.post(url, {'rating': 8, 'comment': 'Great tour!'})
    assert response.status_code == 302  # Redirect after successful review
    assert Review.objects.filter(user=user, tour=tour).exists()
