def analyze_security_incident():
    """
    Automated security incident response system
    """
    
    print("=" * 60)
    print("SECURITY INCIDENT RESPONSE SYSTEM")
    print("=" * 60)
    print()
    
    # Gather incident information
    print("Enter incident details:\n")
    
    # Incident type
    print("Incident Type:")
    print("1. Unauthorized Access Attempt")
    print("2. Malware Detection")
    print("3. Data Breach")
    print("4. DDoS Attack")
    print("5. Phishing Attempt")
    
    incident_type = input("\nSelect type (1-5): ")
    
    # Severity
    print("\nSeverity Level:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("4. Critical")
    
    severity = int(input("\nSelect severity (1-4): "))
    
    # System affected
    affected_system = input("\nAffected system (e.g., Web Server, Database): ")
    
    # Analysis and response
    print("\n" + "=" * 60)
    print("INCIDENT ANALYSIS")
    print("=" * 60)
    
    # Determine response based on severity
    if severity == 4:  # Critical
        print("\n🚨 CRITICAL INCIDENT - IMMEDIATE ACTION REQUIRED")
        print("\nResponse Actions:")
        print("1. ✓ Security team notified immediately")
        print("2. ✓ Incident commander assigned")
        print("3. ✓ Isolating affected systems")
        print("4. ✓ Activating incident response plan")
        print("5. ✓ Notifying management")
        
        # Additional checks for critical
        if incident_type == "3":  # Data breach
            print("6. ✓ Legal team notified")
            print("7. ✓ PR team on standby")
            print("8. ✓ Compliance officer notified")
        
        response_time = "Immediate (< 15 minutes)"
        escalation = "CTO, CISO, CEO"
        
    elif severity == 3:  # High
        print("\n⚠ HIGH SEVERITY - URGENT RESPONSE")
        print("\nResponse Actions:")
        print("1. ✓ Security team notified")
        print("2. ✓ Senior analyst assigned")
        print("3. ✓ Monitoring affected systems")
        print("4. ✓ Preparing containment measures")
        
        response_time = "Within 30 minutes"
        escalation = "Security Manager, IT Director"
        
    elif severity == 2:  # Medium
        print("\n🟡 MEDIUM SEVERITY - STANDARD RESPONSE")
        print("\nResponse Actions:")
        print("1. ✓ Security analyst assigned")
        print("2. ✓ Incident logged")
        print("3. ✓ Initial investigation started")
        
        response_time = "Within 2 hours"
        escalation = "Security Team Lead"
        
    else:  # Low
        print("\n🟢 LOW SEVERITY - ROUTINE HANDLING")
        print("\nResponse Actions:")
        print("1. ✓ Incident logged")
        print("2. ✓ Added to review queue")
        print("3. ✓ Monitoring for patterns")
        
        response_time = "Within 24 hours"
        escalation = "None required"
    
    # Display summary
    print("\n" + "=" * 60)
    print("INCIDENT SUMMARY")
    print("=" * 60)
    print(f"Affected System: {affected_system}")
    print(f"Response Time: {response_time}")
    print(f"Escalation: {escalation}")
    print(f"Status: ACTIVE - Under Investigation")
    print()


# Run the program
if __name__ == "__main__":
    analyze_security_incident()
