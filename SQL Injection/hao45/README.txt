a:the source and type checking for any embeeded url are ineffective and no one can control the sending
Thus, add a image but sending protocol to url and get the cookie with it. This will send the cookie to the attacker.

b:also, since no sending control, every one can send to any destiny, and the webserver does not check anything (the sender's url) other than cookie 
Thus, when the user is logged in, send the trasfer protocol to the server and the jump to other pages so the user will not notice it in human

c:the registeration protocol does not escape any SQL character when checking the user name in registeration (only quote the name) and/or salt value
As a result, the salt checking may check the different user than the input one.
Thus, register a new user with the ';-- after the attacked username and everything is fine so far. 
So when checking the salt, it will check the new user, 
but when checking the name and passward, the post characters will trick the sql server and make it return true bypassing the password.