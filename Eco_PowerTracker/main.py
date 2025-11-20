from EcoPowerTracker import power_tracker as pt

pt.log_usage("Laptop", 5, 60)
pt.log_usage("Fan", 10, 75)

pt.calculate_bill()
pt.suggest_savings()

pt.compare_usage(2.5, 3.0)

pt.encrypt_report("monthly_report.txt")
