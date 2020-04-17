class TemplateReader:
    def __init__(self):
        pass

    def read_course_template(self,course_name):
        try:
            if (course_name=='Btech'):
                email_file = open("email_templates/B. Tech. _!st Year_11062019.html", "r")
                email_message = email_file.read()
            elif (course_name=='Mtech'):
                email_file = open("email_templates/MTEC_ECE_2018.html", "r")
                email_message = email_file.read()
            elif (course_name == 'PhD'):
                email_file = open("email_templates/MTEC_ECE_2018.html", "r")
                email_message = email_file.read()

            return email_message
        except Exception as e:
            print('The exception is '+str(e))
