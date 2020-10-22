#!"C:\xampp\perl\bin\perl.exe"

BEGIN {

      push(@INC,'C:\xampp\perl\lib\CGI.pm');

}

use CGI;

$query = new CGI;

print $query->header;

print $query->start_html('User Name Status');


$grep_string = "grep userbin.inp |";

open(MASTER, $grep_string);

read(MASTER, $result, 100);



&add_choices($query);



sub add_choices {

     my($query)=@_;

     $query_line = "";

     $company = $query->param('shoe');

     if ($company) {
	     
          
          $query_line = $query_line . "<div style='background-color:rgb(200,200,200);margin-left:500px;margin-top:20px;font-size:30px;padding-left:30px;;padding-top:10px;height:45px;width:120px;'>Shoes</div>";

     }

     $products = $query->param('goggle');

     if ($products) {

          $query_line = $query_line . "<div style='background-color:rgb(200,200,200);margin-left:500px;margin-top:20px;font-size:30px;padding-left:30px;;padding-top:10px;height:45px;width:120px;'>Goggles</div>";

     }

     $prodx = $query->param('watch');

     if ($prodx) {

          $query_line = $query_line . "<div style='background-color:rgb(200,200,200);margin-left:500px;font-size:30px;margin-top:20px;padding-left:30px;;padding-top:10px;height:45px;width:120px;'>Watches</div>";

     }

     $prody = $query->param('cloth');

     if ($prody) {

          $query_line = $query_line . "<div style='background-color:rgb(200,200,200);margin-left:500px;font-size:30px;margin-top:20px;padding-left:30px;;padding-top:10px;height:45px;width:120px;'>Clothes</div>";

     }

     open(USER_FILE, ">> userbin.inp") || die "Could not process request";

     $query_line = $query_line . "\n\n";

     print USER_FILE $query_line;

     close(USER_FILE);

     
     
     print "<h1 style='padding-left:290px;background-color:rgb(230,223,150);'>YOUR ADDED INFORMATION ABOUT</h1>";
	 
     print $query_line;
     print "<p style='margin-left:450px;'> Check Your Announcements ";

     print $query->a({href=>"http://localhost/osl/project2/output.cgi"},"Click here");

}

print "<hr>";

print $query->end_html;

exit(0);