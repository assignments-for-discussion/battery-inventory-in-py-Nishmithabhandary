def count_batteries_by_health(present_capacities, rated_capacity=120):
    counts = {"healthy": 0, "exchange": 0, "failed": 0}
    
    for capacity in present_capacities:
        soh_percentage = (capacity / rated_capacity) * 100
        
        if soh_percentage > 80:
            counts["healthy"] += 1
        elif 62 <= soh_percentage <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 5, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1

    print("Done counting :)")

if _name_ == '_main_':
    test_bucketing_by_health()
