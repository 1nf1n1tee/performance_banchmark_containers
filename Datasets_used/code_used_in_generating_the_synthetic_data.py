import pandas as pd
import numpy as np
import uuid
import random
from faker import Faker

fake = Faker()

# Parameters
TOTAL_ROWS = 10_000_000   # 10 million
UNIQUE_RATIO = 0.7
OUTPUT_FILE = "synthetic_dataset.csv"

# Calculate unique and redundant
unique_rows = int(TOTAL_ROWS * UNIQUE_RATIO)
redundant_rows = TOTAL_ROWS - unique_rows

print("Generating unique rows...")
data = {
    "id": [str(uuid.uuid4()) for _ in range(unique_rows)],
    "name": [fake.name() for _ in range(unique_rows)],
    "email": [fake.email() for _ in range(unique_rows)],
    "dob": [fake.date_of_birth(minimum_age=18, maximum_age=80) for _ in range(unique_rows)],
    "city": [fake.city() for _ in range(unique_rows)],
    "salary": [round(random.uniform(1000, 50000), 2) for _ in range(unique_rows)]
}

unique_df = pd.DataFrame(data)

print("Generating redundant rows (exact duplicates)...")
redundant_df = unique_df.sample(n=redundant_rows, replace=True, random_state=42)

print("Combining and shuffling...")
full_df = pd.concat([unique_df, redundant_df], ignore_index=True)
del unique_df, redundant_df
full_df = full_df.sample(frac=1, random_state=42).reset_index(drop=True)

print(f"Saving to {OUTPUT_FILE} (this may take a while)...")
full_df.to_csv(OUTPUT_FILE, index=False)

print("✅ CSV dataset generation completed!")
