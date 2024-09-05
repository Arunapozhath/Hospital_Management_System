# Pharmacy Management System

## Overview

This is a Graphical User Interface (GUI) application developed using the Tkinter library in Python. The Pharmacy Management System provides a comprehensive solution for managing various aspects of a pharmacy, including patient registration, hospital management, doctor appointments, and medicine stock. It features a clean and responsive GUI and robust backend integration for seamless operation.

## Key Features

- **Medicine Inventory Management**: Track and manage medicine details, including name, manufacturer, quantity, expiry date, and price.
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations for managing medicines in the database.
- **Database Integration**: Utilizes SQLite for backend database management. Automatically creates and updates the database as necessary.
- **User Interface**: A clean and responsive GUI for easy interaction, featuring input forms, buttons for various operations, and a tree view for displaying records.
- **Error Handling**: Robust error and exception handling to ensure smooth operation.

## Technology Stack

- **Frontend**: Tkinter for building the user interface.
- **Backend**: SQLite for storing and managing data.

## Technical Details

- **Widgets Used**: Labels, entries, buttons, frames, text boxes, comboboxes.
- **Event Handling**: Functions to handle button clicks, text entries, and window events.
- **Date and Time**: Utilizes `datetime` module to fetch current date and time.
- **Randomization**: Uses `random` module to generate reference numbers for patient registration.
- **Messaging**: `messagebox` module to display notifications to users.
- **Database Operations**: 
  - Connects to the SQLite database using methods such as `connect`, `commit`, and `close`.
  - Executes SQL queries using `execute` and fetches data with `fetchall`.
  - Manages data insertion, deletion, and table creation.
  - Employs primary key and auto-increment for unique identifiers.
  - Uses constraints like `not null` and data types like `date` and `real`.

## GUI Layout

- **Grid and Pack Methods**: Arranges widgets in a grid-like or packing-like manner.
- **Widget Customization**: Customizes appearance with attributes like `width`, `font`, `bd`, `relief`, `bg`, `padx`, `pady`, and `sticky`.
- **Comboboxes**: Created with the `ttk` module for hospital codes, lot numbers, and storage advice.

## Functions

- **Prescription Management**: Functions such as `prescriptionfunc` and `prescriptiondatafunc` for prescription generation and data storage.
- **Doctor Management**: Functions include `add_doctor`, `Display_data`, `Clear_data`, `delete_data`, and `exit_app`.
- **Medicine Management**: Functions include `add_medicine`, `display_data`, `clear_data`, `delete_medicine`, and `exit_app`.
- **Window Controls**: Functions to handle exits, resets, and re-initializations like `exit`, `reset`, and `reesetbtt`.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/pharmacy-management-system.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd pharmacy-management-system
   ```
3. **Install Dependencies**:
   Ensure you have Python installed. Tkinter is included with most Python installations.

4. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage

1. Launch the application and log in with valid credentials.
2. Navigate through different windows to manage patients, hospital details, doctor appointments, and medicine stock.
3. Use the registration window to add new users.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with proposed changes.

## License

This project is based on a tutorial by (http://www.youtube.com/@TechieCoder). 

The original code and tutorial are provided for educational purposes only. Please refer to the original YouTube video for more information on usage rights and licensing: (http://www.youtube.com/@TechieCoder).

**Note**: The creator of the original video holds all rights to the content presented in the tutorial. This repository is provided for educational and personal use, and any commercial use or redistribution should be done with permission from the original creator.


## Contact

For any questions or feedback, please reach out to [arunavizhakkatt@gmail.com].
