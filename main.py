import requests as requests
import json
import test_data


main_url = 'https://api.raiser.work/api/'
api_section = 'candidates/'
id = 1036
api_method_post = '/messages'
api_method_post_attachment = '/attachment'
api_method_get = '/messages/paged?recruitmentId=3074&q=&page=1&rows=10'
api_method_delete = 'messages/8665'

auth_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjE1MzRGMDZBNjE0MEY3RTRFQUE5QzE5RjFCMTRDQzBDMTE5OUFDQjEiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJGVFR3YW1GQTktVHFxY0dmR3hUTURCR1pyTEUifQ.eyJuYmYiOjE2Njg0MTY0MTcsImV4cCI6MTY2ODQ0NTIxNywiaXNzIjoiaHR0cDovL2F1dGgucmFpc2VyLndvcmsiLCJhdWQiOlsiaHR0cDovL2F1dGgucmFpc2VyLndvcmsvcmVzb3VyY2VzIiwiYXBpMyJdLCJjbGllbnRfaWQiOiJhbmd1bGFyYXBpMSIsInN1YiI6IjNkNTVlY2NiLTRlZGYtNDI2My1iZDhhLTYxNjM0YjVjYmE0OCIsImF1dGhfdGltZSI6MTY2ODQxNjQxNywiaWRwIjoibG9jYWwiLCJpZCI6IjNkNTVlY2NiLTRlZGYtNDI2My1iZDhhLTYxNjM0YjVjYmE0OCIsInRlbmFudF9pZCI6Ijc2MjMiLCJ0ZW5hbnRfbmFtZSI6IlNpcGVzSW5jNCIsInNjb3BlIjpbIm9wZW5pZCIsImFwaTMiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsicGFzc3dvcmQiXX0.gciQZfjfTdn4jVsehWHcu0iITwq61mWTTQ0O5Eov0FwhyE1pnIYD9QSEn44NtIaYCzgMcW6t1p1xsVgOTLLEeHExngNyBYgav5GEGBrWB8T3xT3a7bO0ZQhRbjSDSsG5faYAVqjvnsEwWqfpbrJoL40Gvo1-y3vXXCvZm5CzefeJLnQhBFs00ElzbGYDJoG5jjxlg_g5jKv9e4Fc6TflS6zwZdUnjHboVpR3XgoUDaF0aD_jsyRavbSAkWjm4BoqG5nD-RSu8vypa59WjcssLjdSuDei-xOueGYWQ4FYm2BiRA1yvOpnGYoGikcq-HvX_uP2md5EFUx09pjabUTP9g'
header = {'authorization': 'Bearer ' + auth_token}


def test_attachments_for_message():
    url = main_url + api_section + str(id) + api_method_post_attachment
    body = {"id": 0,
            "downloadBinary": [137, 80, 78],
            "contentType": "image/png",
            "fileName": "13.09.2022_14.47.08_REC.png",
            "extension": ".png",
            "file": {}
            }

    response_post_attachment = requests.post(url, json=body, headers=header)
    print("Entire JSON response attachment: for POST")
    # print(response_post_attachment.text) 7985, 7986
    assert response_post_attachment.status_code == 200, "Received POST status code != 200."
    data = json.loads(response_post_attachment.content)
    assert data["status"] == 10, "Received request's Status != 0."
    print("Printing key and value:")
    print("AttachmentID:", data["model"])
    print("Done")


# Send full draft message
def test_send_full_draft_message():
    url = main_url + api_section + str(id) + api_method_post
    body = {"recruitmentId":3074,
            "stageId":4241,
            "subject":test_data.subject,
            "message":test_data.message_full,
            "cCs":[16],
            "isDraft":True,
            "attachments": [
                {
                    "attachmentId": 7985,
                    "order": 0
                }
            ],
            "emailTemplateId": 4324,
            "employeeSignatureId":69}

    response_post = requests.post(url, json=body, headers=header)
    print("Entire JSON response: for POST")
    print(response_post.text)
    assert response_post.status_code == 200, "Received POST status code != 200."
    data = json.loads(response_post.content)
    assert data["status"] == 0, "Received request's Status != 0."


# Send simple draft message
def test_send_simple_draft_message():
    url = main_url + api_section + str(id) + api_method_post
    body = {"recruitmentId":3074,
            "stageId":4241,
            "subject":test_data.subject,
            "message":test_data.message_simple,
            "isDraft":True,
            "attachments":[],
            "employeeSignatureId":69}

    response_post = requests.post(url, json=body, headers=header)
    print("Entire JSON response: for POST")
    print(response_post.text)
    assert response_post.status_code == 200, "Received POST status code != 200."
    data = json.loads(response_post.content)
    assert data["status"] == 0, "Received request's Status != 0."


# Send simple message
def test_send_simple_message():
    url = main_url + api_section + str(id) + api_method_post
    body = {"recruitmentId":3074,
            "stageId":4241,
            "subject":test_data.subject,
            "message":test_data.message_simple,
            "isDraft":False,
            "attachments":[],
            "employeeSignatureId":69}

    response_post = requests.post(url, json=body, headers=header)
    print("Entire JSON response: for POST")
    print(response_post.text)
    assert response_post.status_code == 200, "Received POST status code != 200."
    data = json.loads(response_post.content)
    assert data["status"] == 0, "Received request's Status != 0."


# Send full message
def test_send_full_message():
    url = test_data.main_url + test_data.api_section + str(id) + test_data.api_method_post
    body = {"recruitmentId": 3074,
            "stageId": 4241,
            "subject": test_data.subject,
            "message": test_data.message_full,
            "cCs": [16],
            "isDraft": False,
            "attachments": [{
                "attachmentId": 7981,
                "order": 0
            }],
            "employeeSignatureId": 69}

    response_post = requests.post(url, json=body, headers=test_data.header)
    print("Entire JSON response: for POST")
    print(response_post.text)
    assert response_post.status_code == 200, "Received POST status code != 200."
    data = json.loads(response_post.content)
    assert data["status"] == 0, "Received request's Status != 0."


# Delete draft/schld message
def test_delete_draft_message():
    url = main_url + api_section + api_method_delete

    response_delete = requests.delete(url, headers=header, timeout=2.50)
    print("Entire JSON response: for DELETE")
    print(response_delete.text)
    assert response_delete.status_code == 200, "Received DELETE status code != 200."


# Delete NOT draft/schld message
def test_delete_not_draft_message():
    url = main_url + api_section + api_method_delete

    response_delete = requests.delete(url, headers=header, timeout=2.50)
    print("Entire JSON response: for DELETE")
    print(response_delete.text)
    messagesDelRaiserDict = json.loads(response_delete.text)
    assert messagesDelRaiserDict["error"]["code"] == 2000
    assert messagesDelRaiserDict["error"]["displayMessage"] == "Only message with draft, scheduled or error statuses can be deleted."


# Show messages and check the last one
def test_display_message():
    url = main_url + api_section + str(id) + api_method_get

    response_get = requests.get(url, headers=header)
    assert response_get.status_code == 200, "Received GET status code != 200."
    print("Started converting JSON Raiser response to Python dictionary")

    messages_raiser_dict = json.loads(response_get.text)
    print("Printing key and value")
    print("Subject:", messages_raiser_dict["model"]["items"][1]["subject"])
    assert messages_raiser_dict["model"]["items"][1]["subject"] == test_data.subject
    print("Message:", messages_raiser_dict["model"]["items"][1]["message"])
    assert messages_raiser_dict["model"]["items"][1]["message"] == test_data.message_full
    print("MessageID:", messages_raiser_dict["model"]["items"][1]["id"])
    print("Done")

