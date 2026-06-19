# How I Solved Lab 3: The Deployment Budget Optimizer 💰
For this lab, I needed to build a function for the finance team to dynamically calculate monthly cloud server costs and check them against a hard budget limit. Here is the step-by-step breakdown of my logic!

## Step 1: Defining the Function
I started by creating a function called `estimate_deployment_cost` that takes in the three required parameters: `instance_count`, `hourly_rate`, and `budget_cap`. 

## Step 2: Calculating the Total Cost
The lab specified a standard 30-day billing month, which equals 720 hours of uptime. To find the total cost, I just multiplied the number of instances by the hourly rate, and then multiplied that by 720:
```python
total_cost = instance_count * hourly_rate * 720
```

## Step 3: The Conditional Budget Check
Next, I needed to check if the `total_cost` exceeded the `budget_cap`. I set up a simple `if/else` statement:
* If the cost was greater than the budget, I calculated the `excess_amount` by subtracting the budget cap from the total cost.
* If it was within the budget, the script proceeds to the `else` block.

## Step 4: Returning Formatted Strings
Instead of just printing the output inside the function, the lab required me to `return` the specific alert strings so they could be used elsewhere in the application. 

To make the dollar amounts look professional (like `$7,344.00`), I used Python's f-strings with a formatting trick: `:,.2f`. This automatically adds commas for thousands and ensures there are exactly two decimal places.

Here is what the final return logic looked like:
```python
if total_cost > budget_cap:
    excess_amount = total_cost - budget_cap
    return f"REJECTED: Budget Exceeded by ${excess_amount:,.2f}!"
else:
    return f"APPROVED: Total Estimated Cost is ${total_cost:,.2f}."
```

It was a great exercise in combining math operations with conditional logic and clean string formatting!