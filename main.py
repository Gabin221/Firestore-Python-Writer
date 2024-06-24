import os
from google.cloud import firestore

def value():
    characters = "XXX"
    return characters

def update_firestore(characters):
    # Initialize Firestore
    db = firestore.Client()

    # Reference to the document
    doc_ref = db.collection('XXX').document('XXX')

    # Update the document
    doc_ref.set({
        'Valeur': characters
    })

if __name__ == "__main__":
    # Set the path to your service account key file
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'XXX.json'

    characters = value()
    print(f"Generated value: {characters}")

    # Update Firestore with the value
    update_firestore(characters)
    print("Firestore updated successfully")
