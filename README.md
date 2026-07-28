# Tire Volume Calculator

A Python application that calculates the approximate volume of a tire using its width, aspect ratio, and wheel diameter. The application also records customer inquiries for future follow-up, demonstrating both programming fundamentals and practical business thinking.

---

## Business Problem

Tire retailers and automotive service centers often need to estimate tire volume for inventory planning, transportation, and storage. They also need a simple way to record customers who express interest in purchasing tires.

Performing these calculations manually is time-consuming and increases the chance of errors. Businesses also risk losing potential sales if customer inquiries are not recorded.

---

## Solution

This application automates the tire volume calculation using the standard mathematical formula. It also allows interested customers to leave their phone numbers, which are saved together with the tire specifications and the date of the inquiry for future follow-up.

---

## Features

- Calculate tire volume from user input
- Uses the Python `math` module for calculations
- Records the current date automatically
- Saves calculations to a text file
- Collects customer phone numbers
- Uses functions for code organization
- Includes exception handling for invalid input
- Uses Python's main guard (`if __name__ == "__main__":`)

---

## Technologies Used

- Python 3
- Math Module
- Datetime Module
- File Handling
- Exception Handling

---

## Skills Demonstrated

- Python Programming
- Function Design
- Mathematical Calculations
- File Input/Output (I/O)
- Error Handling
- User Input Validation
- Problem Solving
- Clean Code Organization

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/yourusername/tire-volume-calculator.git
```

2. Navigate to the project folder.

```bash
cd tire-volume-calculator
```

3. Run the program.

```bash
python tire_volume.py
```

---

## Example Output

```
Enter the width of the tire in mm (ex 205): 205
Enter the aspect ratio of the tire (ex 60): 60
Enter the diameter of the wheel in inches (ex 15): 15

The approximate volume is 39.92 litres

Would you like to buy tires with the dimensions that you have entered? Yes
Please provide us with your phone number:
```

---

## Future Improvements

- Store customer information in an SQLite database
- Build a graphical user interface using PySide6
- Display tire prices
- Search previous customer records
- Generate quotations and receipts
- Connect to an online product inventory
- Add automated unit testing with `pytest`

---

## Lessons Learned

Through this project I learned how to:

- Organize a Python program using functions
- Import and use Python modules
- Perform mathematical calculations
- Handle user input safely
- Save data to a file
- Implement exception handling
- Build a small application that solves a real business problem

---

## About Me

I am an aspiring Software Developer with a background in Strategic Management and Corporate Governance. I enjoy developing software solutions that combine business value with technology. I am currently expanding my skills in Python, SQL, web development, and data analysis while building practical projects for my portfolio.

---

## Author

**Rufaro Chirume**

GitHub: https://github.com/ruffych594
