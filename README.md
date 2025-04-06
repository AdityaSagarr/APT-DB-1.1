

## 📚 AptiCore Firestore Question Database

This repository contains categorized aptitude questions stored in Google Firestore. The structure is well-defined to support scalable and structured question storage, categorization, and querying.

Note:
- Per chapter 40 questions have been uploaded
- As of now from Simple vs Latex type, Simple questions are inserted 

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
Sure! Here's a cleanly formatted **Markdown version** of your list for use in your README or documentation:

```plaintext
1_arithmetic_number
├── 1.Number_System.json
├── 2.HCF_LCM.json
├── 3.Decimal_Fractions.json
├── 4.Simplification.json
├── 5.Square_Cube_Roots.json
├── 6.Average.json
├── 9.Surds_Indices.json
└── 10.Logarithms.json

2_algebra_aptitude
├── 7.Problems_on_Numbers.json
├── 8.Problems_on_Ages.json
├── 11.Percentage.json
├── 12.Profit_Loss.json
├── 13.Ratio_Proportion.json
├── 14.Partnership.json
└── 15.Chain_Rule.json

3_time_work_speed
├── 16.Pipes_Cisterns.json
├── 17.Time_Work.json
├── 18.Time_Distance.json
├── 19.Boats_Streams.json
└── 20.Problems_on_Trains.json

4_geometry_mensuration
├── 24.Area.json
├── 25.Volume_Surface_Area.json
└── 34.Heights_Distances.json

5_logical_reasoning
├── 35.Odd_Man_Out_Series.json
├── 27.Calendar.json
├── 28.Clocks.json
└── 26.Races_Games.json

6_probability_combinatorics
├── 30.Permutations_Combinations.json
└── 31.Probability.json

7_financial_math_apps
├── 29.Stocks_Shares.json
├── 22.Simple_Interest.json
├── 23.Compound_Interest.json
├── 32.True_Discount.json
├── 33.Bankers_Discount.json
└── 21.Alligation_Mixture.json
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
For any queries connect me at
- adityasagar@socialmistry.com
- www.linkedin.com/in/adityasagarr
