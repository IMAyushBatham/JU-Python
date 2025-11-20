import time
import os

usage_data = []


def log_usage(device, hours, watts):
    """Log device name, hours used, and power consumption"""
    energy = hours * watts / 1000 
    usage_data.append((device, hours, watts, energy))
    print(f"{device} used for {hours} hr(s) consumes {energy:.2f} kWh.")


def calculate_bill(rate_per_kwh=8.5):
    """Calculate total electricity bill"""
    total_energy = sum(item[3] for item in usage_data)
    bill = total_energy * rate_per_kwh
    print(f"Total Energy: {total_energy:.2f} kWh")
    print(f"Estimated Bill: ₹{bill:.2f}")
    return bill


def suggest_savings():
    """Suggest ways to save energy"""
    if not usage_data:
        print("No data logged yet.")
        return

    max_device = max(usage_data, key=lambda x: x[3])
    print(f"⚡ Your top power consumer: {max_device[0]} ({max_device[3]:.2f} kWh)")
    print("💡 Suggestion: Turn it off when not in use or use energy-efficient models.")


def compare_usage(previous, current):
    """Compare previous and current energy usage"""
    if current > previous:
        print(f"Usage increased by {current - previous:.2f} kWh. Try to reduce it!")
    elif current < previous:
        print(f"Good job! Usage decreased by {previous - current:.2f} kWh.")
    else:
        print("Usage is the same as last time.")


def encrypt_report(filename):
    """Encrypts the file name for secure storage"""
    encrypted = "".join(chr(ord(c) + 3) for c in filename)
    print(f"Encrypted file name: {encrypted}")
    print(f"File created on: {time.ctime(os.path.getctime(__file__))}")
    print(f"Last accessed on: {time.ctime(os.path.getatime(__file__))}")
    return encrypted
