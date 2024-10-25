# LIS Study - Code Challenge

This repository contains a Python project that focuses on analyzing and comparing different algorithms for solving the Longest Increasing Subsequence (LIS) problem. The project includes implementations of various algorithms, performance comparisons, and a detailed report documenting the results.

## Project Structure

```
code-challenge/
├── .gitignore                     # Specifies files and directories to ignore in version control.
├── README.md                      # Documentation for this project.
├── algoanalysis.py                # Python module for performing analysis on LIS algorithms.
├── algoanalysis2.py               # Additional analysis functions and comparisons for LIS.
├── main.py                        # Main entry point for running the LIS analysis.
├── main2.py                       # Alternative script for running additional analysis.
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
   cd code-challenge
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

- **`main.py`**: To run the main LIS analysis, execute:
  
  ```bash
  python main.py
  ```

- **`main2.py`**: To run an alternative version of the LIS analysis:
  
  ```bash
  python main2.py
  ```

## Outputs

- **Complexity Graph**: The file `complexity_comparison.png` provides a visualization comparing the time complexities of different LIS algorithms.
- **Report**: The detailed analysis can be found in `paper.pdf`.

## Files Overview

- **`algoanalysis.py` and `algoanalysis2.py`**: These modules contain different implementations and variations of LIS algorithms, allowing a comparison of their performance and behavior on various input datasets.
- **`main.py` and `main2.py`**: These scripts serve as entry points to execute the analyses, utilizing the algorithms provided in `algoanalysis.py` and `algoanalysis2.py`.
- **`paper.pdf`**: This PDF is a comprehensive report of the findings, detailing the results of the algorithmic analysis.
- **`complexity_comparison.png`**: A graph depicting the comparison of different LIS algorithms, providing insights into their performance characteristics.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please reach out to **Niccolò Mascaro** at [n.mascaro@gmx.com](mailto:n.mascaro@gmx.com).

