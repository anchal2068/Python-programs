import csv
def write_into_csv(info_list):
    with open('student_into_csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(("Name", "Age", "Contact", "E-mail_Id"))
        writer.writerow(info_list)

if __name__ =='__main__':
    condition = True
    student_num=1
    while(condition):
        student_info=input("Enter student information for student #{} in the following format(Name Age Contact E-mail_Id):".format(student_num))
        #print("Entered information:" + student_info)
        student_info_list=student_info.split(' ')
        print("Entered split up information is:" + str(student_info_list))
        print("The entered information is -\nName: {}\nAge: {}\nContact: {}\nE-mail_Id: {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        write_into_csv(student_info_list)

        choice_check=input("is the entered information correct(yes/no):")
        if choice_check=="yes":
            write_into_csv(student_info_list)

            condition_check=input("Enter (yes/no) if  you want to enter information for another student:")
            if condition_check=="yes":
                condition = True
                student_num= student_num + 1
            elif condition_check=="no":
                condition=False
        elif choice_check=="no":
                print("\nPlease re-enter the values!")
