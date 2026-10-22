# HTTP (Hypertext Transfer Protocol) is a protocol that allows a client and a server to communicate.




# Status	                        Meaning	                            Typical use
# 200 OK	                        Successful request	                Data retrieved or updated
# 201 Created	                    Resource created	                New expense added
# 204 No Content	                Success without response body	    Resource deleted
# 400 Bad Request	                Invalid request	                    Malformed input
# 401 Unauthorized	                Authentication required or failed	Missing or invalid credentials
# 403 Forbidden	                    Access denied	                    Insufficient permissions
# 404 Not Found	                    Resource doesn't exist	            Expense ID not found
# 422 Unprocessable Content	        Request data fails validation	    Invalid field values
# 500 Internal Server Error	        Unexpected server error	Unhandled backend failure






# install dependencies
# mkdir expense-api
# cd expense-api

# python3 -m venv .venv
# source .venv/bin/activate

# pip install fastapi uvicorn



