import configuration
import requests
import data
def get_docs():
    return requests.get(configuration.URL_SERVICES + configuration.DOCS_PATH)

response = get_docs()
print(response.status_code)

def get_logs():
    return requests.get(configuration.URL_SERVICES + configuration.LOG_MAIN_PATH)

response = get_logs()
print(response.status_code)
print(response.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICES + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)

def get_new_user_token():
    return requests.get(configuration.URL_SERVICES + configuration.KIT_TABLE_PATH)

response = get_new_user_token()
print(response.status_code)



def post_new_user(body):
    return requests.post(configuration.URL_SERVICES + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICES + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)

response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())


def post_new_client_kit(kits_body):
    return requests.post(configuration.URL_SERVICES + configuration.KIT_PATH,
                         json=kits_body,
                         headers=data.headers)

response =post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())



