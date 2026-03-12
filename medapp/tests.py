from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage, Facility, Service


class ContactFormTests(TestCase):
    def test_contact_form_saves_message_and_redirects(self):
        data = {
            'name': 'Alice Example',
            'email': 'alice@example.com',
            'subject': 'Test Inquiry',
            'message': 'Hello, this is a test.'
        }
        response = self.client.post(reverse('contact'), data)
        # successful post should redirect back to contact page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('contact'))
        # the message should be recorded in the database
        msg = ContactMessage.objects.first()
        self.assertIsNotNone(msg)
        self.assertEqual(msg.name, data['name'])
        self.assertEqual(msg.email, data['email'])
        self.assertEqual(msg.subject, data['subject'])
        self.assertEqual(msg.message, data['message'])

    def test_contact_form_ajax_responds_json(self):
        data = {
            'name': 'Bob Ajax',
            'email': 'bob@ajax.com',
            'subject': 'AJAX Ticket',
            'message': 'Testing ajax post'
        }
        response = self.client.post(
            reverse('contact'),
            data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        payload = response.json()
        self.assertEqual(payload.get('status'), 'ok')


class FacilitySearchTests(TestCase):
    def setUp(self):
        # create services
        self.s1 = Service.objects.create(name="Maternity")
        self.s2 = Service.objects.create(name="Emergency")

        # facility 1 has maternity service, high rating, hospital
        self.f1 = Facility.objects.create(
            name="Alpha Hospital",
            location="Karen",
            facility_type="Hospital",
            level="5",
            rating=4.5,
            opening_hours="08:00-17:00",
        )
        self.f1.services.add(self.s1)

        # facility 2 has emergency service, lower rating, dispensary
        self.f2 = Facility.objects.create(
            name="Beta Dispensary",
            location="Dagoretti",
            facility_type="Dispensary",
            level="2",
            rating=2.0,
            opening_hours="07:00-12:00",
        )
        self.f2.services.add(self.s2)

        # facility 3 no services, medium rating
        self.f3 = Facility.objects.create(
            name="Gamma Pharmacy",
            location="Kawangware",
            facility_type="Pharmacy",
            level="3",
            rating=3.0,
            opening_hours="09:00-18:00",
        )

    def test_search_by_service(self):
        response = self.client.get(reverse('facilityl'), {'service': 'Maternity'})
        self.assertEqual(response.status_code, 200)
        facilities = response.context['facilities']
        self.assertIn(self.f1, facilities)
        self.assertNotIn(self.f2, facilities)
        self.assertNotIn(self.f3, facilities)

    def test_search_by_rating(self):
        response = self.client.get(reverse('facilityl'), {'rating': '3'})
        facilities = response.context['facilities']
        self.assertIn(self.f1, facilities)
        self.assertIn(self.f3, facilities)
        self.assertNotIn(self.f2, facilities)

    def test_search_by_type(self):
        response = self.client.get(reverse('facilityl'), {'type': 'Hospital'})
        facilities = response.context['facilities']
        self.assertIn(self.f1, facilities)
        self.assertNotIn(self.f2, facilities)

    def test_search_by_opening_hours(self):
        response = self.client.get(reverse('facilityl'), {'opening_hours': '09:00'})
        facilities = response.context['facilities']
        self.assertIn(self.f3, facilities)
        self.assertNotIn(self.f1, facilities)
        self.assertNotIn(self.f2, facilities)

    def test_search_query_general(self):
        response = self.client.get(reverse('facilityl'), {'q': 'Gamma'})
        facilities = response.context['facilities']
        self.assertEqual(list(facilities), [self.f3])

    def test_search_query_location(self):
        response = self.client.get(reverse('facilityl'), {'q': 'Dagoretti'})
        facilities = response.context['facilities']
        self.assertEqual(list(facilities), [self.f2])

    def test_search_query_facility_type(self):
        response = self.client.get(reverse('facilityl'), {'q': 'Pharmacy'})
        facilities = response.context['facilities']
        self.assertEqual(list(facilities), [self.f3])

    def test_search_query_opening_hours_general(self):
        # substring match in opening_hours should be included in q search
        response = self.client.get(reverse('facilityl'), {'q': '08:00'})
        facilities = response.context['facilities']
        self.assertIn(self.f1, facilities)
        self.assertNotIn(self.f2, facilities)
        self.assertNotIn(self.f3, facilities)

    def test_search_query_service_as_general(self):
        response = self.client.get(reverse('facilityl'), {'q': 'Emergency'})
        facilities = response.context['facilities']
        self.assertIn(self.f2, facilities)
        self.assertNotIn(self.f1, facilities)
        self.assertNotIn(self.f3, facilities)

    # ensure behaviour is identical on the dedicated search page
    def test_searchfacility_endpoint_uses_same_logic(self):
        response = self.client.get(reverse('searchfacility'), {'q': 'Maternity'})
        facilities = response.context['facilities']
        self.assertIn(self.f1, facilities)
        self.assertNotIn(self.f2, facilities)
        self.assertNotIn(self.f3, facilities)
