from llama_cleanup.main import AddressLookup

address_lookup = AddressLookup(
    canadian_postal_codes_path="CanadianPostalCodes202403.csv",
    us_zip_codes_path="USZIPCodes202409.csv",
    llama_model="llama3.1"
)

# Test the lookup method
result = address_lookup.lookup("bridge street and church street camp robinson on m6m 4x2")
print(result)
