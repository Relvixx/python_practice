# 1. We create a list of dictionaries to hold our data
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 95},
    {"name": "Ethan", "score": 88},
    {"name": "Fiona", "score": 91}
]

# 2. Sort the list by score in descending order
# 'key' tells Python to look at the 'score' inside each dictionary
# 'reverse=True' makes it go from High to Low
students.sort(key=lambda x: x['score'], reverse=True)

print("--- Top 3 Students ---")

# 3. Use a for loop with a range to get the first 3
for i in range(3):
    student = students[i]
    name = student["name"]
    score = student["score"]
    
    print(f"{i+1}. {name}: {score} - Topper!")