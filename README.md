############################################################################################################
openssl genpkey -algorithm RSA -out server.key -pkeyopt rsa_keygen_bits:4096
openssl req -new -key server.key -out server.csr -subj "/CN=secure-flask-app.example.com"
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
############################################################################################################
podman build -t secure-flask-app .
podman run -d -p 443:443  secure-flask-app
##################################        Validation          ##############################################
https://192.168.1.10/secure
http://192.168.1.10/secure
############################################################################################################
