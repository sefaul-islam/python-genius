# How I Solved Lab 5: System Alert Flag Evaluator 

In this lab, I built the logic for an automated error monitoring daemon. The goal was to evaluate server telemetry and decide whether an engineer needs to be woken up for an urgent dispatch. Here is how I constructed the logic gates!

## Step 1: Reviewing the Telemetry
The system provided three data points to work with:
* `is_active` (Boolean)
* `cpu_percent` (Float)
* `is_production` (Boolean)

## Step 2: Building the Compound Logic
The core of the assignment was to define a single variable, `should_alert`, based on two distinct failure scenarios.

**Scenario A: The server is down.**
I handled this using the `not` operator. If `is_active` is False, `not is_active` evaluates to True.

**Scenario B: The server is melting down.**
The CPU utilization had to be over 90.0, *but* we only care if it happens in a production environment. I linked these two checks with an `and` operator:
`(cpu_percent > 90.0 and is_production)`

**Combining Them:**
Since either scenario warrants an alert, I tied them together with an `or` operator. I also used parentheses to keep the logic perfectly readable and ensure the order of operations was explicitly clear:
```python
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)
```

## Step 3: Triggering the Alert
Finally, the script evaluates the `should_alert` flag in a simple `if/else` block. 
* If it returns `True`, it prints the `[ALERT]` dispatch warning. 
* If it returns `False`, it prints the `[OK]` safety message.

This was a great exercise in translating plain-English business rules into clean Python boolean logic!