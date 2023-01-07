# OC-token-spoof

Overriding JWT token to set custom values in the JWT token that can be used to set various attributes on the liveworkitem. Essentially implementing based on the below documentation

https://learn.microsoft.com/en-us/dynamics365/customer-service/create-chat-auth-settings


1. Create a public / private key pair using the following command \
`` openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -in private_key.pem -out public_key.pem ``