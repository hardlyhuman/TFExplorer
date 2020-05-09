from django.test import TestCase
from base.models import API, APIVariant
from base.serializers import APISerializer, APIVariantSerializer


class APISerializerTest(TestCase):
    def setUp(self) -> None:
        self.api = API.objects.create(
            name='Api Name',
            usage='Api Usage',
            description='Api Description',
            link='https://github.com',
        )

        self.api_data = {
            'name': 'Api Name',
            'usage': 'Api Usage',
            'description': 'Api Description',
            'link': 'https://github.com',
        }

        self.api_serializer = APISerializer(self.api)

    def test_all_fields(self):
        self.assertEqual(self.api_serializer.data.keys(), self.api_data.keys())
        self.assertEqual(
            self.api_serializer['name'].value, self.api_data['name']
        )
        self.assertEqual(
            self.api_serializer['usage'].value, self.api_data['usage']
        )
        self.assertEqual(
            self.api_serializer['description'].value,
            self.api_data['description'],
        )
        self.assertEqual(
            self.api_serializer['link'].value, self.api_data['link']
        )

    def test_from_custom_dict(self):
        api_serializer = APISerializer(data=self.api_data)
        self.assertTrue(api_serializer.is_valid())
        self.assertEqual(api_serializer.data.keys(), self.api_data.keys())
        self.assertEqual(api_serializer['name'].value, self.api_data['name'])
        self.assertEqual(api_serializer['usage'].value, self.api_data['usage'])
        self.assertEqual(
            api_serializer['description'].value, self.api_data['description']
        )
        self.assertEqual(api_serializer['link'].value, self.api_data['link'])

    def test_is_required_field_missing(self):
        for field in self.api_data.keys():
            tmp = {**self.api_data}
            tmp.pop(field)
            api_serializer = APISerializer(data=tmp)
            self.assertFalse(api_serializer.is_valid())
            self.assertIn(field, api_serializer.errors.keys())

    def test_is_required_field_empty_string(self):
        for field in self.api_data.keys():
            tmp = {**self.api_data, field: ''}
            api_serializer = APISerializer(data=tmp)
            self.assertFalse(api_serializer.is_valid())
            self.assertIn(field, api_serializer.errors.keys())


class APIVariantSerializerTest(TestCase):
    def setUp(self) -> None:
        self.api = API.objects.create(
            name='Api Name',
            usage='Api Usage',
            description='Api Description',
            link='https://github.com',
        )

        self.api_variant = APIVariant.objects.create(
            api=self.api, usage='Api Usage', description='Api Description'
        )

        self.api_data = {
            'name': 'Api Name',
            'usage': 'Api Usage',
            'description': 'Api Description',
            'link': 'https://github.com',
        }

        self.api_variant_data = {
            'api': self.api.pk,
            'usage': 'Api Usage',
            'description': 'Api Description',
        }

        self.api_serializer = APISerializer(self.api)
        self.api_variant_serializer = APIVariantSerializer(self.api_variant)

    def test_all_fields(self):
        self.assertEqual(
            self.api_variant_serializer.data.keys(),
            self.api_variant_data.keys(),
        )
        self.assertEqual(
            self.api_variant_serializer['api'].value,
            self.api_variant_data['api'],
        )
        self.assertEqual(
            self.api_variant_serializer['usage'].value,
            self.api_variant_data['usage'],
        )
        self.assertEqual(
            self.api_variant_serializer['description'].value,
            self.api_variant_data['description'],
        )

    def test_from_custom_dict(self):
        api_variant_serializer = APIVariantSerializer(
            data=self.api_variant_data
        )
        self.assertTrue(api_variant_serializer.is_valid())
        self.assertEqual(
            api_variant_serializer.data.keys(), self.api_variant_data.keys()
        )
        self.assertEqual(
            api_variant_serializer['api'].value, self.api_variant_data['api']
        )
        self.assertEqual(
            api_variant_serializer['usage'].value,
            self.api_variant_data['usage'],
        )

    def test_is_required_field_missing(self):
        for field in self.api_variant_data.keys():
            tmp = {**self.api_variant_data}
            tmp.pop(field)
            api_serializer = APIVariantSerializer(data=tmp)
            self.assertFalse(api_serializer.is_valid())
            self.assertIn(field, api_serializer.errors.keys())

    def test_is_required_field_empty_string(self):
        required_fields = ['usage', 'description']
        for field in required_fields:
            tmp = {**self.api_variant_data, field: ''}
            api_variant_serializer = APIVariantSerializer(data=tmp)
            self.assertFalse(api_variant_serializer.is_valid())
            self.assertIn(field, api_variant_serializer.errors.keys())

    def test_api_is_a_valid_primary_key(self):
        bad_api_variant_data = {**self.api_variant_data, 'api': -1}
        api_variant_serializer = APIVariantSerializer(
            data=bad_api_variant_data
        )
        self.assertFalse(api_variant_serializer.is_valid())
        self.assertIn('api', api_variant_serializer.errors)
        self.assertEqual(
            api_variant_serializer.errors['api'][0].code, 'does_not_exist'
        )
