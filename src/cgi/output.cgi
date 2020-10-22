#!"C:\xampp\perl\bin\perl.exe"
BEGIN {

       push(@INC,'C:\xampp\perl\lib\CGI.pm');

}

use CGI;

$query = new CGI;

print $query->header;

print $query->start_html('The Unique Page');


$grep_string = "grep userbin.inp |";

open(MASTER, $grep_string);

read(MASTER, $result, 100);

close(MASTER);

&get_options();



sub get_options {

     open(CHOICES, "userbin.inp");

     while (<CHOICES>) {

          $line=$_;

          if (index($line,$name) >= 0) {

               $data_string = $line;

               last;

          }

     }

     close(CHOICES);

     $line = $data_string;

     if (index($line, "Shoes") >= 0 ) {
     		
          &print_company();

     }

     if (index($line, "Goggles") >= 0) {
			
          &print_products();

     }

     if (index($line, "Watches") >= 0) {
     		
          &print_productX();

     }

     if (index($line, "Clothes") >= 0) {
     	
          &print_productY();

     }

}


sub not_found {

     my($name)=@_;

     print "<HR><p>";

     print "There are no options for " . $name . ".<p>";

     print "set options <a href='http://localhost:8080/Perl_1/Input.cgi'";

     print "?user_name=" . $name;

     print ">here</a> to create your dynamic page.";

}

sub print_company {

     open(COMPANY, "maj_announce.html");

    
     while (<COMPANY>) {

          print $_;

     }
     print "<HR>";
     
     close(COMPANY);

}

sub print_products {

     open(PRODUCT, "prod_announce.html");

     while (<PRODUCT>) {

          print $_;

     }
     print "<HR>";

     close(PRODUCT);

}

sub print_productX {

     open(PRODX, "prodx_announce.html");

   
    
     while (<PRODX>) {

          print $_;

     }
     print "<HR>";
     close(PRODX);

}


sub print_productY {

     open(PRODY, "prody_announce.html");

    

     while (<PRODY>) {

          print $_;

     }

     print "<HR>";

     close(PRODY);

}




print $query->end_html;



exit(0);