# Creating a Simple Hotel Reservation System in Salesforce Classic

This guide will walk you through the steps to create a basic hotel reservation system in Salesforce Classic without using Visualforce Pages or Apex classes. We'll focus on creating custom objects and tabs for Rooms, Customers, and Reservations.

## Prerequisites

- Salesforce Developer Account or Sandbox environment
- Administrator access to the Salesforce org

## Step 1: Create Custom Objects

First, we'll create three custom objects to store our data:

### 1.1 Create Room Object

1. Navigate to **Setup** > **Create** > **Objects** > **Create New Custom Object**
2. Fill in the following details:
   - **Label**: Room
   - **Plural Label**: Rooms
   - **Object Name**: Room
   - **Description**: Stores information about hotel rooms
   - Check **Allow Reports** and **Allow Activities**
   - **Record Name**: Room Number
   - **Data Type**: Text
   - **Save**

3. Add custom fields:
   - **Room Type** (Picklist): Standard, Deluxe, Suite
   - **Floor** (Number)
   - **Rate Per Night** (Currency)
   - **Status** (Picklist): Available, Occupied, Maintenance
   - **Description** (Text Area)
   - **Amenities** (Multi-select Picklist): WiFi, TV, Mini Bar, Ocean View, etc.

### 1.2 Create Customer Object

1. Navigate to **Setup** > **Create** > **Objects** > **Create New Custom Object**
2. Fill in the following details:
   - **Label**: Customer
   - **Plural Label**: Customers
   - **Object Name**: Customer
   - **Description**: Stores information about hotel customers
   - Check **Allow Reports** and **Allow Activities**
   - **Record Name**: Customer Name
   - **Data Type**: Text
   - **Save**

3. Add custom fields:
   - **Email** (Email)
   - **Phone** (Phone)
   - **Address** (Text Area)
   - **ID Type** (Picklist): Passport, Driver's License, National ID
   - **ID Number** (Text)
   - **Loyalty Status** (Picklist): Regular, Silver, Gold, Platinum

### 1.3 Create Reservation Object

1. Navigate to **Setup** > **Create** > **Objects** > **Create New Custom Object**
2. Fill in the following details:
   - **Label**: Reservation
   - **Plural Label**: Reservations
   - **Object Name**: Reservation
   - **Description**: Stores information about hotel reservations
   - Check **Allow Reports** and **Allow Activities**
   - **Record Name**: Reservation Number
   - **Data Type**: Auto Number
   - **Display Format**: R-{0000}
   - **Starting Number**: 1
   - **Save**

3. Add custom fields:
   - **Check-in Date** (Date)
   - **Check-out Date** (Date)
   - **Number of Guests** (Number)
   - **Status** (Picklist): Confirmed, Checked-in, Checked-out, Cancelled
   - **Total Amount** (Currency)
   - **Payment Status** (Picklist): Pending, Partial, Paid
   - **Special Requests** (Text Area)

## Step 2: Create Relationships Between Objects

Now we'll create relationships between our objects:

### 2.1 Create Lookup Relationships on Reservation Object

1. Navigate to **Setup** > **Create** > **Objects** > **Reservation**
2. Add two lookup relationship fields:
   - **Room** (Lookup Relationship to Room object)
   - **Customer** (Lookup Relationship to Customer object)

## Step 3: Create Custom Tabs

Create tabs for each of our custom objects:

1. Navigate to **Setup** > **Create** > **Tabs**
2. Click **New** in the Custom Object Tabs section
3. Create tabs for each object:
   - Select **Room** object, choose an icon, and save
   - Select **Customer** object, choose an icon, and save
   - Select **Reservation** object, choose an icon, and save

## Step 4: Create List Views

Create useful list views for each tab:

### 4.1 Room List Views

1. Navigate to the **Rooms** tab
2. Click **Create New View**
3. Create the following views:
   - **All Rooms**: All rooms in the hotel
   - **Available Rooms**: Filter where Status = Available
   - **Occupied Rooms**: Filter where Status = Occupied
   - **Maintenance Rooms**: Filter where Status = Maintenance

### 4.2 Customer List Views

1. Navigate to the **Customers** tab
2. Click **Create New View**
3. Create the following views:
   - **All Customers**: All customers
   - **VIP Customers**: Filter where Loyalty Status = Gold OR Platinum

### 4.3 Reservation List Views

1. Navigate to the **Reservations** tab
2. Click **Create New View**
3. Create the following views:
   - **All Reservations**: All reservations
   - **Today's Check-ins**: Filter where Check-in Date = TODAY
   - **Today's Check-outs**: Filter where Check-out Date = TODAY
   - **Active Reservations**: Filter where Status = Confirmed OR Checked-in

## Step 5: Create a Custom App

Create a custom app to group all our tabs:

1. Navigate to **Setup** > **Create** > **Apps**
2. Click **New**
3. Fill in the following details:
   - **App Label**: Hotel Management
   - **Description**: Simple hotel reservation system
   - **Logo**: Upload a hotel logo (optional)
   - Select the tabs: Home, Rooms, Customers, Reservations, Reports
   - **Save**

## Step 6: Set Up Page Layouts

Customize page layouts for better user experience:

1. Navigate to **Setup** > **Create** > **Objects** > select each object
2. Click on **Page Layouts** > **Edit** next to the default layout
3. Arrange fields in logical sections:
   - For Rooms: Room Details, Amenities, System Information
   - For Customers: Customer Details, Contact Information, System Information
   - For Reservations: Reservation Details, Room & Customer, Payment Information, System Information
4. Add related lists to show connections between objects:
   - On Room layout: Add Reservations related list
   - On Customer layout: Add Reservations related list

## Step 7: Create Reports and Dashboard

Create reports to analyze your hotel data:

1. Navigate to the **Reports** tab
2. Create the following reports:
   - **Room Occupancy**: Summary report of rooms grouped by status
   - **Reservations by Date**: Matrix report of reservations by check-in date
   - **Revenue Report**: Summary report of reservations grouped by month showing sum of Total Amount
   - **Customer Loyalty Report**: Summary report of customers grouped by loyalty status

3. Create a dashboard with these reports for a quick overview of hotel operations

## Step 8: Test the System

Test your hotel reservation system with the following workflow:

1. Create sample Room records
2. Create sample Customer records
3. Create Reservation records linking Rooms and Customers
4. Test the list views and reports

## Conclusion

You've now created a simple hotel reservation system in Salesforce Classic without using Visualforce Pages or Apex classes. This system allows you to:

- Manage hotel rooms and their availability
- Track customer information
- Create and manage reservations
- Generate reports on occupancy and revenue

This system can be further enhanced with automation using Process Builder or Flow to automatically update room status when reservations are created or completed.