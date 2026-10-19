import random #importing the random module to generate random numbers and IP addresses

#defining a function to generate random IP addresses
def generate_random_ip():
    return f"192.168.1.{random.randint(1, 20)}"

#define a function to check if the IP address is in the firewall rules
def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

#defining the main function to simulate incoming traffic and check against firewall rules
def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }

    #for loop to simulate incoming traffic and generate 12 random IP addresses, check against firewall rules, and print the results
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")


# calling the main function to execute the program
if __name__ == "__main__":
    main()
