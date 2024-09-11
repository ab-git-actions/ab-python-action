import os

# Get the message from environment variable
message = os.getenv('MESSAGE', 'No message provided')

# Print the message
print(f"Message from the GitHub Action: {message}")
