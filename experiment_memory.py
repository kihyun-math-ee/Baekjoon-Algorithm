"""
Topic: Python Memory Management Experiment
Focus: Reference (Aliasing) vs. Shallow Copy vs. Rebinding
Date: 2026-02-06
"""

# ==========================================
# Experiment 1: Mutable Object (List)
# ==========================================
print("--- Experiment 1: List (Mutable) ---")

list_A = [1, 2, 3]
list_B = list_A        # Aliasing: Copies the reference (address), not the data.
list_C = list_A[:]     # Shallow Copy: Creates a new object with the same data.

# Modification
list_A[0] = 999        # Modifying the object directly affects all aliases.

print(f"Original(A): {list_A}")
print(f"Alias(B)   : {list_B}")  # Expected: [999, 2, 3] (Changed)
print(f"Copy(C)    : {list_C}")  # Expected: [1, 2, 3] (Unchanged)


# ==========================================
# Experiment 2: Immutable Object (Integer)
# ==========================================
print("\n--- Experiment 2: Integer (Immutable) ---")

num_A = 10
num_B = num_A          # Both point to the same '10' object.

# Rebinding
num_A = 20             # Creates a NEW '20' object. num_A now points to '20'.
                       # num_B still points to the original '10' object.

print(f"Original(A): {num_A}")   # Expected: 20
print(f"Alias(B)   : {num_B}")   # Expected: 10 (Independent)
