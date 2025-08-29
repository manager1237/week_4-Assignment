def main():
    # Ask user for filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: make all text uppercase)
        modified_content = content.upper()

        # Create a new file name
        new_filename = "modified_" + filename

        # Write modified content to the new file
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File successfully modified! Saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
