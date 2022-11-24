import os
from flask import Flask, render_template
from flask import request

import boto3
from flask_dynamo import Dynamo
import key_config as keys

import datetime
import pytz

from boto3.dynamodb.conditions import Key, Attr

app = Flask(__name__)

# from boto3.session import Session
# boto_sess = Session(
#     region_name=REGION,
#     aws_access_key_id=ACCESS_KEY_ID,
#     aws_secret_access_key=SECRET_ACCESS_KEY
# )

dynamodb = boto3.resource('dynamodb',
                          region_name=keys.REGION,
                          aws_access_key_id=keys.ACCESS_KEY_ID,
                          aws_secret_access_key=keys.SECRET_ACCESS_KEY)


# app.config['AWS_ACCESS_KEY_ID'] = ACCESS_KEY_ID
# app.config['AWS_SECRET_ACCESS_KEY'] = SECRET_ACCESS_KEY
# app.config['AWS_REGION'] = REGION
# app.config['DYNAMO_ENABLE_LOCAL'] = True
# app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
# app.config['DYNAMO_LOCAL_PORT'] = 8000
# app.config['DYNAMO_SESSION'] = boto_sess

# app.config['DYNAMO_TABLES'] = [
#     {
#          TableName='users',
#          KeySchema=[dict(AttributeName='username', KeyType='HASH')],
#          AttributeDefinitions=[dict(AttributeName='username', AttributeType='S')],
#          ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
#     }, {
#          TableName='groups',
#          KeySchema=[dict(AttributeName='name', KeyType='HASH')],
#          AttributeDefinitions=[dict(AttributeName='name', AttributeType='S')],
#          ProvisionedThroughput=dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
#     }
# ]

# dynamo = Dynamo(app)
#
# with app.app_context():
#     dynamo.create_all()


@app.route("/", methods=['GET'])
def main_page():
    return render_template('index.html')


@app.route("/chat/<room>")
def chat_room(room):
    return render_template('index.html')


@app.route("/<room>")
def chat_room2(room):
    return render_template('index.html')


@app.route("/api/chat/<room>", methods=['POST', 'GET'])
def chat(room):
    # dynamo.tables['users'].put_item(data={
    #     'username': 'rdegges',
    #     'first_name': 'Randall',
    #     'last_name': 'Degges',
    #     'email': 'r@rdegges.com',
    # })

    # for table_name, table in dynamo.tables.items():
    #     print(table_name, table)

    if request.method == 'POST':

        tz_hcm = pytz.timezone('Asia/Ho_Chi_Minh')
        start_utc = datetime.datetime.now(tz_hcm)
        time_now = start_utc.strftime("%Y-%m-%d %X")

        name = time_now
        email = request.form['msg']
        password = request.form['username']

        table = dynamodb.Table('users')

        table.put_item(
            Item={
                'name': name,
                'email': email,
                'password': password
            }
        )
    else:
        email = request.form['msg']
        password = request.form['username']

        table = dynamodb.Table('users')
        response = table.query(
            KeyConditionExpression=Key('email').eq(email)
        )
        items = response['Items']
        name = items[0]['name']
        print(items[0]['password'])

    return render_template('index.html')

    # dbs = None
    # if request.method == 'POST':
    #     tz_hcm = pytz.timezone('Asia/Ho_Chi_Minh')
    #     start_utc = datetime.datetime.now(tz_hcm)
    #     time_now = start_utc.strftime("%Y-%m-%d %X")
    #     username = request.form['username']
    #     messages = request.form['msg']
    #     cur = connection.cursor()
    #     cur.execute(''' INSERT INTO chat1(room, time_now, username, msg) VALUES (%s,%s,%s,%s)''',
    #                 (room, time_now, username, messages))
    #     cur.connection.commit()
    #     cur.close()
    #     return ''
    # else:
    #     cur = connection.cursor()
    #     cur.execute(''' SELECT * FROM chat1 WHERE room=%s ''', (room,))
    #     dbs = cur.fetchall()
    #     str_result = 'Load balancing server: ' + host + "\n\n"
    #     for line in dbs:
    #         str_result = str_result + convertTuple(line) + '\n'
    #     cur.close()
    #     return str_result


if __name__ == "__main__":
    app.run(debug=True)

# REF: https://flask-dynamo.readthedocs.io/en/latest/quickstart.html#initialize-dynamo
