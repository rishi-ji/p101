  
import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def uploadFolder(self, From, To):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(From):
            for filename in files:
                localPath = os.path.join(root, filename)
                relPath = os.path.relpath(localPath, From)
                dbxPath = os.path.join(To, relPath)
                
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dbxPath, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.Ax43fZE1Ge4yR_rHqoQP5jpJft6XJXueeiqRLu50uySXKcLkzJzB0KszqCaE-j6iVNAKbxKgqo9BU55tMs_q1wATE_a3Wt_FlkD1cAjhq3mo7jJKc85LNxhw-lBdfN8Iw0b3gven4Ks'
    transferData = TransferData(access_token)

    From = str(input("Enter the path of the folder to be uploaded: "))
    To = input("Enter the path to upload to Dropbox: ")
    transferData.uploadFolder(From,To)
    print("file has been moved !!!")

main()