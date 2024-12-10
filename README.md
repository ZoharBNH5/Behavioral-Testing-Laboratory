# Behavioral Testing Laboratory

This repository contains code and data for analyzing behavioral experiments conducted in a laboratory setting. The experiments are designed to study and quantify various behavioral patterns, such as grooming, thigmotaxis, and others.

---

## 📁 Project Structure

### Folders and Files
- **`.idea/`**: IDE configuration files (e.g., PyCharm settings). Not essential for analysis.
- **`.history/`**: Temporary history files for the IDE (excluded from tracking).
- **Data Files (`.mat` files)**:
  - `.mat` files contain experimental data, labeled by date and experimental conditions.
- **Python Scripts**:
  - `corolation.py`: Script for comparing the results obtained this year to the results from 2022.
  - `grooming.py`: Script for analyzing grooming behavior.
  - `t_test.py`: Script for performing statistical t-tests on the data.
  - `thigmotaxis_all.py`: Script for analyzing thigmotaxis behavior across different conditions.
  - `txtfile.py`: Script for handling additional text-based data files.

---

## 🧪 Behavioral Metrics
This project analyzes several key behavioral metrics:
1. **Thigmotaxis**: Analysis of time spent in the periphery vs. the center of the arena.
2. **Grooming**: Quantification of grooming behavior over time.
3. **Correlation Analysis**: Investigating relationships between different experimental variables.
4. **Statistical Testing**: Applying t-tests to assess significant differences between experimental groups.

---

## 🔧 Requirements

Before running the code, ensure you have the following dependencies installed:
- Python 3.8 or later
- Required Python libraries:
  - `numpy`
  - `scipy`
  - `matplotlib`
  - `pandas`

You can install these using:
```bash
pip install numpy scipy matplotlib pandas
