from restaurant.models import Menu
from rest_framework.test import APITestCase
from restaurant.serializers import MenuItemSerializers

#Test to validate if serializer validating correct
class MenuItemSerializerTestCase(APITestCase):
    def test_Menu_serializer_valid_data(self):
        data= {
            'title' : 'Burger',
            'price' : 50,
            'inventory' : 100

        }
        serializer = MenuItemSerializers(data = data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors,{})

    # test if serializer data is updated in case any change in data model value

    def test_menu_serializer_update(self):
        item = Menu.objects.create(
            title = 'Pizza',
            price = 50,
            inventory = 100,
            description = "",
        )

        data = {
            "description" : "fast food"
        }

        serializer = MenuItemSerializers(instance=Menu,data=data, partial=True)
        self.assertTrue(serializer.is_valid())
