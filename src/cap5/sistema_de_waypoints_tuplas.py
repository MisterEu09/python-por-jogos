WAYPOINTS = (
    ("Vila Inicial", (50, 75)),
    ("Castelo Negro", (420, 300)),
    ("Caverna dos Segredos", (780, 150))
)


for nome, pos in WAYPOINTS:
    print(f"{nome}: x={pos[0]}, y={pos[1]}")
