from models.base_model import BaseModel
import unittest
import uuid
from datetime import datetime, timedelta
class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""
    def setUp(self):
        """set up"""
        self.model = BaseModel()
        self.model.name = "gabriel"
        self.model.my_number = 14

    def tearDown(self):
        """tear down"""
        pass

    def test_to_dict(self):
        """test to_dict method"""
        model_dict = self.model.to_dict()
        created_at = self.model.created_at.isoformat()
        updated_at = self.model.updated_at.isoformat()
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('my_number', model_dict)
        self.assertIn('id', model_dict)
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['name'], self.model.name)
        self.assertEqual(model_dict['my_number'], self.model.my_number)
        self.assertEqual(model_dict['created_at'], created_at)
        self.assertEqual(model_dict['updated_at'], updated_at)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_init_name_number(self):
        """ test initial value"""
        expected_id = str(uuid.uuid4())
        self.assertEqual(self.model.name, "gabriel")
        self.assertEqual(self.model.my_number, 14)
        self.assertNotEqual(self.model.id, expected_id)

    def test_save(self):
        """ Test save"""
        initially_updated_at = self.model.updated_at
        self.model.save()
        self.assertAlmostEqual(self.model.updated_at, initially_updated_at, delta=timedelta(seconds=1))
    def test_kwargs(self):
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.name, self.model.name)
        self.assertEqual(new_model.my_number, self.model.my_number)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
