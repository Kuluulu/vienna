# Method

The repository is available under [Link to Repository](https://github.com/Kuluulu/vienna).

### 1. Git Repository and Virtual Python Environment Generation

Set up of a GitHub repository and a local virtual environment for reproducibility and to ensure all relevant packages are available. Run the following **environment.sh** in a Virtual Studio Code Terminal (some steps are only necessary on macOS which is the operating system I am using). 

``` shell
#!/bin/sh

# Install Python
echo "Install Python:"
pyenv install 3.11.13

# Set global or local version
pyenv global 3.11.13
```

Then run 
```shell
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install dependencies inside venv
pip install --upgrade pip
pip install pandas matplotlib
```
inside the VS Code Terminal to create the virtual environment to work in.

### 2. Data Access 

After some attempts to use the Python library ``wbdata`` to automate accessing the required World Bank datasets (the library requires an OpenSSL version that I could not successfully access through the python installation on my system), I resorted to downloading the datasets manually from [https://databank.worldbank.org/source/](https://databank.worldbank.org/source/) on July 27, 2025.

OpenAI's ChatGPT quickly leads to the relevant databases, namely 'World Development Indicators' and 'Environment', which I downloaded the required parameters of as comma-separated values (CSVs). The files, including the associated metadata, were added to the repository input folder.

The GDP per capita data was available with different currency options. I selected the "current US$" option, which introduces uncertainty associated to currency exchange but enables direct comparison of the two countries.

### 3. Data Import and Plotting

Create an ``analysis.py`` python file that imports the World Bank data and plots it. Run this using ``python analysis.py``. Files are written to an ``output`` folder.

### 4. Discussion

Write ``discussion.md`` and convert Markdown file into PDF using the VS Code extension "Markdown PDF".