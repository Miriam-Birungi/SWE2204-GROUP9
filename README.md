# 🏨 Hotel Management System

## 📌 Description
This project is a **comprehensive Hotel Management System** designed to streamline hotel operations, enhance guest experiences, and improve overall efficiency. It includes features for room booking, guest management, staff administration, and more.

## Features
- User authentication and registration
- Room booking and availability management
- Guest profile and booking history management
- Hotel ranking system (1-5 star rating)   
- Performance monitoring using Function Points & empirical analysis
- Admin dashboard for hotel management
- Secure Payment processing and real time booking
- Responsive design for various devices
- Software metrics for monitoring system performance 
- Hotel performance evaluation using  1-5 star rating models

---

## 🛠 Technologies Used  
✅ *Frontend:* HTML5, CSS3, JavaScript  
✅ *Backend:* PHP (Laravel)  
✅ *Database:* MySQL  
✅ *Monitoring Tools:* Google Analytics, New Relic  
✅ *Version Control:* Git, GitHub  

---

## Software Metrics Used  

### Process Metrics (Workflow & User Interaction) 
- Booking Completion Rate (%) (Tracks how many users complete a booking.)  
- Payment Processing Time (s) – Average transaction time.  
- Customer Support Response Time (mins) – Measures how quickly issues are resolved.  

### Product Metrics (Code Quality & System Performance)  
- Defect Density (bugs per 1,000 lines of code) – Measures software reliability.  
- Page Load Time (ms) – Evaluates website speed and responsiveness.  
- Test Coverage (%) – Tracks the percentage of tested functionalities.  

### Resource Metrics (System & Human Resources)  
- Server Uptime (%) – Measures system reliability.  
- Database Query Performance (ms) – Tracks how fast search queries return results.  
- Developer Productivity – Number of features implemented per sprint.  

---

##  Goal-Question-Metric (GQM) Approach  

We applied the GQM methodology to align software measurements with project objectives.  

### Example GQM Application for Hotel Performance Ranking:  

1️⃣ Goal: Improve hotel service quality by *enhancing customer satisfaction* ratings.  
2️⃣ Questions:  
   - How many users give a 5-star rating?  
   - What are the common reasons for low hotel ratings?  
   - Which hotel attributes influence customer satisfaction the most?  
3️⃣ Metrics:  
   - Average Hotel Rating (⭐, ⭐⭐, ⭐⭐⭐, ⭐⭐⭐⭐, ⭐⭐⭐⭐⭐)  
   - Booking Frequency per Hotel – (Total Bookings ÷ Month)  
   - Sentiment Score from Customer Reviews  

---

## 🏆 Hotel Ranking Model (1-5 Star System)  

### Problem Definition:  
We rank hotels based on user preferences using an ordinal scale (1-5 stars).  

### Hotels and Their Average Ratings: 

| Hotel Name                  | Average Rating (1-5 Stars)    | Ranking            |
|-----------------------------|-------------------------------|------------        |
| H1 – Speke Resort Munyonyo  | ⭐⭐⭐⭐⭐ (4.8)            | Highly Recommended |
| H2 – Acacia Lodge           | ⭐⭐⭐⭐☆ (4.2)             | Good Choice        |
| H3 – Lake View Hotel        | ⭐⭐⭐☆☆ (3.6)              | Average            |
| H4 – Agip Hotel             | ⭐⭐☆☆☆ (2.8)               | Needs Improvement  |

A hotel is considered better than another if its rating is 0.5 stars higher.  

### Formula for Hotel Performance Rating:  
\[
Hotel Rating Score = {sum ({User Rating} *{Weight})}/{Total Reviews}
\]
For example,  
- If H1 (4.8) > H3 (3.6), then H1 is preferred over H3.  

---

## 🏨 Entities, Attributes, and Values in the Hotel Booking Model  

