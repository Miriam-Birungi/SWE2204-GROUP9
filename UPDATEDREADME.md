# Software Metrics: Measuring Structural Complexity

This repository contains information and examples related to measuring the structural complexity of software, specifically focusing on control-flow aspects. It's based on materials from a Software Metrics course.

## Contents

* **Software Structural Measurement:**
    * Control-flow structure
    * Structural complexity: cyclomatic complexity
    * Data flow and data structure attributes
* **Architectural Measurement** [cite: 8, 9, 10, 11, 12]

## Software Complexity Metrics

The repository explores various software complexity metrics, including those related to code and architecture:

* **Code Complexity Metrics:**
    * Depth of nesting
    * Cyclomatic complexity
    * Information flow complexity
    * Data structure complexity [cite: 8, 9, 10, 11, 12]
* **Architectural Complexity Metrics:**
    * Morphological measures (cohesion, coupling) [cite: 8, 9, 10, 11, 12]

## Control-Flow Structure

###   How to Represent Program Structure

Software structure can be represented by three attributes:

* **Control-flow structure:** The sequence of execution of instructions in a program. [cite: 10, 11, 12]
* **Data flow:** How data is created and handled by the program. [cite: 10, 11, 12]
* **Data structure:** The organization of the data itself. [cite: 10, 11, 12]

###   Key Concepts

* **Basic Control Structures (BCS):** Fundamental control-flow mechanisms. [cite: 16, 17, 18, 19]
    * **Types:** Sequence, Selection (e.g., if-then-else), Iteration (e.g., loops). [cite: 16, 17, 18, 19]
    * **Advanced BCS:** Procedure/function calls, Recursion, Interrupts, Concurrence. [cite: 19]
* **Control Flow Graph (CFG):** A directed graph representing program control flow. [cite: 20, 21, 22, 23, 24]
    * Nodes represent program statements. [cite: 20, 21, 22, 23, 24]
    * Directed arcs indicate the flow of control. [cite: 20, 21, 22, 23, 24]
    * Special nodes: Procedure nodes, Predicate nodes, Start node, Terminal (end) nodes. [cite: 22, 23, 24]
* **Finite-State Machine (FSM):** A model for CFG that explicitly shows control transfer. [cite: 27, 28, 29, 30]
* **Prime Flow Graphs:** Flow graphs that cannot be decomposed non-trivially by sequencing and nesting. [cite: 33, 34]
    * Examples: Sequence of statements, if-condition, if-then-else, while-loop, repeat-loop, case. [cite: 34]
* **Sequencing and Nesting:** Operations to combine flowgraphs. [cite: 35, 36, 37, 38]
    * **Sequence:** Merging the terminal node of one flowgraph with the start node of another. [cite: 35, 36]
    * **Nesting:** Replacing an arc in one flowgraph with another flowgraph. [cite: 37, 38]
* **S-Structured Graph:** A flowgraph constructed by recursively sequencing and nesting prime flowgraphs. [cite: 39, 40, 41, 42]
    * Example: D-structured graphs using sequence, if-conditions, and while-loops. [cite: 42]
* **Prime Decomposition:** Unique decomposition of any flow graph into a hierarchy of sequencing and nesting primes. [cite: 43, 44]

##   Complexity Metrics

###   Depth of Nesting

* Measures the nesting levels within a flowgraph. [cite: 46, 47, 48]
* Lower depth generally indicates less complexity. [cite: 48]
* Formulas are provided in the document to calculate nesting depth for primes, sequences, and nesting. [cite: 46, 47]

###   Cyclomatic Complexity

* Measures program complexity using the cyclomatic number of the program's flowgraph. [cite: 50, 51, 52, 53]
* Calculated in two ways:
    * **Flowgraph-based:** v(G) = e - n + 2p  (where e is the number of edges, n is the number of nodes, and p is the number of connected components). [cite: 52]
    * **Code-based:** v(G) = 1 + d (where d is the number of predicate nodes). [cite: 53]
* Examples are provided in the document. [cite: 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]

###   Cyclomatic Complexity:  Considerations

* **Advantages:** Objective measurement. [cite: 85]
* **Disadvantages:**
    * Limited to component level. [cite: 85]
    * Programs with the same complexity number may have different programming effort. [cite: 85]
    * Same requirements can be programmed with different complexities. [cite: 85]
    * Requires complete design or code visibility. [cite: 85]

##   Software Architecture

###   Representation

* A software system can be represented as a graph S = {N, R}. [cite: 86, 87]
    * Nodes (N) correspond to subsystems. [cite: 86, 87]
    * Edges (R) represent relationships between subsystems. [cite: 86, 87]

###   Morphology

