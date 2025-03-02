GYM MANAGEMENT SYSTEM
A simple Gym Management System built using Python and Tkinter for GUI. This application allows gym administrators to manage members, calculate membership prices, and view member details in a table.

FEATURES

Add Members: Add new gym members with their name, phone number, gender, and selected plan.

Calculate Price: Automatically calculate the price of the selected gym plan.

View Members: Display all members in a table with their details.


Plans Available:

Zumba: ₹500/month

Cardio: ₹500/month

Weightlifting: ₹1000/month

All of Them: ₹1500/month


FILE STRUCTURE

The project is organized into multiple files for better maintainability:

Copy
gym-management-system/
├── main.py              # Entry point of the application
├── gui.py               # Handles the GUI layout and user interactions
├── logic.py             # Contains business logic (e.g., price calculation, member management)
├── database.py          # Handles data storage (e.g., list of members)
├── utils.py             # Utility functions (currently empty)
├── README.md            # Project documentation


PREREQUISITES

Before running the project, ensure you have the following installed:

Python 3.x: Download and install Python from python.org.

Tkinter: Tkinter is included with Python by default. If you don’t have it, install it using:

bash
Copy
sudo apt-get install python3-tk
How to Run the Project
Clone the Repository:

bash
Copy
git clone https://github.com/your-username/gym-management-system.git
cd gym-management-system
Run the Application:

bash
Copy
python main.py


USE THE APPLICATION:

Enter member details (name, phone number, gender, and plan).

Click Calculate Price to see the price of the selected plan.

Click Add Member to add the member to the table.


SCREENSHOTS

Gym Management System Screenshot
Example of the Gym Management System GUI.

![image](https://github.com/user-attachments/assets/427fad2b-c3c9-4ee7-90ae-5813f4700f88)

![image](https://github.com/user-attachments/assets/c973c456-5c2c-4aef-bff7-fb5298a27cf7)



CODE OVERVIEW

main.py
The entry point of the application. It initializes the GUI and starts the program.

gui.py
Contains all the GUI-related code, including labels, entry fields, buttons, and the table for displaying member details.

logic.py
Handles the business logic, such as calculating prices and managing the list of members.

database.py
Manages data storage. In this case, it uses a list to store member details.

utils.py
Reserved for utility functions (currently empty).


FUTURE IMPROVEMENTS

Save Data to a File: Store member details in a file (e.g., CSV or JSON) for persistence.

Edit/Delete Members: Add functionality to edit or delete existing members.

Advanced Plans: Allow custom plans with dynamic pricing.

Database Integration: Use a database (e.g., SQLite) to store member details.


CONTRIBUTING

Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

LICENSE

This project is licensed under the MIT License. See the LICENSE file for details.

AUTHOR

Nitish Kumar Talukdar
Feel free to reach out if you have any questions or suggestions!

Acknowledgments
Thanks to Tkinter for providing an easy-to-use GUI framework.

Inspired by the need for a simple gym management solution.

