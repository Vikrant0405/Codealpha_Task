import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename


OUTPUT_FILE = "emails.txt"

EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

        emails = re.findall(EMAIL_PATTERN, content)

        # Remove duplicates
        unique_emails = sorted(set(emails))

        return unique_emails

    except FileNotFoundError:
        print(f"❌ Error: '{input_file}' not found.")
        return []

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return []


def save_emails(emails, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")

        print(f"\n✅ {len(emails)} email(s) saved to '{output_file}'")

    except Exception as e:
        print(f"❌ Error saving file: {e}")
        

def select_file ():
    Tk().withdraw()  # Hide the main window

    file_path = askopenfilename(
        title="Select a file",
        filetypes=[
            ("Supported Files", "*.txt *.csv *.xlsx *.xls *.docx *.pdf"),
            ("All Files", "*.*")
        ]
    )

    return file_path


def main():
    print("=" * 50)
    print("EMAIL EXTRACTOR".center(50))
    print("=" * 50)
    INPUT_FILE = select_file()
    emails = extract_emails(INPUT_FILE)

    if emails:
        print("\n📧 Emails Found:\n")
        for i, email in enumerate(emails, start=1):
            print(f"{i}. {email}")

        save_emails(emails, OUTPUT_FILE)

    else:
        print("\n⚠️ No email addresses found.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.bye! 👋")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
     