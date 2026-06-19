# How I Solved Lab 2: The Multi-Cluster IP Audit Tool ☁️

I recently worked on a Python lab where I had to process a raw audit log from our cloud infrastructure. The goal was to figure out how many active internal application routes we had and calculate the cluster's utilization percentage. Here is a breakdown of how I tackled the problem!

## Step 1: Navigating the Dictionary
The data was provided in a dictionary called `cluster_config`. The two pieces of information I needed were the maximum capacity (`total_max_slots`) and the list of current IP addresses (`active_nodes`). 

To grab the maximum slots, I simply accessed the dictionary key:
`max_slots = config["total_max_slots"]`

## Step 2: The Sequential Loop (Counting Nodes)
The lab specifically required me to use a sequential `for` loop to count the active endpoints. While I could have normally just used `len(config["active_nodes"])` for a quick count, I followed the requirements by setting up a counter variable. 

I initialized `active_count = 0`, and then looped through the list:
```python
for node in config["active_nodes"]:
    active_count += 1
```
For every IP address the loop found, it added 1 to my total count.

## Step 3: Calculating Utilization Percentage
With the active count and the max slots stored in variables, it was time for some simple math. I divided the active nodes by the total max slots, and then multiplied by 100 to convert it into a percentage:
```python
utilization_pct = (active_count / max_slots) * 100
```

## Step 4: Formatting a Clean Output
Finally, I needed to print a summary report. To make the output look clean and professional, I used Python's **f-strings**. This allowed me to directly inject my variables (like the cluster name, active count, and utilization percentage) right into the text strings without messy concatenation. 

The final result prints out a nice, readable audit report that clearly shows how much of the cluster is currently being used!