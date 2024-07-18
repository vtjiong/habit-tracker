import requests
from datetime import datetime
USERNAME = "Your Username"
token="Your Token"
pixela_endpoint = "https://pixe.la/v1/users"
user_params ={
    "token":token,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# We can comment it out because we already created the user profile
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "code1",
    "name": "Coding_Graph1",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}
headers ={
    "X-USER-TOKEN": token
    # This puts the token inside the header of the requests,instead of the body of the url
}
today=datetime.now()
#This creates a datetime object of a certain year and monty and day

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"
pixel_params= {
    'date': today.strftime("%Y%m%d"),
    #This functions formats the date to a certain format
    'quantity':input("How many minutes did you code today")
}
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)
pixel_params_second={
    'quantity':'20'
}
pixel_endpoint_update=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{today.strftime("%Y%m%d")}"
# response=requests.put(url=pixel_endpoint_update,headers=headers,json=pixel_params_second)
# print(response.text)

response=requests.delete(url=pixel_endpoint,headers=headers)