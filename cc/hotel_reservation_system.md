# 🏨 Hotel Reservation System using Salesforce Classic

This project demonstrates how to create a **Hotel Reservation System** application in **Salesforce Classic** using custom objects, fields, and relationships.

---

## 🎯 Objective

Build a custom application in **Salesforce Classic** to manage hotel room reservations. This includes managing rooms, customers, and reservation records using custom objects, fields, and lookup relationships.

---

## 🔧 Prerequisites

- Salesforce Classic is enabled in your Salesforce org.
- Admin access to create objects, fields, and tabs.

---

## 🚀 Step-by-Step Instructions

### 📁 1. Create a New Custom App
1. Go to **Setup** (Click on your name > Setup).
2. Navigate to **Build > Create > Apps**.
3. Click **New** under "Custom Apps".
4. Select **Custom App**, click **Next**.
5. App Label: `Hotel Reservation System`
6. App Name: `Hotel_Reservation_System`
7. Add a custom logo if desired.
8. Choose tabs to include initially (we'll add the ones we create later).
9. Assign profiles that can access the app.
10. Click **Save**.

---

## 🏨 Room Management

### 🧱 2. Create the Room Object
1. Go to **Build > Create > Objects**.
2. Click **New Custom Object**.
3. Label: `Room`
4. Object Name: `Room`
5. Plural Label: `Rooms`
6. Check **"Launch New Custom Tab Wizard"** after saving.
7. Save.

### 3️⃣ Create Custom Fields for Room
Navigate to the Room object and click **"New"** under **Custom Fields & Relationships**:

- **Type**
  - Data Type: Picklist
  - Values: Single, Double, Suite
  - Required: Yes

- **Price**
  - Data Type: Currency
  - Decimal Places: 2
  - Required: Yes

- **Available**
  - Data Type: Checkbox
  - Default Value: Checked (True)

### 🗂️ 4. Create Tab for Room
1. After object creation, the **Tab Wizard** should open.
2. Tab Style: Choose an icon (e.g., Key or Hotel).
3. Click **Next**, assign to profiles, and **Save**.

---

## 👤 Customer Management

### 🧱 5. Create the Customer Object
1. Go to **Create > Objects** > **New Custom Object**.
2. Label: `Customer`
3. Object Name: `Customer`
4. Plural Label: `Customers`
5. Save and launch the **New Custom Tab Wizard**.

### 6️⃣ Create Custom Fields for Customer
- **Phone**
  - Data Type: Phone
  - Required: Yes

- **Email**
  - Data Type: Email
  - Required: Yes

### 🗂️ 7. Create Tab for Customer
Use the **Tab Wizard** to create a tab for Customer.
- Choose an appropriate icon (e.g., Person).
- Save.

---

## 📅 Reservation Management

### 🧱 8. Create the Reservation Object
1. Go to **Create > Objects** > **New Custom Object**.
2. Label: `Reservation`
3. Object Name: `Reservation`
4. Plural Label: `Reservations`
5. Save and launch the **Tab Wizard**.

### 9️⃣ Create Custom Fields for Reservation
- **Check-in**
  - Data Type: Date

- **Check-out**
  - Data Type: Date

- **Lookup to Room**
  - Data Type: Lookup Relationship
  - Related To: `Room`

- **Lookup to Customer**
  - Data Type: Lookup Relationship
  - Related To: `Customer`

> These relationships help you associate each reservation with one customer and one room.

### 🗂️ 10. Create Tab for Reservation
Use the **Tab Wizard** to create a tab for Reservation.
- Icon: Choose something like a Calendar or Document.
- Save.

---

## 🔄 Summary of Objects and Fields

### Object: **Room**
| Field Name | Type       |
|------------|------------|
| Name       | Auto       |
| Type       | Picklist   |
| Price      | Currency   |
| Available  | Checkbox   |

### Object: **Customer**
| Field Name | Type    |
|------------|---------|
| Name       | Auto    |
| Phone      | Phone   |
| Email      | Email   |

### Object: **Reservation**
| Field Name | Type              |
|------------|-------------------|
| Name       | Auto              |
| Check-in   | Date              |
| Check-out  | Date              |
| Room       | Lookup(Room)      |
| Customer   | Lookup(Customer)  |

---

## ✅ Final Output

Once completed, your **Hotel Reservation System** in **Salesforce Classic** will allow you to:
- Track room availability and pricing.
- Store customer contact details.
- Record reservations with check-in and check-out dates.
- Use custom tabs to easily access data.

---

## 🧪 Bonus: Test Your Application

- Try creating a few rooms (e.g., Single, Double).
- Add customers.
- Create reservation records by linking rooms and customers with check-in/out dates.
- Use **Reports** or **List Views** to analyze data.

---

Happy Building! ☁️
