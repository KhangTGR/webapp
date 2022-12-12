# Simple Chat App
# How to use
- Using Dockerfile to build image
- Image using AWS DynamoDB and Flask to design a Webchat App
- Add you access key & secret key on 'app.py' to connect to AWS:
   os.environ['AWS_ACCESS_KEY_ID'] = "Add your access key"
   os.environ['AWS_SECRET_ACCESS_KEY'] = "Add your secret access key"
- To create new chat channel, please add postfix more to URL
   Example: http://example.com/001