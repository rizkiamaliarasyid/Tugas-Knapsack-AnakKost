# ==========================================
# 0/1 Knapsack Dynamic Programming (DP)
# Studi Kasus: Anak Kost Belanja Bulanan
# Budget Maksimal = 300.000
# ==========================================

def knapsack_dp(items, budget):
    n = len(items)

    # dp[i][w] = skor maksimum dari i item pertama dengan budget w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # build table dp
    for i in range(1, n + 1):
        cost, score = items[i - 1][1], items[i - 1][2]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + score)
            else:
                dp[i][w] = dp[i - 1][w]

    # traceback untuk mencari item terpilih
    w = budget
    selected = []
    x = [0] * n  # vektor keputusan

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1])
            x[i - 1] = 1
            w -= items[i - 1][1]

    selected.reverse()

    max_score = dp[n][budget]
    total_cost = sum(item[1] for item in selected)

    return max_score, total_cost, selected, x


# ==========================================
# DATA ITEM (Nama, Biaya, Skor)
# ==========================================

items = [
    ("Beras", 75000, 85),            # x1
    ("Telur", 32000, 80),            # x2
    ("Ikan Kaleng", 42000, 78),      # x3
    ("Tempe", 15000, 55),            # x4
    ("Tahu", 18000, 50),             # x5
    ("Sayur", 30000, 70),            # x6
    ("Buah", 35000, 65),             # x7
    ("Susu SKM Sachet", 18000, 35),  # x8
    ("Mie Instan", 28000, 45),       # x9
    ("Minyak", 20000, 40),           # x10
    ("Vitamin C", 30000, 55),        # x11
    ("Snack Ringan", 22000, 42)      # x12
]

budget = 300000

# ==========================================
# RUN PROGRAM
# ==========================================

max_score, total_cost, selected_items, decision_vector = knapsack_dp(items, budget)

print("==========================================")
print("HASIL KNAPSACK DP (0/1)")
print("==========================================")
print("Budget Maksimal      :", budget)
print("Nilai Maksimum (Skor):", max_score)
print("Total Biaya Terpakai :", total_cost)
print("\nDaftar Item Terpilih:")
for name, cost, score in selected_items:
    print(f"- {name} | Biaya: {cost} | Skor: {score}")

print("\nVektor Keputusan x1-x12:")
print(decision_vector)
print("==========================================")





