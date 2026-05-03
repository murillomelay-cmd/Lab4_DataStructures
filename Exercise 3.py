from collections import deque, Counter

SEED_NUM = 1
STUDENT_MAJOR = "BSME"
FAVORITE_ARTIST = "EUNWOO"
LOCAL_HAZARD = "TYPHOON"
CONTROL_NUM = max(3, SEED_NUM)


burst = [
    (CONTROL_NUM, "WEATHER"),
    (CONTROL_NUM + 1, "TRAFFIC"),
    (CONTROL_NUM + 2, "WEATHER"),
    (CONTROL_NUM + 3, "WEATHER"),
    (CONTROL_NUM + 4, LOCAL_HAZARD),
    (CONTROL_NUM + 5, "WEATHER"),
    (CONTROL_NUM + 6, "TRAFFIC")
]
start_time = burst[-1][0] + 1

burst.extend([
    (start_time, "FIRE"),
    (start_time + 1, "TRAFFIC"),
    (start_time + 2, "WEATHER")
])
buffer = deque(maxlen=5)
# LOCAL_HAZARD check
local_hazard_used = LOCAL_HAZARD

# burst size
total_burst = len(burst)

# WEATHER at CONTROL_NUM + 3
weather_append = any(x[0] == CONTROL_NUM + 3 for x in buffer)

# LOCAL_HAZARD appended?
hazard_appended = any(x[1] == LOCAL_HAZARD for x in buffer)

# final length
final_len = len(buffer)

# sum of timestamps
timestamp_sum = sum(x[0] for x in buffer)
print("LOCAL_HAZARD Used:", local_hazard_used)
print("Total Burst Size:", total_burst)
print("Did WEATHER at CONTROL_NUM + 3 append?:", "Y" if weather_append else "N")
print("Did LOCAL_HAZARD append?:", "Y" if hazard_appended else "N")
print("Final Deque Length:", final_len)
print("Final Sum of Timestamps:", timestamp_sum)
print("Exact Final Deque Output:", buffer)