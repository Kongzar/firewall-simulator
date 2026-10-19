# Firewall Rule Simulator

A small Python script that simulates incoming network traffic and checks each
connection against a simple firewall rule set. It's a beginner-friendly demo of
how allow/block rules work.

## How it works

1. `generate_random_ip()` creates a random IP address in the `192.168.1.1`–`192.168.1.20` range.
2. `check_firewall_rules()` looks the IP up in a dictionary of firewall rules.
   - If the IP has a rule (e.g. `block`), that action is returned.
   - If there's no matching rule, the default action is `allow`.
3. `main()` simulates 12 incoming connections and prints the result for each one.
4. Each simulated connection also gets a random number (0-9999), printed as `Random:`. It acts as a placeholder connection ID and doesn't affect the allow/block decision.

## Firewall rules

| IP address    | Action |
|---------------|--------|
| 192.168.1.1   | block  |
| 192.168.1.4   | block  |
| 192.168.1.9   | block  |
| 192.168.1.13  | block  |
| 192.168.1.16  | block  |
| 192.168.1.19  | block  |

All other IPs are allowed by default.

## Requirements

- Python 3.6+ (uses f-strings)
- No external libraries (only the built-in `random` module)

## Usage

```bash
python firewall_simulator.py
```

## Example output

```
IP: 192.168.1.7, Action: allow, Random: 4821
IP: 192.168.1.13, Action: block, Random: 903
IP: 192.168.1.2, Action: allow, Random: 7745
...
```

Output varies on every run because the IPs are random.

## Ideas for improvement

- Add rules for IP ranges or subnets (using the `ipaddress` module)
- Add port and protocol rules
- Log results to a file
- Change the default policy to "deny" (default-deny is the safer real-world approach)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
