	function Name()
	{
		var name=document.getElementById("name").value
		if(name.length<1)
         	{
            	document.getElementById("sp1").innerHTML="*required"
          	}
        else
        	{
        		document.getElementById("sp1").innerHTML=""
        	}
        
	}


	function User()
	{
		var user=document.getElementById("user").value
		var reg= /^\S*$/
		if(user.length<1)
         	{
            	document.getElementById("sp2").innerHTML="*required"
          	}
        else if(reg.test(user))
        	{
        		document.getElementById("sp2").innerHTML=""
        	}
        	else
        	{
        		document.getElementById("sp2").innerHTML="*no space between characters"
        	}
        
	}

	function Pwd()
	{
		var pwd=document.getElementById("pwd").value
		if(pwd.length<1)
         	{
            	document.getElementById("sp3").innerHTML="*required"
          	}
        else if(pwd.length<8 || pwd.length>16)
        	{
        		document.getElementById("sp3").innerHTML="*password must have 8-16 characters"
        	}
        	else
        	{
        		document.getElementById("sp3").innerHTML=""
        	}
        
	} 

	function Cpwd()
	{
		var cpwd=document.getElementById("cpwd").value
		var pwd=document.getElementById("pwd").value
		if(cpwd.length<1)
         	{
            	document.getElementById("sp4").innerHTML="*required"
          	}
        else if(pwd!==cpwd)
        	{
        		document.getElementById("sp4").innerHTML="*password does not match "
        	}
        	else
        	{
        		document.getElementById("sp4").innerHTML=""
        	}
	} 

	function Email()
	{
		var email=document.getElementById("email").value
		var reg=/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
		if(email.length<1)
         	{
            	document.getElementById("sp5").innerHTML="*required"
          	}
        else if(reg.test(email))
        		{
            		document.getElementById("sp5").innerHTML=""
          		}
          		else
	        	{
	        		document.getElementById("sp5").innerHTML="*invalid email"
	        	}
        	
	        
	}

	function Mobile()
	{
		var mobile=document.getElementById("mobile").value
		var reg= /^\+?([0-9]{2})\)?[-. ]?([0-9]{5})[-. ]?([0-9]{5})$/
		if(mobile.length<5)
         	{
            	document.getElementById("sp6").innerHTML="*required"
          	}
        else if(reg.test(mobile))
        	{
        		document.getElementById("sp6").innerHTML=""
        	}
        	else
        	{
        		document.getElementById("sp6").innerHTML="*invalid mobile number"
        	}
        
	}

	function Add()
	{
		var add=document.getElementById("add").value
		if(add.length<1)
         	{
            	document.getElementById("sp7").innerHTML="*required"
          	}
        else
        	{
        		document.getElementById("sp7").innerHTML=""
        	}
        
	}

  function Log()
  {
    var sp2=document.getElementById("sp2").innerHTML
    var sp3=document.getElementById("sp3").innerHTML
    var user=document.getElementById("user").value
    var pwd=document.getElementById("pwd").value
     if(user.length==0 || pwd.length==0)
    {
      document.getElementById("sp9").innerHTML="Please fill the Log In Details"
      return false
    }
     else if (sp2.length<1 && sp3.length<1) 
            {   
              return true
            }   
          else
            {    
              document.getElementById("sp9").innerHTML="User Name or Password Incorrect"
              return false
            }    
  }


  function Submit()
  {
    var p1=document.getElementById("sp1").innerHTML
    var p3=document.getElementById("sp3").innerHTML
    var p4=document.getElementById("sp4").innerHTML  
    var p5=document.getElementById("sp5").innerHTML
    var p6=document.getElementById("sp6").innerHTML
    var p7=document.getElementById("sp7").innerHTML

      var a=document.getElementById("a").value
      var name=document.getElementById("name").value
      var gender=document.getElementById("gender").value
      var dob=document.getElementById("dob").value
      var dep=document.getElementById("dep").value
      var email=document.getElementById("email").value
      var pwd=document.getElementById("pwd").value
      var cpwd=document.getElementById("cpwd").value
      var mobile=document.getElementById("mobile").value
      var add=document.getElementById("add").value
    

    if(a.length<1 || name.length<1 || gender.length<1 || dob.length<1 || dep.length<1 || email.length<1 || pwd.length<1 || cpwd.length<1 || mobile.length<1 || add.length<1)
    {
      document.getElementById("sp8").innerHTML="Please fill the Mandatory fields"
      return false
    }
    else if(p1.length<1 && p3.length<1 && p4.length<1 && p5.length<1 && p6.length<1 && p7.length<1)
          {
            return true
          }
          else
          {
            document.getElementById("sp8").innerHTML="Please fill the form Correctly"
            return false 
          }

  }



   
    
   
    
    