

## 📚 AptiCore Firestore Question Database

This repository contains categorized aptitude questions stored in Google Firestore. The structure is well-defined to support scalable and structured question storage, categorization, and querying.

---

### 🧠 Question Data Structure

Each question in the database follows this schema:

```json
{
  "id": "M.1.1.S.22",
  "type": "MCQuestion",
  "text": "Question text here",
  "is_latex": false,
  "is_image": false,
  "image_url": null,
  "latex_string": null,
  "xp": 1,
  "tag": "Exam name, Year",
  "difficulty": "EASY",
  "topic": "Topic Name",
  "chapter": "Chapter Name",
  "option_list": [
    {
      "text": "Option A",
      "is_correct": false,
      "is_latex": false,
      "is_image": false,
      "latex_string": null,
      "image_url": null
    },
    ...
  ]
}
```

---

### 🆔 Question ID Format

The `id` field follows a structured pattern for consistency and traceability:

```
Format: M.<category_id>.<chapter_id>.<type>.<question_number>
Example: M.1.1.S.22
```

| Part        | Meaning                              |
|-------------|--------------------------------------|
| `M`         | MCQ Type                             |
| `1`         | Category ID (e.g., Arithmetic)       |
| `1`         | Chapter ID (e.g., Number System)     |
| `S/L`       | Simple (S) or LaTeX (L)              |
| `22`        | Question number                      |

---

### 📁 Folder and Category Structure

Questions are organized under folders and `.json` files. Each folder represents a category, and each file represents a chapter.

```
CATEGORIES/
├── 1_arithmetic_number
│   ├── 1.Number_System.json
│   ├── 2.HCF_LCM.json
│   └── ...
├── 2_algebra_aptitude
│   ├── 7.Problems_on_Numbers.json
│   └── ...
├── 3_time_work_speed
│   ├── 16.Pipes_Cisterns.json
│   └── ...
├── ...
```

#### 📘 Category Reference Table

| Category ID | Category Name             |
|-------------|---------------------------|
| 1           | Arithmetic and Number     |
| 2           | Algebra and Aptitude      |
| 3           | Time, Work & Speed        |
| 4           | Geometry & Mensuration    |
| 5           | Logical Reasoning         |
| 6           | Probability & Combinatorics |
| 7           | Financial Math & Applications |

---

### ☁️ Firestore Setup

This project uses Google Cloud Firestore to store and manage questions.

#### 🔐 Credentials

```python
from google.cloud import firestore
from google.oauth2 import service_account

cred = service_account.Credentials.from_service_account_file("serviceAccountKey.json")
db = firestore.Client(credentials=cred)
collection_name = "Questions_1.1"
```

#### 📥 Verifying Data

```python
def verify_firestore_data(limit=5):
    docs = db.collection(collection_name).stream()
    for doc in list(docs)[:limit]:
        data = doc.to_dict()
        print(f"ID: {doc.id}")
        print(f"Question: {data.get('text')}")
        print(f"Chapter: {data.get('chapter')}")
        print(f"Options: {[opt.get('text') for opt in data.get('option_list', [])]}")
```

---

### ✅ Insertion Status

> All questions have been successfully uploaded to Firestore under collection: **`Questions_1.1`**

---

### 📌 Notes

- Questions may include text, images, or LaTeX formats.
- Every entry is validated using a Pydantic schema before uploading.
- The Firestore `document ID` matches the `question ID`.

---

Would you like this in Markdown file format or want me to generate an actual `.md` file for download?
