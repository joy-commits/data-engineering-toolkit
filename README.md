# Data Engineering Toolkit 🔧

This repo contains a straightforward collection of Python scripts to help with common data tasks like cleaning, changing, and saving data.

### What's Inside?
This toolkit provides simple, reusable functions for:
* Data Cleaning: Functions to handle things like duplicates or empty values **(data_cleaning.py)**.
* Data Transformation: Helpers for changing data types or modifying columns **(data_transformation.py)**.
* Data Loading: A simple function to save your data to a file **(data_loading.py)**.

### How to Use
Here's a quick example of how you can use the cleaning script.
First, make sure you have pandas installed:

```bash
pip install pandas
```

Then, you can import and use the functions like this:

```Python
import pandas as pd
from data_cleaning import remove_duplicates

# Create a sample DataFrame with a duplicate row
data = {
    'user_id': [101, 102, 101, 103],
    'plan': ['basic', 'premium', 'basic', 'pro']
}
my_dataframe = pd.DataFrame(data)

print("Original Data:")
print(my_dataframe)

# Use a function from the toolkit to clean it
clean_dataframe = remove_duplicates(my_dataframe)

print("\nCleaned Data:")
print(clean_dataframe)
```

### Want to Contribute? 🤝
Got an idea or a fix? Contributions are welcome!
* Grab a copy of the project by forking it.
* Create a new branch for your work
```bash
git checkout -b feature/your-new-idea
```
* Make your changes and commit them with a clear message.
* Push your branch to your fork.
* Open a Pull Request back to the develop branch of this repository.
