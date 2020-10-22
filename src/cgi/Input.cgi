#!"C:\xampp\perl\bin\perl.exe"

BEGIN {

     push(@INC,'C:\xampp\perl\lib\CGI.pm');

}

use CGI;

$query = new CGI;


print $query->header;

print $query->start_html('Choices');


print "<div style='background-color:rgb(255,255,240);margin:0px;'>";

print "<div style='background-color:powderblue; height:100px; width=100%'>

<div style='padding-top:0px; padding-left:410px' >
<h1 >Dyanamic Announcements</h1>
</div>

<div style='padding-left: 1000px;padding-top:-100px;'>
<p style='font-family:sans;font-size:20px;'>
<i>Easy and Fast</i>
</p>
</div>

</div>";



print "<h1 style='margin-left:550px'> Choices</h1>";


print "<div style='background-color:powderblue; height:300px; width:500px; margin-left:360px; margin-top:-10px; font-size:25px;'>";

print $query->start_form(-method=>'POST', -action=>'http://localhost/osl/project2/process_request.cgi');


print $query->checkbox(-name=>'shoe',-label=>'Shoes Announcements',-style=>'margin-left:100px;margin-top:35px;');


print "<br>";

print $query->checkbox(-name=>'goggle',-label=>'Goggles Announcements',-style=>'margin-left:100px;margin-top:35px;');

print "<br>";

print $query->checkbox(-name=>'watch',-label=>'Watches Announcements',-style=>'margin-left:100px;margin-top:35px;');

print "<br>";

print $query->checkbox(-name=>'cloth',-label=>'Clothes Announcements',-style=>'margin-left:100px;margin-top:35px;');

print "<p style='margin-left:170px;background-color:red;width:20px;'>";

print $query->submit(-style=>'background-color:black;font-size:20px;color:white;height:30px;');

print '</div>';
print "<hr style='margin-top:200px;'>";
print "</div>";


print $query->end_html;
