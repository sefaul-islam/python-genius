# How I Solved Lab 4: The Profile Text Normalization Pipeline 

In this lab, I had to deal with messy user data from a survey. The text inputs were full of random spaces and erratic capitalization. My job was to clean it all up before passing it downstream into production environments. Here is how I built the normalization pipeline!

## Step 1: Setting up the Variables
I started with the raw list of strings provided in the lab: `raw_survey_inputs`. I also had an empty list ready to hold my cleaned data called `sanitized_records`.

## Step 2: Looping Through the Data
Since I needed to process every single item in the list, I set up a `for` loop to iterate through them sequentially:
```python
for item in raw_survey_inputs:
```

## Step 3: Cleaning the Strings
This was the core part of the lab. For each `item`, I chained two Python string methods together:
1. `.strip()`: This removed all the unnecessary whitespace characters from the left and right sides of the string.
2. `.lower()`: This forced all the uppercase and mixed-case letters into standard lowercase formatting.

```python
    cleaned_item = item.strip().lower()
```

## Step 4: Storing the Results
Once the string was perfectly clean, I needed to save it. I used the `.append()` method to add my newly formatted `cleaned_item` directly into the `sanitized_records` list.

```python
    sanitized_records.append(cleaned_item)
```

## Step 5: Verification
Finally, the script prints out both lists so I can visually verify that my pipeline worked. The output clearly shows the transformation from chaotic, messy text to nice, uniform, production-ready data!