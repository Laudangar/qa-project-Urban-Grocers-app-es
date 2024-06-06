import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El numero que ingresaste es incorrecto. " \
                                         "los numeros de caracteres deben tener al menos 1 caracter y no más de 512 caracteres"


def negative_asert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El parámetro no se pasa en la solicitud"


def test_The_allowed_number_of_1_characters_get_success_response():
    positive_assert("a")


def test_The_allowed_number_of_511_characters_get_success_response():
    positive_assert ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_The_number_of_characters_is_less_than_the_allowed_amount():
    negative_assert_code_400 ("")


def test_The_allowed_number_of_512_characters_get_success_response():
    negative_assert_code_400 ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_Special_characters_allowed():
    positive_assert("\"№%@\",")


def test_spaces_are_allowed():
    positive_assert(" A Aaa ")


def test_Numbers_allowed():
    positive_assert("123")


def test_Parameter_is_not_passed_in_the_request():
    kit_body = get_kit_body()
    kit_body.pop("name")
    negative_asert(kit_body)

def test_A_different_type_of_parameter_was_passed():
    kit_body = get_kit_body(123)
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El número que ingresaste es incorrecto. " \
                                         "Los nombres deben tener al menos 1 carácter y no más de 512 caracteres."