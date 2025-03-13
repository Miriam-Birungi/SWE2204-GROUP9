# Hotel Management System

## Description
This project is a comprehensive Hotel Management System designed to streamline hotel operations, enhance guest experiences, and improve overall efficiency. It includes features for room booking, guest management, staff administration, and more.

## Features
- User authentication and registration
- Room booking and availability management
- Guest profile and booking history management
- Admin dashboard for hotel management
- Secure Payment processing and real time booking
- Responsive design for various devices
- Software metrics for monitoring system performance 
- Hotel performance evaluation using  1-5 star rating models


## Technologies Used
- HTML5
- CSS3
- JavaScript
- PHP (backend)
- MySQL (database)
- Google analytics, new Relic(monitoring tools)
- github(version control)

# 🏨 Hotel Booking System  

## 📌 Description  
This project is a *comprehensive Hotel Booking System* designed to improve customer satisfaction, booking efficiency, and hotel service quality. It includes:  
✅ Room booking and availability management  
✅ User authentication and profile tracking  
✅ Hotel performance evaluation using *1-5 star rating models*  
✅ Secure payment processing and real-time booking updates  
✅ Software metrics for monitoring system performance  

---

## 📢 Features  
- 🔹 *User authentication and registration*  
- 🔹 *Hotel ranking system (1-5 star rating)*  
- 🔹 *Room booking and availability tracking*  
- 🔹 *Guest profile and booking history management*  
- 🔹 *Admin dashboard for hotel operations*  
- 🔹 *Secure payment processing*  
- 🔹 *Performance monitoring with software metrics*  

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
```bash
git clone https://github.com/Miriam-Birungi/SWE2204-GROUP9.git
cd SWE2204-GROUP9

## Installation
1. Clone the repository:
   git clone https://github.com/Miriam-Birungi/SWE2204-GROUP9.git
2. Set up a local web server (Apache) and ensure PHP is installed.
3. Import the provided MySQL database schema.
4. Configure the database connection in the PHP files.
5. Open the project in your web browser.

## Usage
- Navigate to the homepage to view available rooms and make bookings.
- Use the admin panel to manage hotel operations, rooms, and guest information.
- Explore different sections like About, Contact, and Terms of Service.

## Contributing
Contributions to improve the Hotel Management System are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (\`git checkout -b feature-branch\`)
3. Make your changes and commit (\`git commit -am 'Add some feature'\`)
4. Push to the branch (\`git push origin feature-branch\`)
5. Create a new Pull Request

## License
[MIT License](https://opensource.org/licenses/MIT)

## Contact
For any queries or support, please contact Bwambale Martin Kigongo at martinbwam@gmail.com .
