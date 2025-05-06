# AI Algorithms and Salesforce Development - Dependencies

## AI Algorithms

This folder contains various AI and algorithm implementations. Here are the dependencies required for each file:

### General Requirements
- Python 3.6+

### File-Specific Dependencies

#### astar.py
- Standard Python libraries only (no external dependencies)

#### chatbot.py
- ChatterBot library (v1.0.8 recommended)
- SQLite (used by ChatterBot's SQLStorageAdapter)
- Additional ChatterBot dependencies:
  - chatterbot-corpus (for training data)
  - pytz (for timezone handling)
  - nltk (Natural Language Toolkit)
  - spacy (For language processing)
  - pint (Unit conversion utility)
  - mathparse (For mathematical evaluation)
  - python-dateutil (For date/time parsing)

#### dfsbfs.py
- Standard Python libraries only
  - collections (deque) - included in Python standard library

#### nqueen.py
- Standard Python libraries only (no external dependencies)

#### greedyselection.py
- Standard Python libraries only (no external dependencies)

### Installation Instructions for AI Components

To install the required dependencies for all AI components, run:

```bash
# Install ChatterBot and primary dependencies
pip install chatterbot==1.0.8 chatterbot-corpus

# Install additional NLP dependencies
pip install nltk spacy pytz pint mathparse python-dateutil

# Download required NLTK data
python -m nltk.downloader punkt
python -m nltk.downloader wordnet
python -m nltk.downloader averaged_perceptron_tagger

# Download required spaCy language model
python -m spacy download en_core_web_sm
```

Note: ChatterBot may have additional dependencies that will be automatically installed. The latest version might be different, so adjust as needed.

### Compatibility Notes

- The chatbot.py file uses ChatterBot which has specific compatibility with Python versions. ChatterBot 1.0.8 works best with Python 3.6-3.8.
- All other scripts should work with any Python 3.6+ version.

## Salesforce Apex and Visualforce (cc/pract_3_apex)

This section contains Salesforce Apex classes and Visualforce pages that need to be deployed to a Salesforce environment.

### Files

#### calc.txt
- Apex class for a basic calculator

#### calc_vfp.txt
- Visualforce page for the calculator interface 

#### sort.txt
- Apex utility class for sorting operations

### Implementation Steps

1. **Setting up the Calculator Application**:
   
   a. **Create the Apex Class**:
   - Log into your Salesforce Developer Console
   - Click File > New > Apex Class
   - Name the class "calculator" (case sensitive)
   - Copy the content from `calc.txt` and paste it into the class editor
   - Click Save

   b. **Create the Visualforce Page**:
   - In Developer Console, click File > New > Visualforce Page
   - Name the page "calculator" or any preferred name
   - Copy the content from `calc_vfp.txt` and paste it into the page editor
   - Click Save

   c. **Link Verification**:
   - The Visualforce page is automatically linked to the Apex class through the controller attribute:
     ```
     <apex:page controller="calculator" sidebar="false">
     ```
   - This connects the Visualforce page to the "calculator" Apex class

2. **Accessing the Calculator**:
   - After deployment, the calculator can be accessed via the URL:
     ```
     https://[your-instance].salesforce.com/apex/[your-visualforce-page-name]
     ```

3. **Additional Sorting Utility**:
   - The `sort.txt` file contains a sorting utility class that can be deployed similarly:
     - Create a new Apex Class named "SortingUtility"
     - Copy content from `sort.txt`
     - This class can be executed via Anonymous Apex by calling: `SortingUtility.testSorting();`

### Requirements

- Access to a Salesforce Developer Environment (Developer Edition or Sandbox)
- Sufficient permissions to create Apex classes and Visualforce pages

## Additional Cloud Computing Resources (cc folder)

This section provides links to markdown guides for cloud computing and Salesforce development concepts.

### Hotel Reservation System in Salesforce (cc/hotel_reservation_system.md)

A comprehensive guide for creating a hotel reservation system in Salesforce Classic without using Visualforce or Apex. This document covers:

- Creating custom objects for Rooms, Customers, and Reservations
- Setting up relationships between objects
- Creating custom tabs and list views
- Configuring page layouts
- Creating reports and dashboards
- Testing the complete system

**To access**: Open the file at `cc/hotel_reservation_system.md`

### Creating EC2 Instances in AWS (cc/creating_ec2_instance.md)

A step-by-step guide for creating and managing Amazon EC2 instances in AWS. The document includes:

- Prerequisites for AWS account setup
- Detailed steps from signing in to launching an instance
- Selecting AMIs and instance types
- Configuring security groups
- Creating and using key pairs
- Connecting to and managing instances
- Important security and cost management considerations

**To access**: Open the file at `cc/creating_ec2_instance.md` 