# SaliencyHeatmapGaze
Folder Structure:
- demos: demo videos 
- images: images for server push
- powerpoint: powerpoint presentation in PDF format

NOTE: To run you will need to generate SSL keys. Use the following command to do so. I originally had the keys on the repository, but Github sent me a security error. 
 openssl req -x509 -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' \
  -keyout localhost-privkey.pem -out localhost-cert.pem
