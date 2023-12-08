from journal import Journal

def main():
    journal = Journal()
    while True:
        print("\nMy Journal")
        print("1. Write new entry")
        print("2. List all entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter your journal entry:\n")
            journal.add_entry(text)
            print("Entry added.")
        elif choice == "2":
            print("\nJournal Entries:")
            print(journal.list_entries())
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
