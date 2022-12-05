import requests as requests
import json
from requests.exceptions import HTTPError

main_url = 'https://api.raiser.work/api/'
api_section = 'candidates/'
id = 1036
api_method_get = '/messages/paged?recruitmentId=3074&q=&page=1&rows=10'


def test_display_message():
    url = main_url + api_section + str(id) + api_method_get
    auth_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjE1MzRGMDZBNjE0MEY3RTRFQUE5QzE5RjFCMTRDQzBDMTE5OUFDQjEiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJGVFR3YW1GQTktVHFxY0dmR3hUTURCR1pyTEUifQ.eyJuYmYiOjE2NjgxNDkzMTAsImV4cCI6MTY2ODE3ODExMCwiaXNzIjoiaHR0cDovL2F1dGgucmFpc2VyLndvcmsiLCJhdWQiOlsiaHR0cDovL2F1dGgucmFpc2VyLndvcmsvcmVzb3VyY2VzIiwiYXBpMyJdLCJjbGllbnRfaWQiOiJhbmd1bGFyYXBpMSIsInN1YiI6IjNkNTVlY2NiLTRlZGYtNDI2My1iZDhhLTYxNjM0YjVjYmE0OCIsImF1dGhfdGltZSI6MTY2ODE0OTMxMCwiaWRwIjoibG9jYWwiLCJpZCI6IjNkNTVlY2NiLTRlZGYtNDI2My1iZDhhLTYxNjM0YjVjYmE0OCIsInRlbmFudF9pZCI6Ijc2MjMiLCJ0ZW5hbnRfbmFtZSI6IlNpcGVzSW5jNCIsInNjb3BlIjpbIm9wZW5pZCIsImFwaTMiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsicGFzc3dvcmQiXX0.fRW3t0v6Q5QwI3XJVhqJC1Mn3AsbwTTsxppFCVT48qM5TniB_eermrsbUryPY_Fv_5mMwtLI3MPL9lNm1qvjIKmAXQRyLjdPOLFbRsLccSUYTcjKtofmeTVR2IneRHDt_smW63tcy1bp8LvhqK7lCXnrSZtZIGQEc1LKqKMmjx49jaBprl1o4PusG0mlKyoVPjt5J9eGsYgV_b0WYYm4tm-ea2u1aHqn3FY_v00t8IOuzRSt3hjrBaDCJb0cfOBmC39a_2b32iIrc7ArDT7U7EonAFvsGp2KdZIff63_C7803Xb7locuJySP8hR38dV02Vt9CCdEtrr1pPsXFhtIEA'
    header = {'authorization': 'Bearer ' + auth_token}

    response_get = requests.get(url, headers=header).text
    print("Started converting JSON Raiser response to Python dictionary")

    messages_raiser_dict = json.loads(response_get)

    print("Printing key and value")
    print("Subject:", messages_raiser_dict["model"]["items"][0]["subject"])
    print("Message:", messages_raiser_dict["model"]["items"][0]["message"])
    print("Done")



    response_post = requests.post(url, json=body, headers=header)
    print("Entire JSON response: for POST")
    print(response_post.content)
    assert response_post.status_code == 401, "The message for the case if the status code != 200."
    data = json.loads(response_post.content)
    assert data["error"]["code"] == 2000
    assert data["error"]["displayMessage"] == "An error occurred during the activation of a particular registration. See the inner exception for details. Registration: Activator = AccessResolver (ReflectionActivator), Services = [Raiser.Accessing.IAccessResolver], Lifetime = Autofac.Core.Lifetime.CurrentScopeLifetime, Sharing = Shared, Ownership = OwnedByLifetimeScope ---> An error occurred during the activation of a particular registration. See the inner exception for details. Registration: Activator = ApplicationStorage (ReflectionActivator), Services = [Raiser.Accessing.IApplicationStorage], Lifetime = Autofac.Core.Lifetime.CurrentScopeLifetime, Sharing = Shared, Ownership = OwnedByLifetimeScope ---> An exception was thrown while invoking the constructor 'Void .ctor(Raiser.Catalog.Core.Tenant, Raiser.Catalog.Repository.Mssql.CatalogContext)' on type 'ApplicationStorage'. ---> Sequence contains no elements (See inner exception for details.) (See inner exception for details.) (See inner exception for details.)"
    assert data["status"] == 1
