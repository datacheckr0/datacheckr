#! python3
# leadCalc.py - Calculates the cost os wasted leads per month and year do to undelivered email addresses

def calculate_costs(total_spent, num_leads, unverified_percentage):
    # Calculate cost per lead
    cost_per_lead = total_spent / num_leads
    
    # Calculate total cost of wasted leads per month
    total_wasted_cost_per_month = total_spent * unverified_percentage

    # Calculate total cost of wasted leads per year
    total_wasted_cost_per_year = total_wasted_cost_per_month * 12

    return cost_per_lead, total_wasted_cost_per_month, total_wasted_cost_per_year

def main():
    try:
        # Gather inputs
        total_spent = float(input("Enter total amount spent on leads per month: "))
        num_leads = int(input("Enter number of leads targeted per month: "))
        unverified_percentage = float(input("Enter percentage of leads with unverified data (as decimal): "))

        # Calculate costs
        cost_per_lead, total_wasted_cost_per_month, total_wasted_cost_per_year = calculate_costs(total_spent, num_leads, unverified_percentage)

        # Display results
        print(f"Cost per lead: ${cost_per_lead:.2f}")
        print(f"Total cost of wasted leads per month: ${total_wasted_cost_per_month:.2f}")
        print(f"Total cost of wasted leads per year: ${total_wasted_cost_per_year:.2f}")

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()

