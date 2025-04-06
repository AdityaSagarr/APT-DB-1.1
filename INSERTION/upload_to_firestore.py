import os
import json
from pathlib import Path
from google.cloud import firestore
from google.oauth2 import service_account
from question_schema import Question

# 🔐 Firestore setup
cred = service_account.Credentials.from_service_account_file("serviceAccountKey.json")
db = firestore.Client(credentials=cred)
collection_name = "questions2"

# 📁 Path to your data folder
BASE_DIR = Path(r"D:\WORK\APTI-CORE\BASE\DATA\IT-4(Insertion)\CATEGORIES - Copy")

# 📂 Recursively go through all folders and .json files
for folder, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".json"):
            file_path = os.path.join(folder, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    questions = data.get("questions", [])
                    for question_data in questions:
                        try:
                            q = Question(**question_data)
                            doc_ref = db.collection(collection_name).document(q.id)
                            doc_ref.set(q.dict())
                            print(f"✅ Uploaded: {q.id}")
                        except Exception as e:
                            print(f"❌ Validation/Upload failed for {question_data.get('id')}: {e}")
            except Exception as e:
                print(f"⚠️ Could not open {file_path}: {e}")
