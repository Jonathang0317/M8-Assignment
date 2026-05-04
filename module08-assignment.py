# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cloud Security": 200,
    "Network security": 165,
    "Technical Support": 110
}
# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", "email": "jsmith@abccorp.com", "phone": "111-1234"}
customer2 = {"company_name": "XYZ Ltd", "contact_person": "LeBron James", "email": "LeBronJ@xyzltd.com", "phone": "222-5678"}
customer3 = {"company_name": "Tech Solutions", "contact_person": "Michael Jordan", "email": "mjordan@techsol.com", "phone": "333-1234"}
customer4 = {"company_name": "Innovate Inc", "contact_person": "Angel Reese", "email": "AngelR@innovate.com", "phone": "444-5678"}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
for cust_id, info in customers.items():
    print(f"ID: {cust_id}, Info: {info}")
    
# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
print("C002 info:", c002_info)
print("C003 contact:", c003_contact)
print("C999 info:", c999_info)

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information
customers["C001"]["phone"] = "555-0000"
customers["C002"]["industry"] = "Finance"


print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
print("C001 updated:", customers["C001"])
print("C002 updated:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}
projects = {
    "C001": [
        {"name": "Website Redesign", "service": "Web Development", "hours": 50, "budget": 150*50},
        {"name": "Security Audit", "service": "Network security", "hours": 20, "budget": 165*20}
    ],
    "C002": [
        {"name": "Data Pipeline", "service": "Data Analysis", "hours": 40, "budget": 175*40}
    ],
    "C003": [
        {"name": "Cloud Migration", "service": "Cloud Security", "hours": 60, "budget": 200*60}
    ],
    "C004": [
        {"name": "Help Desk Setup", "service": "Technical Support", "hours": 15, "budget": 110*15}
    ]
}
print("\n\nProject Information:")
print("-" * 60)
# Add your code here
for cid, proj_list in projects.items():
    print(f"{cid}: {proj_list}")

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for cid, proj_list in projects.items():
    for proj in proj_list:
        cost = proj["hours"] * services[proj["service"]]
        print(f"{cid} - {proj['name']} cost: ${cost:.2f}")

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
print("Customer IDs:", list(customers.keys()))
print("Customer Names:", [c["company_name"] for c in customers.values()])
print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts
service_counts = {}
for proj_list in projects.values():
    for proj in proj_list:
        service_counts[proj["service"]] = service_counts.get(proj["service"], 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
print(service_counts)

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)
all_projects = [p for plist in projects.values() for p in plist]
total_hours = sum(p["hours"] for p in all_projects)
total_budget = sum(p["budget"] for p in all_projects)
avg_budget = total_budget / len(all_projects)
max_budget = max(p["budget"] for p in all_projects)
min_budget = min(p["budget"] for p in all_projects)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
print(f"Total Hours: {total_hours}")
print(f"Total Budget: {total_budget}")
print(f"Average Budget: {avg_budget:.2f}")
print(f"Max Budget: {max_budget}")
print(f"Min Budget: {min_budget}")

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for cid, cust in customers.items():
    proj_list = projects.get(cid, [])
    num_projects = len(proj_list)
    total_hours_cust = sum(p["hours"] for p in proj_list)
    total_budget_cust = sum(p["budget"] for p in proj_list)
    print(f"{cid} | {cust['company_name']} | Projects: {num_projects} | Hours: {total_hours_cust} | Budget: {total_budget_cust}")

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
adjusted_rates = {service: rate*1.1 for service, rate in services.items()}
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects
active_customers = {cid: cust for cid, cust in customers.items() if projects.get(cid)}
print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}
customer_budgets = {cid: sum(p["budget"] for p in projects.get(cid, [])) for cid in customers}
print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension
service_tiers = {service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic" for service, rate in services.items()}
print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
print(service_tiers)

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results
def validate_customer(customer_dict):
    required = ["company_name", "contact_person", "email", "phone"]
    return all(field in customer_dict for field in required)

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
for cid, cust in customers.items():
    print(f"{cid} valid? {validate_customer(cust)}")

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses
status_counts = {"active": 0, "completed": 0, "pending": 0}
for proj_list in projects.values():
    for proj in proj_list:
        proj["status"] = "active"  # Sample status
        status_counts[proj["status"]] += 1
        
print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
print(status_counts)

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys
def analyze_customer_budgets(projects_dict):
    result = {}
    for cid, proj_list in projects_dict.items():
        total = sum(p["budget"] for p in proj_list)
        count = len(proj_list)
        avg = total / count if count else 0
        result[cid] = {"total": total, "average": avg, "count": count}
    return result

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
print(analyze_customer_budgets(projects))

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations
def recommend_services(customer_id, customers, projects, services):
    used_services = {p["service"] for p in projects.get(customer_id, [])}
    recommendations = [s for s in services if s not in used_services]
    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
for cid in customers:
   print(f"{cid} recommendations: {recommend_services(cid, customers, projects, services)}")