* Refers to the overall shape of the software architecture. [cite: 88, 89, 90]
* Characterized by:
    * Size (nodes and edges) [cite: 89, 90]
    * Depth (longest path from root to leaf) [cite: 89, 90]
    * Width (number of nodes at any level) [cite: 89, 90]
    * Edge-to-node ratio (connectivity density) [cite: 89, 90]
* Example provided. [cite: 90]

###   Tree Impurity

* Measures how much a graph differs from a tree structure. [cite: 91, 92]
* Smaller values indicate a better design. [cite: 91, 92]
* Formula and examples are given. [cite: 92]

##   Cohesion

###   Components and Modules

* A module/component is a bounded sequence of program statements with an aggregate identifier. [cite: 94, 95, 96, 97, 98, 99, 100]
* Properties:
    * Nearly-decomposability: High ratio of intra-module to extra-module communication. [cite: 95, 96]
    * Compilability:  Should be separately compilable. [cite: 96]
* Modular/component-based systems are partitioned into components with relationships between them. [cite: 97, 98, 99, 100]
* Represented by a graph S = {C, Re} where C is the set of components and Re is the set of relationships. [cite: 99, 100]
* Code complexity of a component-based system is the sum of the cyclomatic complexities of its components. [cite: 101]

###   Cohesion (Concept)

* Describes how strongly related responsibilities are among design elements. [cite: 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
* Goal: High cohesion (highly related responsibilities within a class). [cite: 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
* Cohesion of a module: Extent to which its components are needed to perform a task. [cite: 103, 104, 105]
* Types of cohesion (from high to low): Functional, Sequential, Communicative, Procedural, Temporal, Logical, Coincidental. [cite: 104, 105, 106]
* Cohesion for a component is the ratio of internal relationships to the total number of relationships. [cite: 108, 109, 113, 114]
* System cohesion is the average cohesion of all components. [cite: 110, 111, 112, 115, 116]
* Examples are provided. [cite: 106, 113, 114, 115, 116]

##   Coupling

###   Coupling (Concept)

* Describes how strongly one element relates to another. [cite: 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]
* Goal: Loose coupling (small, direct, visible, and flexible relations). [cite: 118, 120]
* Package dependencies should be minimized and follow layering conventions. [cite: 119]
* Class relationships should also strive for loose coupling. [cite: 120]

###   Coupling (Types)

* Various types of coupling (from least to most coupled):
    * R0: Independence (no communication) [cite: 121, 122, 123]
    * R1: Data coupling (communication via parameters) [cite: 121, 122, 123]
    * R2: Stamp coupling (modules use the same record type) [cite: 121, 122, 123]
    * R3: Control coupling (one module controls the behavior of another) [cite: 121, 122, 123]
    * R4: Content coupling (one module refers to the internals of another) [cite: 121, 122, 123]
* No standard measurement exists. [cite: 123]

###   Coupling in Component-Based Systems

* Coupling of a component is the ratio of external relations to the total number of relations. [cite: 124, 125, 129]
* System coupling is the average coupling of all components. [cite: 126, 127, 128, 130, 131]
* Examples are provided. [cite: 129, 130, 131]

###   Coupling (Representation)

* Graph representation is used. [cite: 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142]
* Coupling between modules x and y is a function of the worst coupling relation and the number of interconnections. [cite: 132]
* Global coupling of a system is the median value of all module couplings. [cite: 133, 134, 135, 136, 137, 138]
* An example is provided to demonstrate the calculation. [cite: 139, 140, 141, 142]

##   Other Structural Metrics

###   Information Flow Measures

* Information flow is measured by fan-in and fan-out. [cite: 144, 145, 146, 147]
    * **Fan-in:** Number of flows terminating at a module + number of data structures from which info is retrieved. [cite: 145]
    * **Fan-out:** Number of flows starting at a module + number of data structures updated by the module. [cite: 145]
* Information Flow Complexity (IFC) metrics are presented. [cite: 146]
* An example is provided. [cite: 147]
* Revisions to the Henry-Kafura IFC measure are listed. [cite: 148, 149, 150, 151]

###   Data Structure Measurement

* There's a trade-off between control-flow and data structure complexity. [cite: 152, 153, 154, 155, 156, 157]
* Higher cyclomatic complexity often implies less complex data structures. [cite: 153, 156]
* A simple example for data structure measurement is provided, considering integers, strings, and arrays. [cite: 154]
* Example 3B illustrates calculating data structure complexity for two programs. [cite: 155, 156, 157]

##   Conclusion

The document provides an overview of various complexity metrics for software, covering both code and architectural aspects. These metrics help in quantifying and understanding different attributes of software complexity, which is crucial for software design, development, and maintenance. [cite: 158]
