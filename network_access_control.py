def check_network_access():
    """
    Network access control decision system
    """
    
    print("=" * 60)
    print("NETWORK ACCESS CONTROL SYSTEM")
    print("=" * 60)
    print()
    
    # User information
    username = input("Enter username: ")
    ip_address = input("Enter IP address: ")
    time_hour = int(input("Enter current hour (0-23): "))
    
    # Security checks
    print("\nPerforming security checks...\n")
    
    # Check 1: User authentication
    valid_users = ["admin", "user1", "user2", "security_analyst"]
    is_authenticated = username in valid_users
    
    if is_authenticated:
        print(f"✓ User '{username}' authenticated")
    else:
        print(f"❌ User '{username}' not recognized")
    
    # Check 2: IP address validation
    internal_ips = ["192.168.1.", "10.0.0.", "172.16.0."]
    is_internal_ip = any(ip_address.startswith(prefix) for prefix in internal_ips)
    
    if is_internal_ip:
        print(f"✓ IP {ip_address} is from internal network")
    else:
        print(f"⚠ IP {ip_address} is external")
    
    # Check 3: Business hours
    is_business_hours = 9 <= time_hour < 17
    
    if is_business_hours:
        print(f"✓ Access during business hours ({time_hour}:00)")
    else:
        print(f"⚠ Access outside business hours ({time_hour}:00)")
    
    # Decision logic
    print("\n" + "=" * 60)
    print("ACCESS DECISION")
    print("=" * 60)
    print()
    
    if not is_authenticated:
        print("❌ ACCESS DENIED")
        print("Reason: User not authenticated")
        print("Action: Request proper credentials")
        
    elif is_internal_ip and is_business_hours:
        print("✓ ACCESS GRANTED - Full Access")
        print("Reason: Internal user during business hours")
        print("Access Level: Standard")
        
    elif is_internal_ip and not is_business_hours:
        print("⚠ ACCESS GRANTED - Limited Access")
        print("Reason: Internal user outside business hours")
        print("Access Level: Restricted")
        print("Note: Activity will be logged and monitored")
        
    elif not is_internal_ip and is_business_hours:
        print("⚠ ACCESS REQUIRES ADDITIONAL VERIFICATION")
        print("Reason: External IP address")
        print("Action: VPN connection or 2FA required")
        
    else:  # External IP, outside business hours
        print("❌ ACCESS DENIED")
        print("Reason: External access outside business hours")
        print("Action: Contact security team for special access")
    
    print()


# Run the program
if __name__ == "__main__":
    check_network_access()
