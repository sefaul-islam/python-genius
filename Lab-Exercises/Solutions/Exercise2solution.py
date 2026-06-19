cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
    # 1. Use a loop to count the active nodes
    active_count = 0
    for node in config["active_nodes"]:
        active_count += 1
        
    # Extract the max slots from the dictionary
    max_slots = config["total_max_slots"]
    
    # 2. Run the mathematical formula to find utilization percentage
    utilization_pct = (active_count / max_slots) * 100
    
    # 3. Print a clean summary report using string interpolation (f-strings)
    print(f"--- Audit Report: {config['cluster_name']} ---")
    print(f"Active Endpoints : {active_count}")
    print(f"Total Max Slots  : {max_slots}")
    print(f"Utilization      : {utilization_pct}%")
    print("---------------------------------------")

# Execute the audit tool
calculate_capacity(cluster_config)