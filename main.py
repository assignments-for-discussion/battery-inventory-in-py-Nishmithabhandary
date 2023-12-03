def classify_battery_health(present_capacity):
    """
    Classify battery health based on State of Health (SoH) percentage.

    Args:
    - present_capacity: The charge available in the battery after a full charge.

    Returns:
    - Classification of battery health: "healthy", "exchange", or "failed".
    """
    rated_capacity = 120  # Rated capacity of a new battery
    soh_percentage = (present_capacity / rated_capacity) * 100

    if soh_percentage > 80:
        return "healthy"
    elif 62 <= soh_percentage <= 80:  # Adjusted condition for "exchange"
        return "exchange"
    else:
        return "failed"

def count_batteries_by_health(present_capacities):
    """
    Count batteries based on their state of health (SoH).

    Args:
    - present_capacities: List of present capacities for each battery.

    Returns:
    - Dictionary containing counts for healthy, exchange, and failed batteries.
    """
    counts = {"healthy": 0, "exchange": 0, "failed": 0}

    for capacity in present_capacities:
        classification = classify_battery_health(capacity)
        counts[classification] += 1

    return counts

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    
    # Test case with various SoH percentages
    present_capacities = [113, 116, 80, 5, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    
    # Asserts based on provided information
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1

    # Additional boundary tests
    assert count_batteries_by_health([120, 120, 120]) == {"healthy": 3, "exchange": 0, "failed": 0}
    assert count_batteries_by_health([60, 61, 62]) == {"healthy": 0, "exchange": 3, "failed": 0}
    assert count_batteries_by_health([30, 40, 50]) == {"healthy": 0, "exchange": 0, "failed": 3}
    assert count_batteries_by_health([85, 83, 78, 60, 58]) == {"healthy": 3, "exchange": 2, "failed": 0}

    print("All tests passed! Done counting :)")

if __name__ == '__main__':
    test_bucketing_by_health()
