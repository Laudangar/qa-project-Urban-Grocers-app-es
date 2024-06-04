import sender_stand_request
import data

def get_new_user_token(kits_body):
    current_body = data.kit_body.copy()
    current_body["kits_body"] = kits_body
    return current_body #pasar al final

def positive_assert(kits_body):
    kit_body = get_kit_body(kits_body)
    kit_response = sender_stand_request.get_new_user_token(kits_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["authToken"] != ""

    kit_table_response = sender_stand_request.get_new_user_token()
    str_kit = kit_body["kits_body": "a","Abcd" * 511 + "a"] + kit_response.json()["authToken"]
    assert kit_table_response.text.count(str_kit) == 1

def negative_assert_code_400(kits_body):
    kit_body = get_new_user_token(kits_body)
    response = sender_stand_request.post_new_client_kit(kits_body)

    assert response.status_code == 400

    assert response.json()["code"] == 400
    assert response.json()["message"] == "El numero que ingresaste es incorrecto. " \
                                         "los numeros de caracteres deben tener al menos 1 caracter y no más de 512 caracteres"

def test_The_allowed_number_of_1_characters_get_success_response():
    positive_assert("a")


def test_The_allowed_number_of_511_characters_get_success_response():
    positive_assert ("Abcd" * 511 + "a")


def test_The_number_of_characters_is_less_than_the_allowed_amount():
    negative_assert_code_400 ("")


def test_The_allowed_number_of_512_characters_get_success_response():
    negative_assert_code_400 ("Abcd" * 512)

def test_Special_characters_allowed():
    positive_assert("\"№%@\",")

def test_spaces_are_allowed():
    positive_assert(" A Aaa ")

def test_Numbers_allowed():
    positive_assert("123")

def test_Parameter_is_not_passed_in_the_request():
    kits_body = get_new_user_token
    negative_assert_code_400(kits_body)

def test_A_different_type_of_parameter_was_passed():
    kits_body = get_new_user_token(123)
    response = sender_stand_request.post_new_client_kit(kits_body)
    assert response.status_code == 400
