
import firebase_admin
from firebase_admin import credentials, auth

# Use raw string to avoid issues with backslashes
cred = credentials.Certificate(r'C:\Users\Administrator\Documents\GREENET\greenet-9ab8c-firebase-adminsdk-m849n-b18f011cb3.json')
firebase_admin.initialize_app(cred)

# Generate a custom token for a specific user ID
custom_token = auth.create_custom_token('greenet-9ab8c')
print(custom_token.decode('utf-8'))

