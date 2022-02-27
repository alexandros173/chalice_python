import boto3 as boto3
from chalice import Chalice

app = Chalice(app_name='genesis')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/songs/{song}')
def songs_to_album(song):
    table_instance = boto3.resource('dynamodb').Table('genesis_albums')
    return table_instance.get_item(Key={'song_name': song}).get('Item')


@app.on_sqs_message(queue='the-genesis-queue')
def handler(event):
    for record in event:
        print(f'Message Body: {record.body}')