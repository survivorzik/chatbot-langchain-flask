# from src.logger import logging
# import unittest
# from unittest.mock import patch,Mock
# from app import app


# class TestApp(unittest.TestCase):

#     def setUp(self):
#         self.client = app.test_client()
#         self.baseurl='http://localhost:5000'
        
#     def test_index(self):
#         response = self.client.get(f'{self.baseurl}/')
#         # data=response.get('data')
#         print(response)
#         logging.info(str(response))
#         # self.assertEqual(response.status_code, 200)

#     @patch('app')
#     def test_chatbot_response(self, mock_chatbot):
#         test_input = 'Hello'
#         test_response = 'Hi there!'
        
#         mock_chatbot.return_value.generate_response.return_value = test_response
        
#         data = {'data': test_input}
#         response = self.client.post(f'{self.baseurl}/data', json=data)
#         # data=response.get('data')
#         # logging.info(str(data))
#         logging.info(str(response))
#         print(response,"res_test")
#         # self.assertEqual(response.json['message'], test_response)
        
#     def test_invalid_json(self):
#         response = self.client.post(f'{self.baseurl}/data', data='invalid')
#         # data=response.get('data')
#         # logging.info(str(data))
#         logging.info(str(response))
#         print(response,"res_test2")

#         # self.assertEqual(response.status_code, 400)
#         # self.assertEqual(response.json['error'], 'Invalid JSON')
        
#     def test_chatbot_exception(self):
#         mock_chatbot = Mock(side_effect=Exception('Chatbot error'))
        
#         with patch('app.Chatbot', mock_chatbot):
#             response = self.client.post(f'{self.baseurl}/data', json={'data': 'test'})
#         # data=response.get('data')
#         # logging.info(str(data))
#         print(response,"res_test3")

#         logging.info(str(response))
#         # self.assertEqual(response.status_code, 500)
#         # self.assertEqual(response.json['error'], 'Chatbot error')

# if __name__ == '__main__':
#     unittest.main()
    
    
import unittest
from app import app
from src.logger import logging

class ApiTestCase(unittest.TestCase):

    def setUp(self):  
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        logging.info(response.data)
        assert response.status_code == 200
    
    def test_index_post(self):
        mock_data = {'data': 'Hello'}
        response = self.app.post('/data', json=mock_data)
        logging.info(response.data)

        assert response.status_code == 200
        assert b'Hello' in response.data

    def test_index_exception(self):
        mock_data = {'bad_key': 'Hello'}
        response = self.app.post('/data', json=mock_data)
        logging.info(response.data)

        assert response.status_code == 400

if __name__ == '__main__':
    unittest.main()