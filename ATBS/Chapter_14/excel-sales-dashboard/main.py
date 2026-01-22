from openpyxl import Workbook


def main() -> None:
    # Create a new Excel workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Budget"

    # Header row
    ws.append(["Item", "Category", "Cost (€)"])

    # Simple data (you can edit these later)
    rows = [
        ("Coffee", "Food", 3.50),
        ("Bus ticket", "Transport", 1.20),
        ("Notebook", "Study", 4.80),
        ("Sandwich", "Food", 5.10),
        ("Phone top-up", "Bills", 10.00),
    ]

    for item, category, cost in rows:
        ws.append([item, category, cost])

    # Calculate total in Python (beginner-friendly)
    total = sum(cost for _, _, cost in rows)

    # Add an empty row + total row
    ws.append([])
    ws.append(["TOTAL", "", total])

    # Save the workbook
    wb.save("mini_budget.xlsx")
    print("Saved: mini_budget.xlsx")


if __name__ == "__main__":
    main()