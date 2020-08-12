#!/bin/sh
# First of "data formats" section
openssl pkey -inform PEM -outform DER -in cert.pem -text
# Then for second question
openssl x509 -in 2048b-rsa-example-cert.der -inform der -noout 
-modulus
