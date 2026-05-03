SEED_NUM = 1
STUDENT_MAJOR = "BSME"
FAVORITE_ARTIST = "EUNWOO"
LOCAL_HAZARD = "TYPHOON"
CONTROL_NUM = max(3, SEED_NUM)

festival = {
    "Ben&Ben",
    "SB19",
    "Bini",
    "Eraserheads",
    FAVORITE_ARTIST,
    "Zild",
    f"Indie Artist {CONTROL_NUM}"
}

user_a = {"Ben&Ben", "Bini", "Maki", "Dionela", FAVORITE_ARTIST}

user_b = {
    "SB19",
    "Eraserheads",
    "Zild",
    f"Indie Artist {CONTROL_NUM}",
    "Parokya ni Edgar"
}
festival.update({
    "Kamikazee",
    "December Avenue",
    "Cup of Joe"
})
def jaccard(set1, set2):
    return len(set1 & set2) / len(set1 | set2) * 100
similarity_a = jaccard(user_a, festival)
similarity_b = jaccard(user_b, festival)
dealbreakers_a = user_a - festival
print("Jaccard Similarity (User A):", round(similarity_a, 2), "%")
print("Jaccard Similarity (User B):", round(similarity_b, 2), "%")
print("User A Dealbreakers:", dealbreakers_a)
# Total artists in expanded festival
print("Total Artists in Expanded Festival:", len(festival))

# Intersection (User A & Festival)
intersection_a = user_a & festival
print("Length of Intersection (User A & Festival):", len(intersection_a))

# Union (User A & Festival)
union_a = user_a | festival
print("Length of Union (User A & Festival):", len(union_a))

# Jaccard Similarity Function
def jaccard(set1, set2):
    return len(set1 & set2) / len(set1 | set2) * 100

# Similarities
sim_a = jaccard(user_a, festival)
sim_b = jaccard(user_b, festival)

print("User A Jaccard Similarity (%):", round(sim_a, 2))
print("User B Jaccard Similarity (%):", round(sim_b, 2))

# Dealbreakers
dealbreakers_a = user_a - festival
print("User A Dealbreaker Artists:", dealbreakers_a)