from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'storagesysqaac' # Must be replaced by your <storage_account_name>
    account_key = '/5xK9xeE211oJAZPuBoijfVyabjhOMAYPN8v148dslclgeLg3+rC9PwWG3ul+9ZWS2o/YoiKkigmaF9exKEySA==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'storagesysqaac' # Must be replaced by your storage_account_name
    account_key = '/5xK9xeE211oJAZPuBoijfVyabjhOMAYPN8v148dslclgeLg3+rC9PwWG3ul+9ZWS2o/YoiKkigmaF9exKEySA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None