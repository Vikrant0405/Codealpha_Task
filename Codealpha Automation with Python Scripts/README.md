# 📧 Email Extractor

A simple Python application that extracts all email addresses from a selected text file and saves the unique email addresses into a new file (`emails.txt`).

## 🚀 Features

- 📂 File selection using a graphical file picker.
- 🔍 Extracts email addresses using Regular Expressions (Regex).
- 🧹 Removes duplicate email addresses automatically.
- 📄 Saves extracted emails to a text file.
- 📋 Displays all extracted emails in the console.
- ⚠️ Handles file errors gracefully.

---

## 🛠️ Technologies Used

- Python 3.x
- Regular Expressions (`re`)
- Tkinter (File Dialog)

---

## 📁 Project Structure

```
Email_Extractor/
│
├── email_extractor.py      # Main Python program
├── emails.txt              # Output file (generated automatically)
├── README.md               # Project documentation
```

---

## 📦 Requirements

Python 3.x

Tkinter is included with most Python installations.

No external libraries are required.

---

## ▶️ How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/Email_Extractor.git
```

### Step 2: Navigate to the project folder

```bash
cd Email_Extractor
```

### Step 3: Run the program

```bash
python email_extractor.py
```

---

## 📂 Supported File Types

The file picker allows selecting:

- TXT
- CSV
- XLSX
- XLS
- DOCX
- PDF
- All Files

> **Note:** The current version reads text files (`.txt`) correctly. Other file types can be selected, but additional libraries are required to extract text from them.

Examples:

- PDF → `PyPDF2` or `pdfplumber`
- DOCX → `python-docx`
- Excel → `pandas` or `openpyxl`

---

## 📸 Working

1. Run the program.
2. Select a file using the file picker.
3. The program scans the file.
4. All email addresses are extracted.
5. Duplicate emails are removed.
6. The unique email addresses are displayed.
7. The emails are saved in `emails.txt`.

---

## 📝 Example

### Input (`sample.txt`)

```
Contact us at support@example.com

Sales: sales@example.com

support@example.com

info@test.org
```

### Console Output

```
1. info@test.org
2. sales@example.com
3. support@example.com

3 email(s) saved to 'emails.txt'
```

### Output (`emails.txt`)

```
info@test.org
sales@example.com
support@example.com
```

---

## ⚙️ How It Works

The program uses the following Regular Expression:

```python
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

This pattern matches most standard email formats.

---

## 🔮 Future Improvements

- Support extracting text directly from PDF files.
- Support Microsoft Word (.docx).
- Support Excel (.xlsx and .xls).
- Drag-and-drop file selection.
- GUI interface.
- Export to CSV or Excel.
- Progress bar for large files.

---

## 👨‍💻 Author

**Vikrant Hanumant Kharke**

B.Sc. Computer Science

Python Developer

GitHub: https://github.com/Vikrant0405

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub and feel free to contribute!