| Entity     | Attribute             |Possible Values                                                    |
|------------|---------------------- |-------------------------------------------------------------------|
| Hotels     | Name                  | Speke Resort, Munyonyo, Acacia Lodge, Lake View Hotel, Agip Hotel |
|            | Location              | Entebbe, Kampala, Mbarara                                         |
|            | Rating                | ⭐, ⭐⭐, ⭐⭐⭐, ⭐⭐⭐⭐, ⭐⭐⭐⭐⭐                     |
|            | Room Type             | Single, Double, Suite, Deluxe                                     |
| Rooms      | Price per Night       | $50, $100, $200, $500                                             |
|            | Availability Status   | Available, Booked, Pending                                        |
|            | Features              | WiFi, Breakfast, Pool, Gym, Parking                               |
| Users      | Name                  | Joel Atuhe, Hanani Elizabeth, Arinaitwe Allan                     |
|            | Booking History       | Hotel 1 (2 nights), Hotel 2 (3 nights)                            |
|            | Preferred Location    | City Center, Near Airport                                         |
| Reviews    | Rating                | ⭐, ⭐⭐, ⭐⭐⭐, ⭐⭐⭐⭐, ⭐⭐⭐⭐⭐                     |
|            | Feedback              | Excellent service, Needs improvement                              |

---

## ⚙ Installation Guide  

### 1️⃣ Clone the Repository  
git clone https://github.com/Miriam-Birungi/SWE2204-GROUP9.git
cd SWE2204-GROUP9

## 🛠 Technologies Used  
- ✅ **Frontend:** HTML5, CSS3, JavaScript  
- ✅ **Backend:** PHP (Laravel)  
- ✅ **Database:** MySQL  
- ✅ **Version Control:** Git, GitHub

---

## 📊 Software Metrics Used  

### 🔹 **Process Metrics (Workflow & User Interaction)**  
- **Booking Completion Rate (%)** – Percentage of users who complete a booking.  
- **Payment Processing Time (s)** – Average time taken to complete a transaction.  
- **Customer Support Response Time (mins)** – Measures efficiency of support staff.  

### 🔹 **Product Metrics (Code Quality & System Performance)**  
- **Defect Density (bugs per 1,000 lines of code)** – Evaluates code quality.  
- **Page Load Time (ms)** – Measures website speed and user experience.  
- **Test Coverage (%)** – Tracks the percentage of the system covered by automated tests.  

### 🔹 **Resource Metrics (System & Human Resources)**  
- **Server Uptime (%)** – Percentage of time the system is operational.  
- **Database Query Performance (ms)** – Measures response time for search queries.  
- **Developer Productivity** – Number of features delivered per sprint.  

---

## 🎯 Goal-Question-Metric (GQM) Approach  

We apply the **GQM methodology** to ensure that software measurement is aligned with project goals.  

**Example GQM Application for Booking Success Rate:**  

1️⃣ **Goal:** Improve the booking completion rate by 15% over 3 months.  
2️⃣ **Questions:**  
   - How many users abandon bookings before completion?  
   - What are the most common reasons for failed transactions?  
   - Which pages have the highest exit rates?  
3️⃣ **Metrics:**  
   - **Booking Success Rate:** (Completed bookings ÷ Total attempts) × 100  
   - **Payment Failure Rate:** (Failed transactions ÷ Total transactions) × 100  
   - **Page Load Time:** Avg time taken to load booking pages

## 📊 Software Investigation & Performance Metrics  

This project incorporates **Software Engineering Investigation** to optimize system efficiency.  

### **Empirical Research Techniques Applied:**  
✅ **Case Study:** Analyzing how users interact with the booking system and improving search algorithms.  
✅ **Experimentation:** Testing different UI designs to optimize booking completion rates.  
✅ **Survey-Based Analysis:** Collecting user feedback on hotel satisfaction using Likert scales (1-5 stars).  

