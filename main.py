
def count_batteries_by_health(present_capacities):
    counts = {"healthy": 0, "exchange": 0, "failed": 0}   # dictionary with count set to Zero for each health category
    rated_capacity = 120      # related capacity: It is a rated capacity of a new battery

    if not present_capacities:
       return counts     #IF the list is empty , return the counts without processing
    for present_capacity in present_capacities:
        
        soh_percentage = (present_capacity / rated_capacity) * 100    
        # the above formula is to calculate State-of-Health (SoH) in percentage


        # now our job is to classify the batteries based on SoH ranges
        if soh_percentage > 80:
            counts["healthy"] += 1
        elif 62 <= soh_percentage <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1
    return counts        # we have to return 'counts' contains the final count for each health category after processing all batteries


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]   #not empty list
  counts = count_batteries_by_health(present_capacities)
  print("For non empty list -Counts: ",counts)       # to print the count of the each health category after processing all batteries
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")  

  empty_capacities = []   #empty list
  empty_counts = count_batteries_by_health(empty_capacities)
  print("empty list -Counts: ",empty_counts)       # to print the count of the each health category after processing all batteries
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)
  
  print("Done counting :)")
  


if __name__ == '__main__':
  test_bucketing_by_health()
