# test_views.py

# This is a passing test based on the code I placed in the views.py file
from django.test import RequestFactory
from aumwi import views

class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = views.HomeView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'
