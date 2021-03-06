import requests

API_LINK = "http://127.0.0.1:4000/"
UPLOAD_FOLDER = './static/temp/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
SEARCH_TERMS = ['name', 'method', 'company', 'model', 'city', 'country', 'city',
                'destination_city', 'destination_country', 'origin_city', 'origin_country']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_image(filename):
    file = {'file': open(filename, 'rb')}
    return requests.post(API_LINK+'upload', files=file).text
