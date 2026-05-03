from collections import defaultdict, Counter

SEED_NUM = 1
STUDENT_MAJOR = "BSME"
FAVORITE_ARTIST = "EUNWOO"
LOCAL_HAZARD = "TYPHOON"
CONTROL_NUM = max(3, SEED_NUM)

stream = [
    ("TUP Manila", "BSECE"),
    ("TUP Taguig", f"BSME_v{CONTROL_NUM}"),
    ("TUP Manila", f"BSME_v{CONTROL_NUM}"),
    ("TUP Manila", "BSECE"),
    ("TUP Visayas", STUDENT_MAJOR),
    ("TUP Taguig", "BSECE"),
    ("TUP Manila", "BSECE")
]

stream.extend([
    ("TUP Manila", "BSIT"),
    ("TUP Manila", "BSECE"),
    ("TUP Taguig", "BSIT"),
    ("TUP Visayas", "BSECE"),
])

# PHASE 1: GROUP DATA
campus_data = defaultdict(list)

for campus, program in stream:
    campus_data[campus].append(program)

# PHASE 2: FREQUENCY COUNT
for campus in campus_data:
    counts = Counter(campus_data[campus])
    print(f"{campus}: {counts}")

# TOP PROGRAM IN MANILA
manila_top = Counter(campus_data["TUP Manila"]).most_common(1)

print("Top program in TUP Manila:", manila_top)
# CONTROL_NUM
print("CONTROL_NUM Used:", CONTROL_NUM)

# STUDENT_MAJOR
print("STUDENT_MAJOR Used:", STUDENT_MAJOR)

# Expanded Stream Length
print("Expanded Stream Length:", len(stream))

# TUP Manila applications
manila_apps = campus_data["TUP Manila"]
print("Total Applications Processed for TUP Manila:", len(manila_apps))

# Top program + frequency
manila_counter = Counter(manila_apps)
top_program, freq = manila_counter.most_common(1)[0]

print("Top Requested Program at TUP Manila:", top_program)
print("Exact Frequency of Top Program:", freq)