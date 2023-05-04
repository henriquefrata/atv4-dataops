from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests
import csv

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {

  "type": "service_account",
  "project_id": "methodical-mark-382223",
  "private_key_id": "65a264dd0f1c782d4eeb53c10d1b71c03d84bca8",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCtdTeI0L9zIay1\nHXo3lLeNCa8tIyFzyS26Hv3oDPWGU5EEGdkayRXwxxNJ2fOJ9shwWicQQtH/3Tkt\n/4QB86uQvSTccdXIL/UkEViBPl5yDnkzdKUMpGRrXYXW+A7m13MSjbN/1TyymqUI\nXuKa+VzLiq/mcQg/+sbtB7JqCv4uFJBqXoQTTjvZ/oaxA8fvqMVFocaztIVNzMPK\njCn14qjxnTXsm46eKOO0IThk/Yqw2cm6yqon+NSn733qywc+CpolFH3tlxDcdApa\npkr6JgRq0iXzJ7r60uf9qMLIZZLsUSgpxG7Q/3IrDZcTZFKOCMpRXrkrwbxyfDty\nj+qxZh7pAgMBAAECgf8BsaNZMrCr7yhAnIkVAd7JAc80IaOx/cT0jFjuazH6ndZM\ns/PqzwvnzgniLr6yGjba4gZ/oidq2D42tMgVPMvwHei+Pl5YFh/Oulyi5nkFpB6K\n4hi6huB0K/Wio8mBd5koFTorhWmSVPBHpKWR3d2KH1CYb4IlHc3Tgr+7SWAyEv01\ne0XGgUZEqea/h+pNtQ6z9G6xtm/QIo3a3DcNNL6fHseCLCWBYKPUthxR1dp+yyXU\npf964sEJuo5vG1UjRTuwqlYQV4ZwYDfw7wYXnuAflfMMfIr/HlxHvQMvx64SQmoF\ndUUwXQ+bLFYBoMVZabsiV476+c0RlyKfWXGi0UECgYEA4xGpvUCQvI2oNuvPawcE\nJf4wB3ElXrs/Nr01uOdyWyVrDr+Cd8y+lr83/LTAzb7ZDftpsL62lGyL3ARH1K/s\nfeSHDieMRTfTwrA8hDUBvRqoX/w7ZWepAjtGXoRPDeb5V8YlUc/viu/t+Oq8KBuN\niCvev9YICw77Q0wO/M7OsPECgYEAw47p37ZR/OxE8mW9OqjmDt/KSZobVyTOWuLo\n4HzrkqbV5sui0WiOngQia7XEmxYlSKEMH3UqSAnzkTw0sx0rU34kWE1oFUhc9AE6\nKoMnlLqIuDCvvbXSI1HeBYyKlD6/s6Pnp4z2ULy/JV+Lxl+mPVE5C4VprNUFrygT\nvC48TXkCgYB8cz7ToeJx5TXPvBh3cWX9qL4MJiA0Nm4kAznBeOB9QhnWAHJyVH4U\nwwLddvfBDBuMhUHdA/mviXpyAMqZsD3uleTLhjNj8IAYUV0pnJ+yVDz6NpUbM+A2\nf+RGgz+MwA3i5I+pskx4mp2T8ptjZA6DFoBEJftMjE58COCiAHraEQKBgQCr4LM7\n1eHvu7XJmpQbt5EkZ5tC33jCOe5IwYDOtdzS82GzTS2Ygh4/UgDyzDq12FwCntGp\n4G++C0kRUGo9Nxj6dDb7iWU+t3BDYcS+0rF6Lgy2XsxHoEPGmVDbba/rJc+V0yxq\n/iELyyjxby3JuA3DfNz3fFXp+vzY+w+FaNnFeQKBgQDedPyJY5OnjZHrSwfZjFJ/\n/T6Uwnjyduyj3PXp89jDjPo981AxPKJ8cznGeBRiz5xHZ0Vn9GcYLPIiIuZhfrHk\n+vDy7no+7Fwu60UGtsphBdp8rY5KED8vBAkXNeNAbyqU9Y4n0zGljfXBqVaqOp7G\nukaZY8JDAPLSZIu5CuZSAg==\n-----END PRIVATE KEY-----\n",
  "client_email": "conta-atv4@methodical-mark-382223.iam.gserviceaccount.com",
  "client_id": "112399296671854291158",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/conta-atv4%40methodical-mark-382223.iam.gserviceaccount.com"

}

try:

  """Uploads a file to the bucket."""
  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('atv4henriquefrata') ### Nome do seu bucket
  blob = bucket.blob('atv4.csv')

  pages = []
  names = "Name \n"

  for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

  for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
      names = names + artist_name.contents[0] + "\n"

    blob.upload_from_string(names, content_type="text/csv")

except Exception as ex:
  print(ex) 
