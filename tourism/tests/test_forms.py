import pytest
from tours.forms import ReservationForm, ReviewForm

@pytest.mark.django_db
def test_reservation_form_valid():
    form_data = {'status': 'pending'}
    form = ReservationForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_review_form_valid():
    form_data = {'rating': 8, 'comment': 'Great tour!'}
    form = ReviewForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_review_form_invalid_rating():
    form_data = {'rating': 11, 'comment': 'Great tour!'}  # Invalid rating
    form = ReviewForm(data=form_data)
    assert not form.is_valid()
