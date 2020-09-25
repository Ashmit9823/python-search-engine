
<html>
<head>
<title>GOOGLE TRIGGERED SEARCH ENGINE</title>
<head>
<body bgcolor = grey>
<form method = get name = form1>
<font align = center color = blue><h1>SEARCH ENGINE</h1></font>
<br><hr height = 10px>
<input type = text name = query placeholder = 'enter your query here'>
<button name = sub>submit</button>
<br>
<?php
if(isset($_GET['sub']))  {
    $Query = $_GET['query'];
    $f_query = str_replace(' ', '+', $Query) ;
    header("location: https://www.google.com?q=$f_query");
}
?>
</form>
</body>
</html>