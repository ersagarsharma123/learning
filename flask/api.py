import requests
import datetime

# Base URL and API Key
BASE_URL = "https://navitas-solar.frappe.cloud/api/resource/ToDo"
API_KEY = "eda788a42ae8c4d"
API_SECRET = "b81feba0b4d97a8"
HEADERS = {
    "Authorization": f"token {API_KEY}:{API_SECRET}",
    "Content-Type": "application/json",
}

def create_todo():
    # Create a new ToDo item
    data = {
        "description": "Test ToDo Item Your Name vikash sharma",
        "status": "Open",
        "priority": "Medium",
        "date": datetime.date.today().strftime("%Y-%m-%d"),
    }

    response = requests.post(BASE_URL, json=data, headers=HEADERS)
    response_data = response.json()

    if response.status_code == 200:
        print("ToDo item created:", response_data)
        return response_data["data"]["name"]  # Return the unique name of the created ToDo item
    else:
        print("Error creating ToDo item:", response_data)
        return None

def read_todo():
    # Read all ToDo items
    response = requests.get(f"{BASE_URL}?fields=[\"*\"]", headers=HEADERS)
    response_data = response.json()

    if response.status_code == 200:
        print("ToDo items:", response_data)
    else:
        print("Error reading ToDo items:", response_data)

def update_todo(todo_name):
    # Update the status of a ToDo item
    data = {"status": "Closed"}

    response = requests.put(f"{BASE_URL}/{todo_name}", json=data, headers=HEADERS)
    response_data = response.json()

    if response.status_code == 200:
        print("ToDo item updated:", response_data)
    else:
        print("Error updating ToDo item:", response_data)

def delete_todo(todo_name):
    # Delete a ToDo item
    response = requests.delete(f"{BASE_URL}/{todo_name}", headers=HEADERS)

    if response.status_code == 200:
        print("ToDo item deleted successfully.")
    else:
        print("Error deleting ToDo item:", response.json())

if __name__ == "__main__":
    # Step 1: Create a new ToDo item
    todo_name = create_todo()

    if todo_name:
        # Step 2: Read the created ToDo item
        read_todo()

        # Step 3: Update the status of the ToDo item to "Closed"
        update_todo(todo_name)

        # Step 4: Delete the ToDo item
        delete_todo(todo_name)
