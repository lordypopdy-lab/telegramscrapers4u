import csv

def format_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header row
        writer.writerow(["sr. no.", "username", "user id", "name", "Status"])
        
        # Skip the header of the input file
        next(reader)
        
        sr_no = 1  # Initialize serial number
        
        for row in reader:
            username = row[0].strip() if row[0].strip() else "Unknown"
            user_id = row[2].strip() if len(row) > 2 else ""
            name = row[1].strip() if len(row) > 1 else ""
            status = row[-1].strip() if row[-1].strip() else ""
            
            # Filter out rows where username is "Unknown"
            if username.lower() != "unknown":
                writer.writerow([sr_no, username, user_id, name, status])
                sr_no += 1
    
    print(f"Formatted CSV saved as {output_file}")

# Example usage
format_csv("teammember.csv", "output.csv")
