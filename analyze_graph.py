# analyze_graph.py
import os
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import time
import random

# -----------------------------
# Folder setup
# -----------------------------
DATA_DIR = "../data"
PLOTS_DIR = "../outputs/plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

# -----------------------------
# Graph analysis function
# -----------------------------
def analyze_graph(path, name, directed=False):
    print(f"\n=== Analyzing {name} ===")
    start_time = time.time()

    # Load graph
    print("Loading graph...")
    if directed:
        G = nx.read_edgelist(path, nodetype=int, create_using=nx.DiGraph())
    else:
        G = nx.read_edgelist(path, nodetype=int, create_using=nx.Graph())
    print(f"Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # Degree distribution
    degrees = [d for _, d in G.degree()]
    avg_degree = sum(degrees) / len(degrees)

    # Clustering coefficient
    if G.number_of_nodes() > 50000:
        sample_nodes = random.sample(list(G.nodes()), 10000)
        avg_clustering = nx.average_clustering(G, nodes=sample_nodes)
        clustering_vals = [nx.clustering(G, v) for v in sample_nodes]
    else:
        avg_clustering = nx.average_clustering(G)
        clustering_vals = list(nx.clustering(G).values())

    # Connected components
    num_components = nx.number_connected_components(G)
    components = [len(c) for c in nx.connected_components(G)]

    # Density
    density = nx.density(G)

    # Diameter (largest connected component)
    largest_cc_nodes = max(nx.connected_components(G), key=len)
    G_lcc = G.subgraph(largest_cc_nodes)
    if len(G_lcc) > 10000:
        nodes_sample = random.sample(list(G_lcc.nodes()), 1000)
        G_sample = G_lcc.subgraph(nodes_sample)
        try:
            diameter = nx.approximation.diameter(G_sample)
        except nx.NetworkXError:
            diameter = "Cannot compute (sample not connected)"
    else:
        diameter = nx.diameter(G_lcc)

    # Centrality measures
    deg_centrality = sum(nx.degree_centrality(G).values()) / len(G)
    if G.number_of_nodes() > 50000:
        bet_centrality = "Skipped (graph too large)"
    else:
        bet_centrality = sum(nx.betweenness_centrality(G, k=1000).values()) / len(G)

    # -----------------------------
    # Visualizations
    # -----------------------------

    # 1️⃣ Degree distribution
    plt.figure(figsize=(8, 5))
    plt.hist(degrees, bins=50, color='skyblue', edgecolor='black')
    plt.title(f"Degree Distribution - {name}")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(PLOTS_DIR, f"{name}_degree_distribution.png"))
    plt.close()

    # 2️⃣ Clustering coefficient distribution
    plt.figure(figsize=(8, 5))
    plt.hist(clustering_vals, bins=50, color='lightgreen', edgecolor='black')
    plt.title(f"Clustering Coefficient Distribution - {name}")
    plt.xlabel("Clustering Coefficient")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(PLOTS_DIR, f"{name}_clustering_distribution.png"))
    plt.close()

    # 3️⃣ Component size distribution
    plt.figure(figsize=(8, 5))
    plt.hist(components, bins=50, color='salmon', edgecolor='black')
    plt.title(f"Connected Component Size Distribution - {name}")
    plt.xlabel("Component Size (# of Nodes)")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(PLOTS_DIR, f"{name}_component_sizes.png"))
    plt.close()

    end_time = time.time()
    print(f"All plots saved for {name} in {PLOTS_DIR}")

    return {
        "Graph": name,
        "Nodes": G.number_of_nodes(),
        "Edges": G.number_of_edges(),
        "AvgDegree": avg_degree,
        "Clustering": avg_clustering,
        "Density": density,
        "Components": num_components,
        "Diameter": diameter,
        "AvgDegreeCentrality": deg_centrality,
        "AvgBetweenness": bet_centrality,
        "TimeSec": end_time - start_time
    }

# -----------------------------
# Main execution
# -----------------------------
if __name__ == "__main__":
    results = []
    results.append(analyze_graph("../data/facebook_combined.txt", "Facebook"))
    results.append(analyze_graph("../data/roadNet-CA.txt", "RoadNet_CA"))

    # Save results to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv("../outputs/results.csv", index=False)
    print("\nAll results saved to ../outputs/results.csv")

    # Comparison bar chart
    metrics_to_compare = ["AvgDegree", "Clustering", "Density"]
    comparison_df = results_df[["Graph"] + metrics_to_compare].set_index("Graph")
    comparison_df.plot(kind="bar", figsize=(8, 5), color=['skyblue', 'lightgreen', 'salmon'])
    plt.title("Network Comparison: Facebook vs RoadNet_CA")
    plt.ylabel("Metric Value")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "Network_Comparison_BarChart.png"))
    plt.close()

    print("Comparison bar chart saved to outputs/plots/Network_Comparison_BarChart.png")
