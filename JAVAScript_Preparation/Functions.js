<!DOCTYPE html>
<html>
<body>

<h1> FUNCTION </h1>
<h2>
function add(a,b)
{
return a+b;
}
</h2>

The number one is 
<p id="one">20</p>

The number two is 
<p id="two">25</p>

After Addition number is 
<p id="three"></p>

<i>1. document.getElementById.html gets the html content <br>
2. parseInt converts html element type to integer!</i>

<script>

function add(a,b)
{
return a+b;
}
y=document.getElementById("one").innerHTML;
z=document.getElementById("two").innerHTML;

document.getElementById("three").innerHTML=add(parseInt(y),parseInt(z));

</script>

</body>
</html>




<!--
 FUNCTION
function add(a,b) { return a+b; }
The number one is

20
The number two is

25
After Addition number is

45
1. document.getElementById.html gets the html content
2. parseInt converts html element type to integer!
  -->

