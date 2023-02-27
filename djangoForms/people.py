from main import People

try:
    name = input("Enter Your Name\n")
    PhoneNumber = input("Enter Your Phone Number\n")
    email = input("Enter Your email\n")
    county = input("Enter Your county\n")
    gender = input("Enter Your gender\n")
    religion = input("Enter Your religion\n")
    password = input("Enter Your password\n")

    People.create(name=name,
                  PhoneNumber=PhoneNumber,
                  email=email,
                  county=county,
                  gender=gender,
                  religion=religion,
                  password=password)
    print("Account Created Successfully")
except:
    print("Failed to create an account,Retry")
