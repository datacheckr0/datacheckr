def calculate_missed_revenue(total_revenue, num_leads, undelivered_percentage):
    # Calculate revenue per lead
    revenue_per_lead = total_revenue / num_leads

    # Calculate total revenue from valid leads
    total_valid_revenue = total_revenue

    # Calculate missed revenue from undelivered leads
    missed_revenue = total_valid_revenue * undelivered_percentage

    return missed_revenue, revenue_per_lead

def main():
    try:
        # Gather inputs
        total_revenue = float(input("Enter total monthly revenue: "))
        num_leads = int(input("Enter number of leads reached out to per month: "))
        undelivered_percentage = float(input("Enter percentage of undelivered leads (as decimal): "))

        # Calculate missed revenue and revenue per lead
        missed_revenue, revenue_per_lead = calculate_missed_revenue(total_revenue, num_leads, undelivered_percentage)

        # Display results
        print(f"Missed revenue from undelivered leads per month: ${missed_revenue:.2f}")
        print(f"Revenue per lead: ${revenue_per_lead:.2f}")

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
