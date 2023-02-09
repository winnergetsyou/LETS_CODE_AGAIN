<!DOCTYPE html>
<html>


<body>

<input id = "hi">
<button onclick=function1()>Submit</button>

<p id="input_id">d</p>
<script>

function function1()
{
document.getElementById("input_id").innerHTML=document.getElementById("hi").value;
}


</script>


</body>
</html>
