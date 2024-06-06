import configuration
import requests
import data

# Solicitud GET a la combinación de URL_SERVICES y DOC_PATH
def get_docs():
    return requests.get(configuration.URL_SERVICES + configuration.DOCS_PATH)




# Solicitud para que devuelve la respuesta con los registros por defecto
def get_logs():
    return requests.get(configuration.URL_SERVICES + configuration.LOG_MAIN_PATH)




# Solicitud para que devuelve la respuesta con los datos de la tabla de la base de datos denominada "user"
def get_users_table():
    return requests.get(configuration.URL_SERVICES + configuration.USERS_TABLE_PATH)




# Solicitud para dar el token para la creación del user
def get_new_user_token():
    response = requests.post(configuration.URL_SERVICES + configuration.CREATE_USER_PATH,
                             json=data.user_body,
                             headers=data.headers)

    return response.json()["authToken"]


# Solicitud para recuperar información de la tabla de base de datos para el kit
def get_kit_table():
    return requests.get(configuration.URL_SERVICES + configuration.KIT_TABLE_PATH)




# Solicitud para la creación del user
def post_new_user(body):
    return requests.post(configuration.URL_SERVICES + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)




# solicitud Post para buscar los kits por sus productos
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICES + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)




# Solicitud Post para la creación del kit
def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICES + configuration.KIT_PATH,
                         json=kit_body,
                         headers=headers)
