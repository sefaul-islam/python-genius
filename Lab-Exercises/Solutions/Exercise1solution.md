#This is a solution to the Student-Lab_Exercise1.md problem

## Step 1: Gathering User Data
Firstly I have prompted the user for their Age, Name and Developer status.

To keep the data clean, I used `.strip().lower()` on the string inputs to remove accidental spaces and standardize the text formatting. I also wrapped the age input in `int()` to ensure Python treats it as a number for my math logic later.

## Step 2: The Logic (Assigning Tiers)
Next came the brain of the script. I needed to assign a specific clearance `tier` based on two conditions: age and developer status. I set up a simple `if/elif/else` block:

* **Under 18?** Automatically assigned to `Tier 3: Guest`.
* **18 or older AND a developer?** Promoted to `Tier 1: Admin Infrastructure Access`.
* **18 or older but NOT a developer?** Placed in the default adult tier, `Tier 2: Standard Executive Access`.

## Step 3: Formatting the Output
Finally, I wanted to print out a clean summary of the user's profile. I used a multi-line **f-string** (using triple quotes `"""`) so I could easily format the text across multiple lines without messy concatenation. 

Inside the f-string, I even included a quick inline `if/else` statement `{"Yes" if is_developer else "No"}` to translate the boolean developer status back into clean, readable English!