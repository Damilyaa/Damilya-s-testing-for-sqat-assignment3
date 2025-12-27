# Damilya's Testing for SQAT Assignment 3

## About
This repository contains assignments for a Software Quality Assurance and Testing (SQAT) course, demonstrating error handling and testing methodologies across different software modules.

## Project Structure

```
.
├── test_tc-001.py            # Test for implicit wait
├── test_tc-002.py            # Test for explicit wait
├── test_tc-003.py            # Test for drag and drop
├── test_tc-004.py            # Test for hover
├── test_tc-005.py            # Test for dropdown by xpath
├── test_tc-006.py            # Test for dropdown by text
├── conftest.py               # configuring pytest
├── report.html               # test report
├── README.md                 # About the project
├── requirements.txt          # Python dependencies
└── venv/                     # Python virtual environment
```

## Quick Start

### Prerequisites
- Python 3.x installed

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Damilyaa/Damilya-s-testing-for-sqat-assignment3.git
   cd Damilya-s-testing-for-sqat-assignment2
   ```

2. **Set up virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

## Running Modules
Each module can be run independently:

```bash
# To run test
 pytest -v --html=report.html --self-contained-html
```
## Author
- Amangeldykyzy Damilya | SE-2327