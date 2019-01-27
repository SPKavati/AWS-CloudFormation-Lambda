import boto3
from datetime import datetime, timedelta

iamClient = boto3.client('iam')

def lambda_handler(event, context):
    try:
        response = client.list_users()
        for i in range(len(response['Users'])):
            DisableAccount = ((datetime.now() - timedelta(days=180)) > response['Users'][i]['PasswordLastUsed'] > (datetime.now() - timedelta(days=90)))
            DeleteAccount = (response['Users'][i]['PasswordLastUsed'] > (datetime.now() - timedelta(days=180)))
            if(DisableAccount):
                print("Disabling the User since not Used accounts for more than 90 days ")
                user = iam.User(response['Users'][i]['UserName'])
                print("Disabling Login Profile")
                login_profile = user.LoginProfile()
                response = login_profile.delete()
                print(response)
                print("Diabling AccessKeys")
                access_key_iterator = user.access_keys.all()
                for access_key in access_key_iterator:
                    response = access_key.deactivate()
            if(DeleteAccount):
                print("Deleting the User account Since Not logged on for more than 180 days")
                response = user.delete()
                print(response)
    except Exception as e:
        print(e)
