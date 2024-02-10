def count_notes(amount):
    denominations = [100, 50, 20, 10, 5]
    notes_count = {}

    for denomination in denominations:
        count = amount // denomination
        amount %= denomination
        notes_count[denomination] = count

    return notes_count

def main():
    try:
        amount = int(input("Enter the amount: "))
        notes_count = count_notes(amount)

        print("Number of notes needed:")
        for denomination, count in notes_count.items():
            if count > 0:
                print(f"{denomination} note: {count}")

    except ValueError:
        print("Invalid input. Please enter a valid amount.")

if __name__ == "__main__":
    main()