**Example Hypothesis:**  
_"Can an improved search algorithm reduce booking time by 20%?"_ 

✅ **Software Complexity Analysis:** Using **Halstead’s Complexity Metrics** to evaluate the **readability and maintainability** of our source code.  

---
## Automating LOC (Lines of Code) Measurement in Python

To dynamically measure the Lines of Code (LOC) in our Hotel Management System, you can use a Python script to scan your PHP, JavaScript, HTML, and CSS files and count.

This python script together with its usage can be found in the [LOC](./LOC/) folder.

---

## 📜 **Halstead's Complexity Analysis in the Hotel Management System**  

### **🔹 What is Halstead's Complexity Model?**  
Halstead’s Complexity Analysis is a **software engineering metric** used to measure **code complexity** by analyzing **operators and operands**.  
It helps our **Hotel Management System** by:  
✅ **Detecting complex code sections** that may need optimization.  
✅ **Measuring the maintainability & readability** of the system.  
✅ **Estimating development effort** based on logical code operations.  

---

## 📏 **Halstead’s Metrics Used in Our Hotel Management System**  
| **Metric** | **Formula** | **Meaning in Our Codebase** |
|------------|------------|---------------------------|
| **n₁** | Unique Operators | Number of distinct operators in the code. |
| **n₂** | Unique Operands | Number of distinct variables/constants. |
| **N₁** | Total Operators | Total occurrences of operators. |
| **N₂** | Total Operands | Total occurrences of operands. |
| **Program Vocabulary (n)** | **n = n₁ + n₂** | Unique tokens in the code. |
| **Program Length (N)** | **N = N₁ + N₂** | Total elements in the code. |
| **Volume (V)** | **V = N × log₂(n)** | Measures the size of the implementation. |
| **Difficulty (D)** | **D = (n₁ / 2) × (N₂ / n₂)** | Complexity of logic in the code. |
| **Effort (E)** | **E = D × V** | Total effort required to develop & maintain the code. |

---

## **⚙️ How Halstead's Complexity is Implemented in the Hotel Management System**  

We use **Python** to **automatically analyze all PHP, JavaScript, and Python files** in the project and calculate **Halstead’s Complexity Metrics**.  
This helps in **evaluating code efficiency, readability, and maintainability**.  

✅ **Scans all source code files in the project**  
✅ **Identifies operators and operands**  
✅ **Computes complexity metrics**  
✅ **Saves results into a CSV file for analysis**  

The Halstead Complexity metrics can be found in the [Halstead](./Halstead/) folder

---
How the software quality analysis.py works.

What This Script Does:
✅ Scans all .php, .js, .html, .css files
✅ Counts:
Total lines of code (LOC)
Unique Operators
Unique Operands
Total Operators
Total Operands
✅ Calculates:
Vocabulary (n)
Length (N)
Volume (V)
Difficulty (D)
Effort (E)
✅ Asks you:
How many bugs/defects are found (for defect density calculation)
✅ Saves:
All results to software_quality_report.csv automatically.

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/Miriam-Birungi/SWE2204-GROUP9.git
3. Set up a local web server (Apache) and ensure PHP is installed.
4. Import the provided MySQL database schema.
5. Configure the database connection in the PHP files.
6. Open the project in your web browser.

## Usage
- Navigate to the homepage to view available rooms and make bookings.
- Use the admin panel to manage hotel operations, rooms, and guest information.
- Explore different sections like About, Contact, and Terms of Service.

## Contributing
Contributions to improve the Hotel Management System are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch
   
   ```bash
   git checkout -b feature-branch
3. Make your changes and commit

   ```bash
   git commit -am 'Add some feature`
4. Push to the branch

   ```bash
   git push origin feature-branch`
5. Create a new Pull Request

## License
[MIT License](https://opensource.org/licenses/MIT)

## Contact
For any queries or support, please contact Bwambale Martin Kigongo at `martinbwam@gmail.com` .
