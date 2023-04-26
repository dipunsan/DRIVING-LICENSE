from tkinter import *
root = Tk()
root.title("Driving Lisence")
root.geometry("600x400")

root.configure(bg="white")
canvas=Canvas(root,width=300,height=400)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150,90, font=('Times', '24', 'bold italic') ,text="Identity Card")
label_name_tag = canvas.create_text(40,165, font=('Times', '16', 'bold') ,text="Name :")
label_pin_no_tag = canvas.create_text(40,165, font=('Times', '16', 'bold') ,text="Name :")
label_address_tag = canvas.create_text(40,165, font=('Times', '16', 'bold') ,text="Name :")
label_authorised_to_drive_the_following_vehicle_tag = canvas.create_text(40,165, font=('Times', '16', 'bold') ,text="Name :")


label_name = Label(root)
label_pin_no = Label(root)
label_address = Label(root)
label_authorised_to_drive_the_following_vehicle = Label(root)

def myCardDetails():
    name = "Aditya Lenka"
    print(type(name))   
    pin_no = "451478"
    print(type(pin_no))
    address = "Kataribagh, opposite to Naval Base, Kochi, Kerala"
    print(type(address))
    authorised_to_drive_the_following_vehicle = "two wheeler"
    print(type(authorised_to_drive_the_following_vehicle))
    
    label_name['text'] = name
    label_date_of_birth['text'] = "date_of_birth"
    label_pin_no['text'] = "pin_no"
    label_address['text'] = address
    label_authorised_to_drive_the_following_vehicle['text'] = authorised_to_drive_the_following_vehicle
    
    
button1 = Button(root, text = "Show my ID Card", command=myCardDetails)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(90, 205, anchor=CENTER, window=label_grade)
label_subjects_window = canvas.create_window(155, 252, anchor=CENTER, window=label_subjects)
canvas.pack()

root.mainloop()








