# 📊 Comparative Graph Analysis of Facebook and RoadNet-CA Networks

## 🧠 Project Overview
This project aims to perform a **comparative analysis of two large-scale networks**: the Facebook social network and the California road network (RoadNet-CA). These networks originate from entirely different domains—social connections versus physical infrastructure—and exhibit distinct structural properties.  

Using **Python** and the **NetworkX** library, we computed key graph metrics such as degree distribution, clustering coefficient, network density, diameter, connected components, and centrality measures. The analysis highlights how domain-specific constraints influence network structure, connectivity, and local community formation.  

The project provides hands-on experience in handling **large-scale graphs**, performing **unsupervised graph analysis**, generating **visualizations**, and interpreting quantitative results to understand the underlying topology of real-world networks.

---

## ⚙️ Tools and Libraries Used
- **Python 3**: Programming language for data processing and analysis.
- **NetworkX**: A library for network analysis, providing efficient algorithms for computing graph properties and structural statistics.
- **Matplotlib**: Used to generate visualizations such as degree distribution histograms.
- **Pandas**: Used for organizing and exporting results into CSV format for easy review.
- **OS, Time, Random**: Utility libraries for file handling, measuring computation time, and sampling large networks.

---

## 📈 Methodology
Each network was analyzed by loading its edge list into a NetworkX graph. We computed several key properties to understand both **local and global structural characteristics**:

1. **Degree and Degree Distribution**: Measures the number of edges per node. Degree distribution helps identify whether the network is homogeneous (most nodes have similar degrees) or heterogeneous (few nodes dominate connectivity as hubs). The formula used is:

   \[
   P(k) = \frac{N_k}{N}
   \]

   where \(N_k\) is the number of nodes with degree \(k\), and \(N\) is the total number of nodes.

2. **Clustering Coefficient**: Quantifies the likelihood of nodes forming tightly connected groups or triangles. Local clustering for node \(v\) is:

   \[
   C_v = \frac{2T(v)}{k_v(k_v-1)}
   \]

   where \(T(v)\) is the number of triangles through node \(v\) and \(k_v\) is its degree. The average clustering coefficient is the mean over all nodes. High clustering indicates strong local community structures.

3. **Centrality Measures**: Degree and betweenness centrality identify influential nodes. High degree centrality nodes have many connections, while high betweenness nodes serve as connectors along many shortest paths.

4. **Density and Diameter**: Density measures how close a network is to being fully connected:

   \[
   D = \frac{2E}{N(N-1)}
   \]

   Diameter measures the longest shortest path in the largest connected component, reflecting how “far apart” nodes can be.

5. **Connected Components and Triangles**: Components indicate network cohesion. Triangles represent local redundancy and clustering.

For **large networks** like RoadNet-CA, we used **sampling** or approximation techniques to compute metrics like diameter and clustering efficiently without excessive computation time.

---

## 📊 Experimental Results

The table below summarizes the key metrics computed for both networks:

| Metric | Facebook | RoadNet-CA |
|--------|-----------|------------|
| Nodes | 4,039 | 1,965,206 |
| Edges | 88,234 | 2,766,607 |
| Avg Degree | 43.7 | 2.8 |
| Density | 0.0108 | 0.0000014 |
| Clustering | 0.6055 | 0.0462 |
| Components | 1 | 2,642 |
| Diameter (approx) | 8 | ~800 |

**Interpretation:**

- The **Facebook network** is highly connected and forms a single large component, with a high clustering coefficient indicating strong community structures. Most nodes have a moderate number of connections, while a few nodes act as hubs, creating a long-tailed degree distribution.
- The **RoadNet-CA network** is sparse with very low density and clustering, reflecting physical constraints of road intersections. Its degree distribution is narrow, with most nodes having 2–3 connections, and multiple smaller disconnected components exist, especially in rural areas.

---

## 📈 Visualizations

### Facebook Degree Distribution
The histogram of node degrees shows a **heavy-tailed distribution**, typical of social networks. A small number of highly connected users (hubs) dominate the network, while most users maintain a moderate number of connections. This pattern demonstrates the **scale-free property** and aligns with the small-world phenomenon, where short paths exist between most nodes.

### RoadNet-CA Degree Distribution
The degree distribution is narrow and concentrated around 2–3 degrees, reflecting the **planar and uniform nature** of road networks. Unlike social networks, there are no dominant hubs, and connectivity is limited by geography. This results in long average path lengths and low local clustering.

---

## 🔍 Comparative Summary

The comparative analysis reveals clear differences between the two networks:

- **Connectivity:** Facebook is densely connected; RoadNet-CA is sparse and spatially constrained.
- **Local Clustering:** High in Facebook due to communities; low in RoadNet-CA because intersections rarely form triangles.
- **Diameter:** Small for Facebook (≈8), enabling rapid spread of information; large for RoadNet-CA (≈800), reflecting long travel paths.
- **Components:** Facebook forms a single giant component; RoadNet-CA contains thousands of smaller components in isolated regions.
- **Hubs:** Facebook has influential hub nodes; RoadNet-CA distributes connectivity uniformly.

**Key Insights:**
- Social networks evolve organically, promoting hubs, high clustering, and short paths.
- Road networks are constrained by physical layout, resulting in sparse connectivity, low clustering, and longer paths.
- Graph metrics and visualizations provide clear evidence of **domain-specific structural differences**.

---

## 💡 Learning Outcomes
1. Practical experience with **large-scale graph analysis** using NetworkX and Python.
2. Ability to compute and interpret multiple graph metrics including degree, clustering, centrality, density, and diameter.
3. Skills in **visualizing network properties** for clearer insight.
4. Understanding of **domain-specific structural patterns** in networks.
5. Experience in **handling computational challenges** for very large networks, including sampling and approximation.
6. Improved ability to document, reproduce, and present **quantitative findings** effectively.

---

## 📚 References
- SNAP Datasets: [https://snap.stanford.edu/data/](https://snap.stanford.edu/data/)  
- NetworkX Documentation: [https://networkx.org/documentation/stable/](https://networkx.org/documentation/stable/)  

---

**Author:** Raju Bandam  
**Course:** CS6010 — Network Analysis Project  
**Year:** 2025
