This is an Online shop with DRF and React JS.

It has some features like :
- Full authentication via OTP
- Multi Clients (GOLDEN, SILVER, BRONZE) to count selling volume individually
- Redis database to control some async tasks
- Coupons have  certain amount of use time for each client types
- A section to keep track of shipping products
- Seprated media file to prevent shell attack

Before you want to test it in development : 
- first fill up some settings like SECRET_KEY in settings.py
- create migrations folder (I removed them)
- initiate a docker container to run redis (or directly run redis on port 6379)
- I set time zone to Iran local time zone, you change it as you please

If you found any bugs or have any advice, send me a comment.

Thanks.
