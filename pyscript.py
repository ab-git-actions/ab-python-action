import os

# Get the message from environment variable
message = os.getenv('MESSAGE', 'No message provided')

# Print the message
print(f"Message from the GitHub Action: {message}")
print("Hello AB")
print("Testing action")
print("Testing action 1")
print("Testing action 2")
print("Testing action 2")
