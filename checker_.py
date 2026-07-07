print("====== PHISHING LINK CHECKER ======")
print("Check if the link is safe or fake\n")

link = input("Enter link to check: ")

print("\n====== RESULT ======")

if "https://" not in link:
    print("❌ UNSAFE - NO https. Your data can be hacked ")
elif "bank" in link and "login" in link and ".com" not in link:
    print("❌ PHISHING LINK - THIS LOOKS LIKE A FAKE BANK WEBSITE") 
elif "free" in link and "prize" in link:
    print("❌ SCAM LINK - FREE PRIZE OFFERS ARE USUALLY SCAMS ")
else:
    print("✅ SAFE LINK - This link looks safe ")

print("\nTip: Think twice before clicking unknown links ")