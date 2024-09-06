import plotly.graph_objects as go
import plotly.io as pio

# Define vertices for a 3D hypercube (inner and outer cubes)
vertices = [
    [1, 1, 1],  # A (0100)
    [1, 1, -1], # B (0101)
    [1, -1, 1], # C (0100)
    [1, -1, -1],# D (0100)
    [-1, 1, 1], # E (0100)
    [-1, 1, -1],# F (1000)
    [-1, -1, 1],# G (1001)
    [-1, -1, -1]# H (0100)
]

# Corresponding binary values for each vertex (4-bit)
binary_values = ['0100', '0101', '0100', '0100', '0100', '1000', '1001', '0100']

# XOR combinations to create 8-bit binary for "HYDRA"
xor_combinations = [
    ('0100', '1000', '01001000', 'H'), # A XOR F -> H
    ('0101', '1001', '01011001', 'Y'), # B XOR G -> Y
    ('0100', '0100', '01000100', 'D'), # C XOR H -> D
    ('0100', '0010', '01010010', 'R'), # D XOR I -> R
    ('0100', '0001', '01000001', 'A')  # E XOR J -> A
]

# Define edges for the hypercube
edges = [
    [0, 1], [0, 2], [0, 4],
    [1, 3], [1, 5],
    [2, 3], [2, 6],
    [3, 7],
    [4, 5], [4, 6],
    [5, 7],
    [6, 7]
]

# Create a list of lines to be plotted
lines = []
for edge in edges:
    x0, y0, z0 = vertices[edge[0]]
    x1, y1, z1 = vertices[edge[1]]
    lines.append(go.Scatter3d(x=[x0, x1], y=[y0, y1], z=[z0, z1], mode='lines', line=dict(color='blue', width=2)))

# Add vertices to the plot
vertex_trace = go.Scatter3d(
    x=[v[0] for v in vertices],
    y=[v[1] for v in vertices],
    z=[v[2] for v in vertices],
    mode='markers+text',
    text=[f'{bin} ({v[0]}, {v[1]}, {v[2]})' for bin, v in zip(binary_values, vertices)],
    textposition='top center',
    marker=dict(size=5, color='red'),
)

# Create XOR operation transitions as text points
xor_texts = go.Scatter3d(
    x=[0, 0, 0, 0, 0],  # Positioned along the X-axis or adjusted accordingly
    y=[2, 2.5, 3, 3.5, 4],  # Positioned along the Y-axis or adjusted accordingly
    z=[2, 2.5, 3, 3.5, 4],  # Positioned along the Z-axis or adjusted accordingly
    mode='text',
    text=[f'XOR: {bin1} XOR {bin2} = {result_bin} ({char})' for bin1, bin2, result_bin, char in xor_combinations],
    textposition='middle center',
)

# Create the figure and plot
fig = go.Figure(data=[vertex_trace] + lines + [xor_texts])
fig.update_layout(
    title='3D Hypercube Visualization with XOR Operations for "HYDRA"',
    scene=dict(
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis'),
        zaxis=dict(title='Z-axis')
    )
)

# Save as HTML file in shared storage so Firebase can access it
output_path = '/data/data/com.termux/files/home/storage/shared/hypercube_theory.html'  # Adjust this to your shared storage location
pio.write_html(fig, file=output_path, auto_open=False)


