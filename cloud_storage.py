import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        dataOfSourceFile = open(file_from, 'rb')
        dbx.files_upload(dataOfSourceFile.read(), file_to)
"""
    access_token variable is declared which has some string.
    Then a new transferData object is created using the
    class defined earlier and access_token is passed to it.
"""

"""
After that a variable called file_from is declared which
will have the path of the file or folder which we want to
upload. 
below that file_to variable is declared which has the full
path to upload the file to, including name that you
wish the file to be called once uploaded.

Then upload_file function of the class is called and
file_from and file_to is passed to it as arguments
"""

#Function definition to upload file to dropbox using access_token & python
def main():
    access_token = 'sl.BFItnowfLAyA7CCV6IUK_gUZKt96CoiAkD8Xy_AzRM958204iEW7iOTYgYNv8xu43senRfg7PSpvBsioZcCGuk0QJEf6oZUScOIHc0NRKGE0WW1q6drMyT__YhE-NsAU9d_aA1A'
    objectOfTansferDataClass = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    objectOfTansferDataClass.upload_file(file_from, file_to)
    print("file has been moved !!!")

#Function call to upload file to dropbox using access_token & python
main()