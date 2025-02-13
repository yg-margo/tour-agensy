import pytest
from django.urls import reverse, resolve
from tours.views import TourListView, TourDetailView, ReservationCreateView, ReviewCreateView

@pytest.mark.django_db
def test_tour_list_url():
    url = reverse('tour-list')
    assert resolve(url).func.view_class == TourListView

@pytest.mark.django_db
def test_tour_detail_url():
    url = reverse('tour-detail', args=[1])
    assert resolve(url).func.view_class == TourDetailView

@pytest.mark.django_db
def test_reservation_create_url():
    url = reverse('reservation-create', args=[1])
    assert resolve(url).func.view_class == ReservationCreateView

@pytest.mark.django_db
def test_review_create_url():
    url = reverse('review-create', args=[1])
    assert resolve(url).func.view_class == ReviewCreateView
