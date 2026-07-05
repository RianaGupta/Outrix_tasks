from reportlab.pdfgen import canvas
from datetime import datetime
import random 


invoice_number = random.randint(1000,9999)

today= datetime.now().strftime("%d-%m-%Y")
customer_name=input("Enter customer name:")

num_products=int(input("How many products?"))

products=[]
total = 0
for i in range(num_products):
    name=input(f"Enter product {i+1} name: ")
    price = int(input(f"Enter product {i+1} price: "))

    products.append((name,price))
    total += price
print(products)
print(total)
pdf=canvas.Canvas("prof_invoice.pdf")
pdf.setFont("Helvetica-Bold",20)
pdf.drawString(180,800,"OUTRIX SOLUTIONS")

pdf.line(50,780,550,780)

pdf.setFont("Helvetica",12)

pdf.drawString(50,750,f"Invoice No : {invoice_number}")
pdf.drawString(400,750,f"Date: {today}")

pdf.drawString(50,720,f"Customer : {customer_name}")

pdf.line(50,690,550,690)
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(50, 670, "Product")
pdf.drawString(450, 670, "Price")

pdf.line(50,650,550,650)

pdf.setFont("Helvetica",12)

y=620

for product, price in products:
    pdf.drawString(50,y,product)
    pdf.drawString(450,y,str(price))
    y -= 30

pdf.line(50,y,550,y)
pdf.setFont("Helvetica-Bold",12)
pdf.drawString(50,y - 30 , "Total")
pdf.drawString(450,y - 30 , str(total))

pdf.save()

print("Professional invoice generated")
