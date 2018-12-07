"""Testing the web_container status code and content.

:param str arg1: The docker-machine IP address
:param int arg2: The port exposed for web_container

"""
import sys
import http.client
connection = http.client.HTTPConnection(sys.argv[1], sys.argv[2])
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))
if (response.status != 200):
    raise Exception("The page status is not 200 Ok")
else:
    content = response.read().decode("utf-8")
    if (content != "Hello from app."):
        raise Exception("Page content '{}' is not the expected 'Hello from app.'", content)
    else:
        exit(0)