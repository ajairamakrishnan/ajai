import json

with open("data.json",'r') as f:
    data =f.read()


records = json.loads(data)


gender = records[0]['results'][0]['gender']
email = records[0]['results'][0]['email']
name_title = records[0]['results'][0]['name']['title']
name_first = records[0]['results'][0]['name']['first']
name_last = records[0]['results'][0]['name']['last']
location_street_number =  records[0]['results'][0]['location']['street']['number']
location_street_name =  records[0]['results'][0]['location']['street']['name']
location_city = records[0]['results'][0]['location']['city']
location_state = records[0]['results'][0]['location']['state']
location_country = records[0]['results'][0]['location']['country']
location_postcode = records[0]['results'][0]['location']['postcode']
dob_date = records[0]['results'][0]['dob']['date']
dob_age = records[0]['results'][0]['dob']['age']
registered_date = records[0]['results'][0]['registered']['date']
registered_age = records[0]['results'][0]['registered']['age']
login_uuid = records[0]['results'][0]['login']['uuid']
login_username = records[0]['results'][0]['login']['username']
login_password = records[0]['results'][0]['login']['password']
login_salt = records[0]['results'][0]['login']['salt']
login_md5 = records[0]['results'][0]['login']['md5']
login_sha1 = records[0]['results'][0]['login']['sha1']
login_sha256 = records[0]['results'][0]['login']['sha256']
location_coordinates_latitude = records[0]['results'][0]['location']['coordinates']['latitude']
location_coordinates_longitude = records[0]['results'][0]['location']['coordinates']['longitude']
location_timezone_offset = records[0]['results'][0]['location']['timezone']['offset']
location_timezone_description = records[0]['results'][0]['location']['timezone']['description']
phone = records[0]['results'][0]['phone']
cell = records[0]['results'][0]['cell']
id_name = records[0]['results'][0]['id']['name']
id_value = records[0]['results'][0]['id']['value']
picture_large = records[0]['results'][0]['picture']['large']
picture_medium = records[0]['results'][0]['picture']['medium']
picture_thumbnail = records[0]['results'][0]['picture']['thumbnail']
nat = records[0]['results'][0]['nat']


def customer_info(data):
    customer_info=dict()
    
    gender = data['results'][0]['gender']
    email = data['results'][0]['email']
    name_title = data['results'][0]['name']['title']
    name_first = data['results'][0]['name']['first']
    name_last = data['results'][0]['name']['last']
    location_street_number =  data['results'][0]['location']['street']['number']
    location_street_name =  data['results'][0]['location']['street']['name']
    location_city = data['results'][0]['location']['city']
    location_state = data['results'][0]['location']['state']
    location_country = data['results'][0]['location']['country']
    location_postcode = data['results'][0]['location']['postcode']
    dob_date = data['results'][0]['dob']['date']
    dob_age =data['results'][0]['dob']['age']
    registered_date = data['results'][0]['registered']['date']
    registered_age = data['results'][0]['registered']['age']
    login_uuid = data['results'][0]['login']['uuid']
    login_username = data['results'][0]['login']['username']
    login_password = data['results'][0]['login']['password']
    login_salt = data['results'][0]['login']['salt']
    login_md5 = data['results'][0]['login']['md5']
    login_sha1 = data['results'][0]['login']['sha1']
    login_sha256 = data['results'][0]['login']['sha256']
    location_coordinates_latitude = data['results'][0]['location']['coordinates']['latitude']
    location_coordinates_longitude = data['results'][0]['location']['coordinates']['longitude']
    location_timezone_offset = data['results'][0]['location']['timezone']['offset']
    location_timezone_description = data['results'][0]['location']['timezone']['description']
    phone = data['results'][0]['phone']
    cell = data['results'][0]['cell']
    id_name = data['results'][0]['id']['name']
    id_value = data['results'][0]['id']['value']
    picture_large = data['results'][0]['picture']['large']
    picture_medium = data['results'][0]['picture']['medium']
    picture_thumbnail = data['results'][0]['picture']['thumbnail']
    nat = data['results'][0]['nat']
    


    customer_info['gender']=gender
    customer_info['email']=email
    customer_info['name_title']=name_title
    customer_info['name_first']=name_first
    customer_info['name_last']=name_last
    customer_info['location_street_number']=location_street_number
    customer_info['location_street_name']=location_street_name
    customer_info['location_city']=location_city
    customer_info['location_state']=location_state
    customer_info['location_country']=location_country
    customer_info['location_postcode']=location_postcode
    customer_info['dob_date']=dob_date
    customer_info['dob_age']=dob_age
    customer_info['registered_date']=registered_date
    customer_info['registered_age']=registered_age
    customer_info['login_uuid']=login_uuid
    customer_info['login_username']=login_username
    customer_info['login_password']=login_password
    customer_info['login_salt']=login_salt
    customer_info['login_md5']=login_md5
    customer_info['login_sha1']=login_sha1
    customer_info['login_sha256']=login_sha256
    customer_info['location_coordinates_latitude']=location_coordinates_latitude
    customer_info['location_coordinates_longitude']=location_coordinates_longitude
    customer_info['location_timezone_offset']=location_timezone_offset
    customer_info['location_timezone_description']=location_timezone_description
    customer_info['phone']=phone
    customer_info['cell']=cell
    customer_info['id_name']=id_name
    customer_info['id_value']=id_value
    customer_info['picture_large']=picture_large
    customer_info['picture_medium']=picture_medium
    customer_info['picture_thumbnail']=picture_thumbnail
    customer_info['nat']=nat
    
    
    
    
    return customer_info

customer_info (data=records[1])

my_new_data = [customer_info(data) for data in records]

len(my_new_data)

my_new_data

my_new_data[1]

my_new_data[2]

my_new_data[3]

my_new_data[4]

import pandas as pd
df = pd.DataFrame(my_new_data)

df

df.to_csv("ajai_.csv")

df

