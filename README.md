# Method

### 1. Virtual Python Environment

Set up of virtual environment for reproducibility and to ensure all relevant packages are available. Run the following **environment.sh** in a Virtual Studio Code Terminal (some steps are only necessary on macOS which is the operating system I am using). 

``` shell
#!/bin/sh

# Install system dependencies first (before building Python)
brew install openssl@3 readline sqlite3 xz zlib tcl-tk

# Install Python (must be *after* brew and export)
echo "Install Python:"
pyenv install 3.11.13

# Set global or local version
pyenv global 3.11.13
```

I then run 
```shell
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install dependencies inside venv
pip install --upgrade pip
pip install pandas matplotlib
```
inside the VS Code Terminal to create the virtual environment.

### 2. Data Access 

I tried to use the Python library ``wbdata`` to automate the access to the required World Bank datasets, but the library requires an OpenSSL version that I could not successfully install on my system.

Therefore, I resorted to downloading the datasets manually from https://databank.worldbank.org/source/ on July 27, 2025.

ChatGPT lead me to the databases 'World Development Indicators' and 'Environment' where I was able to download the required parameters as comma-separated values (CSVs).

### 3. Data Import and Plotting

Create a ``analysis.py`` python file that imports the World Bank data and plots it.

### 2. Analysis
# Method

### 1. Virtual Python Environment

Set up of virtual environment for reproducibility and to ensure all relevant packages are available. Run the following **environment.sh** in a Virtual Studio Code Terminal (some steps are only necessary on macOS which is the operating system I am using). 

``` shell
#!/bin/sh

# Install system dependencies first (before building Python)
brew install openssl@3 readline sqlite3 xz zlib tcl-tk

# Install Python (must be *after* brew and export)
echo "Install Python:"
pyenv install 3.11.13

# Set global or local version
pyenv global 3.11.13
```

I then run 
```shell
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install dependencies inside venv
pip install --upgrade pip
pip install pandas matplotlib
```
inside the VS Code Terminal to create the virtual environment.

### 2. Data Access 

I tried to use the Python library ``wbdata`` to automate the access to the required World Bank datasets, but the library requires an OpenSSL version that I could not successfully install on my system.

Therefore, I resorted to downloading the datasets manually from https://databank.worldbank.org/source/ on July 27, 2025.

ChatGPT lead me to the databases 'World Development Indicators' and 'Environment' where I was able to download the required parameters as comma-separated values (CSVs).

### 3. Data Import and Plotting

Create a ``analysis.py`` python file that imports the World Bank data and plots it.

### 2. Analysis