const crypt=require('crypto')
const text="Aadit Singh Bagga"
const hash=crypt.createHmac('sha256',text).digest()
console.log(hash)
