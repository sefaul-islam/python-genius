def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    # 1. Calculate total monthly cost (instances * hourly_rate * 720 hours)
    total_cost = instance_count * hourly_rate * 720
    
    # 2. Implement conditional check against budget_cap
    if total_cost > budget_cap:
        # Calculate how much it exceeded the budget
        excess_amount = total_cost - budget_cap
        return f"REJECTED: Budget Exceeded by ${excess_amount:,.2f}!"
    else:
        # Return the approved message
        return f"APPROVED: Total Estimated Cost is ${total_cost:,.2f}."

# Test Cases to verify execution:
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))


print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))
