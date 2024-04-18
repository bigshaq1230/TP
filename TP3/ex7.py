N_max = 10

# Initialize m1 and m2
m1 = [[0] * N_max for _ in range(N_max)]
m2 = [[0] * N_max for _ in range(N_max)]

# Assign values to m1
for i in range(N_max):
    for j in range(N_max):
        m1[i][j] = 2 + i * N_max + j * 2

# Assign values to m2 (unit matrix)
for i in range(N_max):
    m2[i][i] = 1

# Initialize m3 with zeros
m3 = [[0] * N_max for _ in range(N_max)]

# Calculate m3 = m1 - m2
for i in range(N_max):
    for j in range(N_max):
        m3[i][j] = m1[i][j] - m2[i][j]

# Print m3
for row in m3:
    print(row)
