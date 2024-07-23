import requests
import frappe
import json

def fetch_food_order_details(month):
    url = "http://canteen.benzyinfotech.com/api/v3/customer/report"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZWRhNWExODU0OTFhYWE0MmY5YzMyZjRhMTU5MDM1ODk4ZjZiMzMxNWUzZjJjNGRiZDA1N2IyNGE3NTAzMDc3NDBlMjFlYjZmNGE4Mjk0MGUiLCJpYXQiOjE3MDQ4MDA4OTAuODc5OTI1OTY2MjYyODE3MzgyODEyNSwibmJmIjoxNzA0ODAwODkwLjg3OTkyOTA2NTcwNDM0NTcwMzEyNSwiZXhwIjoxNzM2NDIzMjkwLjgzNDkxMjA2MTY5MTI4NDE3OTY4NzUsInN1YiI6IjI2NSIsInNjb3BlcyI6W119.CwDEjlHoRtOXdFcaO6KGGxV202AOA7MMtJVPtKzgLqzTFzUUnDLGBd7PNAtHO2--3YOathM9HOG8hYjY8wjktXZIoCGUR9GWIaEVUxLwFq927CrSf05NuqTBTrJcDeBOjXDvKcSBiJ2A994FC2IunPcdkaZ4jpoaWBIaWueYUbHviYSQuLec3tFcAMg4njrImAlaN9k-QKkHetpdrdbUEX1Wzq4X-1QwuOx7W3W2nbbxaoNgFX1gaabxi00ZO7h5MokGvtqy_gCkS9TYoM74VfxmTyAAczjttLcPqDNiAL_ZJdutDMezw32CZj8G8l8PUL46F_BuaxatZDBUZxeClZh4_0Wvo9GX4zqF2XvHdzZHnwdB414vNCl8itaGW9w7QWbdchPOglhnek32ZmkH0MIqeOBhnAyHo5_WbP0uLd_3qmz3w04nvTbTGV25-QebaxPAsVD0-7Za1sVpqB_FD6yEeliaEzdxl_8gA5IH59uowpfPYgUIjom8NVEASuYsAwb0q3f0jhNRfwg2zmXNenoDunh_dN9l2NRjI2gdZueSMwu6IJLQK46jpn01uG2iQ1xx-pFJAGe_bzSceLsho3dbtabym3tMqi0Ac02xUP9Mn50LdkFJGNVU9jiuHQfyjQirDtGUfya3aIvpJlCGx9Cx99s_4P89uDnOiXy3A1Q"
    }
    data = {"month": month}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@frappe.whitelist(allow_guest=True , xss_safe=False)
def process_food_orders(month):
    data = fetch_food_order_details(month)
    
    orders = []
    
    for report in data["reports"]:
        date = report.get("date")
        opt_ins = report.get("opt_ins", {})
        
        breakfast_status = "Not Ordered"
        lunch_status = "Not Ordered"
        dinner_status = "Not Ordered"
        
        if isinstance(opt_ins, dict):
            breakfast_status = opt_ins.get("breakfast", "Not Ordered")
            lunch_status = opt_ins.get("lunch", "Not Ordered")
            dinner_status = opt_ins.get("dinner", "Not Ordered")
        
        fine = 0
        if breakfast_status == "Pending":
            fine += 100
        if lunch_status == "Pending":
            fine += 100
        if dinner_status == "Pending":
            fine += 100

        orders.append({
            "date": date,
            "breakfast_status": breakfast_status,
            "lunch_status": lunch_status,
            "dinner_status": dinner_status,
            "fine": fine
        })    
    return orders
