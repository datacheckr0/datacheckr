def calculate_costs(total_spent, num_leads, unverified_percentage):
    # Calculate cost per lead
    cost_per_lead = total_spent / num_leads
    
    # Calculate total cost of wasted leads
    total_wasted_cost = total_spent * unverified_percentage

    return cost_per_lead, total_wasted_cost

def main():
    try:
        # Gather inputs
        total_spent = float(input("Enter total amount spent on leads per month: "))
        num_leads = int(input("Enter number of leads targeted per month: "))
        unverified_percentage = float(input("Enter percentage of leads with unverified data (as decimal): "))

        # Calculate costs
        cost_per_lead, total_wasted_cost = calculate_costs(total_spent, num_leads, unverified_percentage)

        # Display results
        print(f"Cost per lead: ${cost_per_lead:.2f}")
        print(f"Total cost of wasted leads per month: ${total_wasted_cost:.2f}")
        print(f"Total cost of wasted leads per year: ${total_wasted_cost:.2f * 12}")

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
