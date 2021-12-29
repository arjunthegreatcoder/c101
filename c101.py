import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFile(self,from_file,to_file):
        bbx = dropbox.Dropbox(self.access_token)
        f = open(from_file,'rb')
        bbx.files_upload(f.read(),to_file)
def main():
    access_token = 'wTNhlwEhGB8AAAAAAAAAAVidmiXanBELIbbvKjCCkLCAl0zLFR36ilHVHVQpb38z'
    transferData = TransferData(access_token)
    from_file = input("Enter The File Name To Transfer")
    to_file = input("Enter The Path Of DropBox")
    transferData.uploadFile(from_file,to_file)
    print("Your File Has Been Moved")
main()    
