from django.test import TestCase
from .forms import LibraryUpdateFormTest, LibraryEditFormTest

# Create your tests here.


class TestUpdateForm(TestCase):

    def test_update_form_is_valid(self):
        update_form = LibraryUpdateFormTest(
            {
                "title": 'Game',
                "description": 'Description',
                "rating": 4,
                "minplayers": 3,
                "maxplayers": 6,
            })
        self.assertTrue(update_form.is_valid(), msg='Form is not valid')
    
    def test_update_form_is_invalid(self):
        update_form = LibraryUpdateFormTest(
            {
                "title": '',
            }
        )
        self.assertFalse(update_form.is_valid(), msg='Form is valid')


class TestEditForm(TestCase):

    def test_edit_form_is_valid(self):
        update_form = LibraryEditFormTest(
            {
                "description": 'description',
                "rating": 3,
                "minplayers": 1,
                "maxplayers": 6
            }
        )
        self.assertTrue(update_form.is_valid(), msg="Form is not valid")

    def test_edit_form_is_invalid(self):
        update_form = LibraryEditFormTest(
            {
                "description": '',
            }
        )
        self.assertFalse(update_form.is_valid(), msg="Form is valid")