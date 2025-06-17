import urllib.parse
import urllib.request

url = 'http://localhost:8000'
data = {'name': 'John Doe', 'email': 'john@example.com'}
encoded_data = urllib.parse.urlencode(data).encode()

req = urllib.request.Request(url, data=encoded_data)
response = urllib.request.urlopen(req)
print("Server response:")
print(response.read().decode())
