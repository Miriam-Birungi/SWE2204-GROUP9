Hotel Management System

**Overview**

The Hotel Management System is a web-based application designed to simplify hotel management tasks like room bookings, user registrations, payments, and administration. Built using PHP, MySQL, JavaScript, HTML, and CSS, it provides an efficient and secure way to manage hotel operations.

**Key Features**

User Registration & Login: Secure authentication with role-based access.

Room Booking System: Real-time availability and booking management.

Payments & Security: Secure transactions with protection against SQL Injection and XSS.

Admin Dashboard: Manage users, rooms, and reservations efficiently.

**Technology Stack**

Frontend: HTML, CSS, JavaScript

Backend: PHP

Database: MySQL

Web Server: Apache

**Installation Guide**

Clone the repository:

git clone https://github.com/yourusername/hotel-management-system.git

Move the project folder to your web server directory (e.g., htdocs for XAMPP).

Set up the database:

Open phpMyAdmin.

Create a new database (e.g., hotel_management).

"CREATE DATABASE hotel_management;"

Import the SQL file (hotel_booking.sql) from the database/ folder.

Configure the database connection in db.php:

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "hotel_management";

Start Apache & MySQL in XAMPP and access the system via:

http://localhost/hotel-management-system/
