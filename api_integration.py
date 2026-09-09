"""
Task 2: API Integration & JSON Handling

Objective:
- Fetch data from an API
- Parse JSON responses
- Apply filtering/search logic
- Handle API errors
"""

import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

# Change this value to search for another username
SEARCH_USERNAME = "Bret"

print("=" * 60)
print("        API INTEGRATION & JSON HANDLING")
print("=" * 60)

try:
    # Fetch data from API
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    # Convert JSON response to Python objects
    users = response.json()

    print("\nAvailable Usernames")
    print("-" * 30)

    for user in users:
        print(user["username"])

    print("\nSearching for username:", SEARCH_USERNAME)

    found = False

    for user in users:
        if user["username"].lower() == SEARCH_USERNAME.lower():

            print("\nUser Found")
            print("-" * 30)
            print("Name      :", user["name"])
            print("Username  :", user["username"])
            print("Email     :", user["email"])
            print("Phone     :", user["phone"])
            print("Website   :", user["website"])
            print("City      :", user["address"]["city"])
            print("Company   :", user["company"]["name"])

            found = True
            break

    if not found:
        print("\nNo user found with that username.")

except requests.exceptions.ConnectionError:
    print("[ERROR] Unable to connect to the Internet.")

except requests.exceptions.Timeout:
    print("[ERROR] Request timed out.")

except requests.exceptions.HTTPError as e:
    print("[ERROR] HTTP Error:", e)

except Exception as e:
    print("[ERROR] Unexpected Error:", e)

finally:
    print("\n[SUCCESS] Program completed successfully.")