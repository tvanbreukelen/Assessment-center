from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'assessmentcenter' # Must be replaced by your <storage_account_name>
    account_key = 'ENoVc953Q3t8XgJ6RZy4wmZLLfR2uI9cPWucjB3rsrFXxak1FqEenc7oWBAN9P6mLKmVBaQbrKMVq9LtxcXaXQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'assessmentcenter' # Must be replaced by your storage_account_name
    account_key = 'ENoVc953Q3t8XgJ6RZy4wmZLLfR2uI9cPWucjB3rsrFXxak1FqEenc7oWBAN9P6mLKmVBaQbrKMVq9LtxcXaXQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None