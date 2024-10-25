# LIS Algorithms Analysis and Performance Study

This repository contains a Python project that focuses on analyzing and comparing different algorithms for solving the Longest Increasing Subsequence (LIS) problem. The project includes implementations of various algorithms, performance comparisons, and a detailed report documenting the results, highlighting their practical implications in real-world applications, such as blockchain transaction validation.

## Project Structure

```
lis-study/
├── .gitignore                     # Specifies files and directories to ignore in version control.
├── README.md                      # Documentation for this project.
├── lis_n_squared.py               # Python script implementing the O(n^2) approach for LIS calculation.
├── lis_nlogn.py                   # Python script implementing the O(n log n) optimized LIS calculation.
├── algo_analysis.py               # Python module for analyzing and comparing LIS algorithms.
├── algo_analysis_detailed.py      # Additional detailed analysis functions and comparisons for LIS.
├── complexity_comparison.png      # Graphical visualization comparing the time complexity of different algorithms.
├── paper.pdf                      # PDF report documenting the findings and analysis.
```

## Getting Started

### Prerequisites

- Python 3.x is required for running the scripts.
- It is recommended to create a virtual environment to manage dependencies.

### Installation

1. **Clone the Repository**
   
   ```bash
   git clone git@github.com:mascarock/lis-study.git
   cd lis-study
   ```

2. **Create and Activate a Virtual Environment**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   
   If a `requirements.txt` file is provided (create one if needed):

   ```bash
   pip install -r requirements.txt
   ```

## Running the Analysis

- **`lis_n_squared.py`**: To run the O(n^2) LIS analysis, execute:
  
  ```bash
  python lis_n_squared.py
  ```

- **`lis_nlogn.py`**: To run the optimized O(n log n) LIS analysis:
  
  ```bash
  python lis_nlogn.py
  ```

- **`algo_analysis.py`**: To run the comparison analysis between the O(n^2) and O(n log n) approaches:
  
  ```bash
  python algo_analysis.py
  ```

- **`algo_analysis_detailed.py`**: To conduct detailed testing and performance analysis on various input types:
  
  ```bash
  python algo_analysis_detailed.py
  ```

## Outputs

- **Complexity Graph**: The file `complexity_comparison.png` provides a visualization comparing the time complexities of different LIS algorithms.
- **Report**: The detailed analysis can be found in `paper.pdf`.

## Files Overview

- **`lis_n_squared.py`**: Contains the traditional **O(n^2)** dynamic programming approach to solve the LIS problem.
- **`lis_nlogn.py`**: Implements an optimized **O(n log n)** solution using binary search for efficient LIS computation.
- **`algo_analysis.py`**: Includes both LIS approaches and compares their performance on different input sizes, generating a time complexity graph.
- **`algo_analysis_detailed.py`**: Tests both algorithms on various types of input (random, sorted, reversed, etc.) and provides detailed logging and analysis.
- **`paper.pdf`**: This PDF report provides a comprehensive overview of the findings, detailing the differences in time complexity, practical applications, and implications of using different LIS algorithms.
- **`complexity_comparison.png`**: A graph depicting the comparison of different LIS algorithms, providing insights into their performance characteristics.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please reach out to **Niccolò Mascaro** at [n.mascaro@gmx.com](mailto:n.mascaro@gmx.com).

