
is_active = True
cpu_percent = 94.5
is_production = True

# 1. Build the compound logical matching condition statement
# Condition A: Server is not active
# Condition B: CPU is over 90.0 AND it is a production environment
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

# 2. Conditional flow to broadcast the final verdict
if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")