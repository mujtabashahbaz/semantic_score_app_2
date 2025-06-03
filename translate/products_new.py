import csv

# Product data
products = [
    ["Product Name", "Price"],
    ["9 Programs Colorful Screen Contra Angle Endo Motor with LED Light", 21500],
    ["Ferguson Suction Tube 2 mm to 5 mm x 170 mm", 550],
    ["Polishing Brushes - Pack of 100 Brushes", 1650],
    ["SND-Glass Ionomer Cement Type 1", 1500],
    ["Protefix Denture Fixative Powder", 130],
    ["Dental Matrix Sectional Contoured Matrices for Teeth Replacement", 2200],
    ["Wireless Gutta-Percha Heating Cutter", 5500],
    ["Dental Tofflemire Matrix Retainers", 150],
    ["3 Pcs Dental Root Elevators", 950],
    ["Mershon Band Pusher Elevator", 550],
    ["6 Pcs Needle Files Hand Use", 2200],
    ["Interproximal Polishing Strips with Centre Gap – Coarse, Medium and Fine – 1 box / 75 pcs", 2500],
    ["3Pcs Titanium Dental Root Canal Filler", 3500],
    ["Sectional Contoured Metal Matrices", 1500],
    ["Bird Beak Pliers", 1200],
    ["B&E Flow Composite A3.5", 3200],
    ["Dental VITA 3D MASTER Bleached Teeth Shade Guide 29 Colors & classical 16 Colors", 2000],
    ["Semi-adjustable Dental Articulator JT Series", 500]
]

# Write to CSV file
with open('dental_products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(products)

print("CSV file 'dental_products.csv' has been created successfully.")