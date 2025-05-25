# 🕸️ Web Scraping and Data Extraction Project

This project focuses on demonstrating various Python-based techniques for extracting and processing data from different sources using standard libraries and tools such as **pandas**, **camelot**, and **BeautifulSoup**.

---

## 📚 Objectives

The primary goal of this project is to:
- Understand and apply data extraction techniques from structured and semi-structured data formats.
- Utilize Python libraries for parsing CSV, HTML, and PDF files.
- Perform basic web scraping using BeautifulSoup and camelot.

---

## 🛠️ Tools and Technologies

| Tool/Library      | Purpose                                             |
|------------------|-----------------------------------------------------|
| `pandas`          | Reading and analyzing CSV and HTML table data       |
| `camelot`       | Extracting tabular data from PDF documents          |
| `BeautifulSoup`   | Parsing and scraping data from raw HTML content     |
| `requests`        | Sending HTTP requests to retrieve web page content  |

---

## 📄 Overview of Components

### ✅ `read_csv()` – Reading CSV Files

- **Definition**: A `pandas` method used to read comma-separated values (CSV) files and convert them into a DataFrame.
- **Purpose**: Useful for working with exported spreadsheets, datasets from public portals, and structured data.
- **Key Advantage**: Fast, efficient, and supports a wide range of options for delimiters, encodings, and missing values.

---

### ✅ `read_html()` – Extracting Tables from HTML Pages

- **Definition**: `pandas.read_html()` reads HTML documents and extracts `<table>` elements as DataFrames.
- **Use Case**: Useful for scraping structured data from websites such as Wikipedia, news sites, and government portals.
- **Note**: Automatically detects and reads tables but may struggle with dynamic content loaded by JavaScript.

---

### ✅ `read_pdf()` – Extracting Tables from PDFs (via `tabula-py`)

- **Definition**: `tabula.read_pdf()` reads tables from PDF documents and converts them into `pandas` DataFrames.
- **Requirement**: Java must be installed on the system.
- **Use Case**: Common in processing scanned reports, academic papers, and financial documents.
- **Limitation**: Works best with machine-generated (not scanned) PDFs and may require format consistency.

---

### ✅ `camelot` – Advanced Table Extraction from PDFs

- **Definition**: `camelot` is a Python library specifically designed to extract tables from PDFs using two parsing methods: `lattice` (for bordered tables) and `stream` (for whitespace-separated tables).
- **Advantage**: Unlike `tabula-py`, Camelot does not require Java and offers better control over layout detection.
- **Use Case**: Effective in processing structured, multi-column reports, and documents with consistent formatting.
- **Requirement**: Works only with text-based PDFs; image-based PDFs require OCR (e.g., Tesseract).

---

### ✅ `BeautifulSoup` – HTML Parsing and Web Scraping

- **Definition**: BeautifulSoup is a Python library used for navigating and extracting data from HTML and XML files.
- **Functionality**:
  - Parses web pages to extract specific elements like headings, links, paragraphs, images, etc.
  - Supports searching by tag, class, ID, attributes, and CSS selectors.
- **Use Case**: Best for semi-structured web content where structured tags exist but data is not in a table format.
- **Typical Workflow**:
  1. Fetch the web page using `requests`.
  2. Parse HTML with `BeautifulSoup`.
  3. Navigate and extract elements using tag-based logic.
